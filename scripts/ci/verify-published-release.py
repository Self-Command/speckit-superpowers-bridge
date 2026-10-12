"""Verify public pinned/latest downloads, checksums, and native SK installation."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import tempfile
import urllib.request

tag,repository=sys.argv[1:]
version=tag.removeprefix('v')
repo=Path(__file__).resolve().parents[2]
with tempfile.TemporaryDirectory(prefix='bridge-published-release-') as temporary:
    target=Path(temporary)
    base='https://github.com/'+repository+'/releases/download/'+tag+'/'
    names=('speckit-superpowers-bridge-v'+version+'.zip','speckit-superpowers-bridge.zip',
           'SHA256SUMS','release-index.json')
    for name in names:
        urllib.request.urlretrieve(base+name,target/name)
    urllib.request.urlretrieve('https://github.com/'+repository+'/releases/latest/download/speckit-superpowers-bridge.zip',target/'latest.zip')
    sums={line.split()[1]:line.split()[0] for line in (target/'SHA256SUMS').read_text().splitlines()}
    for name in names[:2]:
        assert hashlib.sha256((target/name).read_bytes()).hexdigest()==sums[name],name
    assert (target/names[0]).read_bytes()==(target/names[1]).read_bytes()==(target/'latest.zip').read_bytes()
    index=json.loads((target/'release-index.json').read_text())
    assert index['zip_sha256']==sums[names[0]]
    subprocess.run([sys.executable,repo/'scripts/ci/verify-package-install.py',
                    '--zip',target/names[0],'--index',target/'release-index.json'],check=True)
    print(json.dumps({'published_downloads':'passed','pinned_and_latest_identical':True,
                      'zip_sha256':index['zip_sha256']}))
