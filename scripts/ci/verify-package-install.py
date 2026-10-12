"""Install the candidate with native SK, then test the installed shell files."""
from pathlib import Path
import argparse
import hashlib
import json
import os
import subprocess
import sys
import tempfile
import functools
import http.server
import threading
import zipfile

parser = argparse.ArgumentParser()
parser.add_argument('--zip', type=Path, required=True)
parser.add_argument('--index', type=Path, required=True)
args = parser.parse_args()
archive = args.zip.resolve()
index = json.loads(args.index.read_text())
assert hashlib.sha256(archive.read_bytes()).hexdigest() == index['zip_sha256']
repo = Path(__file__).resolve().parents[2]
win = os.name == 'nt'
env = os.environ.copy()
env.update(PYTHONUTF8='1', PYTHONIOENCODING='utf-8')
if win:
    env['PSModulePath'] = str(Path(os.environ['SystemRoot']) / 'System32/WindowsPowerShell/v1.0/Modules')


def command(arguments, cwd, input=None):
    subprocess.run(list(map(str, arguments)), cwd=cwd, env=env, input=input, text=True,
                   encoding='utf-8', check=True, timeout=600)


with tempfile.TemporaryDirectory(prefix='bridge-native-install-') as temporary:
    base = Path(temporary)
    venv = base / 'venv'
    command([sys.executable, '-m', 'venv', venv], base)
    python = venv / ('Scripts/python.exe' if win else 'bin/python')
    specify = venv / ('Scripts/specify.exe' if win else 'bin/specify')
    command([python, '-m', 'pip', 'install', '--quiet',
             'git+https://github.com/github/spec-kit.git@0282d03eb6fc3091b3deaa3a855d4030dc40cd6c'], base)
    consumer = base / 'consumer'
    consumer.mkdir()
    command([specify, 'init', '--here', '--force', '--non-interactive', '--integration',
             'codex', '--script', 'ps' if win else 'sh', '--ignore-agent-tools'], consumer)
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(archive.parent))
    server = http.server.ThreadingHTTPServer(('127.0.0.1', 0), handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    url = 'http://127.0.0.1:' + str(server.server_port) + '/' + archive.name
    try:
        command([specify, 'extension', 'add', 'speckit-superpowers-bridge', '--from', url], consumer, 'y\n')
        command([specify, 'extension', 'add', 'speckit-superpowers-bridge', '--from', url, '--force'], consumer, 'y\n')
    finally:
        server.shutdown()
        server.server_close()
    extension = consumer / '.specify/extensions/speckit-superpowers-bridge'
    with zipfile.ZipFile(archive) as package:
        for name in package.namelist():
            if name == 'extension.yml' or name.startswith(('scripts/', 'commands/')):
                assert (extension / name).read_bytes() == package.read(name), name
    for name in ('speckit-superpowers-bridge', 'speckit-speckit-superpowers-bridge-execute',
                 'speckit-speckit-superpowers-bridge-handoff', 'speckit-speckit-superpowers-bridge-guard',
                 'speckit-speckit-superpowers-bridge-converge', 'speckit-converge'):
        assert (consumer / '.agents/skills' / name / 'SKILL.md').is_file(), name
    env['BRIDGE_TEST_SCRIPTS'] = str(extension / 'scripts')
    env['BRIDGE_TEST_FLAVOR'] = 'ps' if win else 'sh'
    command([sys.executable, repo / 'tests/test_bridge_regressions.py', '-v'], repo)
    print(json.dumps({'native_install': 'passed', 'native_reinstall': 'passed', 'script_flavor': env['BRIDGE_TEST_FLAVOR'],
                      'zip_sha256': index['zip_sha256'], 'source_sha': index['source_sha']}))
