"""Hash only the shipped execution contract; release evidence/docs are separate."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys

root = Path(__file__).resolve().parents[2]
extension = root / '.specify/extensions/speckit-superpowers-bridge'
files = [extension / 'extension.yml']
files += [p for directory in ('commands', 'scripts') for p in (extension / directory).rglob('*') if p.is_file()]
runtime = hashlib.sha256()
for path in sorted(files):
    runtime.update(path.relative_to(extension).as_posix().encode() + b'\0')
    runtime.update(path.read_bytes() + b'\0')
output = {'source_sha': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=root, text=True).strip(),
          'runtime_sha256': runtime.hexdigest()}
if len(sys.argv) > 1:
    archive = Path(sys.argv[1])
    output.update(zip_name=archive.name, zip_sha256=hashlib.sha256(archive.read_bytes()).hexdigest())
print(json.dumps(output, indent=2))
