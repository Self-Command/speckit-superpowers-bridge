"""Exercise real bridge scripts in disposable consumers, never mock their output."""
from pathlib import Path
import hashlib
import json
import os
import shutil
import subprocess
import tempfile
import unittest

REPO = Path(__file__).resolve().parents[1]
FLAVOR = os.environ.get('BRIDGE_TEST_FLAVOR', 'ps' if os.name == 'nt' else 'sh')
SCRIPTS = Path(os.environ.get('BRIDGE_TEST_SCRIPTS', REPO / '.specify/extensions/speckit-superpowers-bridge/scripts'))


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


class Consumer(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='bridge-regression-')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        subprocess.run(['git', 'init', '-q', str(self.root)], check=True)
        self.feature = self.root / 'specs/001-regression'
        self.feature.mkdir(parents=True)
        (self.root / '.specify/memory').mkdir(parents=True)
        self.write('.specify/feature.json', json.dumps({'feature_directory': 'specs/001-regression'}))
        self.write('.specify/init-options.json', json.dumps({'script': FLAVOR}))
        self.write('.specify/memory/constitution.md', '# Constitution\n')
        self.write('specs/001-regression/spec.md', '# Spec\nFR-001: normalize titles.\n')
        self.write('specs/001-regression/plan.md', '# Plan\nPython standard library.\n')
        self.write('specs/001-regression/tasks.md', '# Tasks\n- [x] T001 Normalize titles.\n')
        self.handoff = self.root / '.specify/superpowers-handoff.json'
        self.events = self.root / '.specify/bridge-events.jsonl'
        self.native = self.root / '.agents/skills/speckit-converge/SKILL.md'
        self.native.parent.mkdir(parents=True)
        shutil.copyfile(REPO / 'tests/fixtures/speckit-converge-codex.md', self.native)

    def write(self, relative, body):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(body, encoding='utf-8', newline='\n')

    def invoke(self, stem, **args):
        if FLAVOR == 'ps':
            command = ['powershell.exe', '-NoProfile', '-ExecutionPolicy', 'Bypass', '-File',
                       str(SCRIPTS / 'powershell' / (stem + '.ps1'))]
            for key, value in args.items():
                command.append('-' + ''.join(part.title() for part in key.split('_')))
                if value is not True:
                    command.append(str(value))
        else:
            command = ['bash', str(SCRIPTS / 'bash' / (stem + '.sh'))]
            for key, value in args.items():
                command.append('--' + key.replace('_', '-'))
                if value is not True:
                    command.append(str(value))
        env = os.environ.copy()
        if os.name == 'nt' and FLAVOR == 'ps':
            env['PSModulePath'] = str(Path(os.environ['SystemRoot']) / 'System32/WindowsPowerShell/v1.0/Modules')
        return subprocess.run(command, cwd=self.root, env=env, capture_output=True, text=True,
                              encoding='utf-8', errors='replace', timeout=30)

    def update(self, status):
        result = self.invoke('update-handoff', status=status, actor='codex')
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        return json.loads(self.handoff.read_text(encoding='utf-8-sig'))

    def completed(self):
        self.update('executing')
        return self.update('complete')

    def prepare(self):
        return self.invoke('prepare-convergence', native_command=self.native, actor='codex')

    def protected(self):
        paths = [self.native, self.handoff, self.events, *self.feature.glob('*.md')]
        return {str(path): digest(path) for path in paths if path.exists()}

    def refusal(self):
        before = self.protected()
        result = self.prepare()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        data = json.loads(result.stdout)
        self.assertFalse(data['eligible'])
        self.assertTrue(data['reason'])
        self.assertEqual(before, self.protected())


class RequiredArtifacts(Consumer):
    def test_each_missing_file_blocks_ready_and_executing(self):
        for name in ('spec.md', 'plan.md', 'tasks.md'):
            path = self.feature / name
            original = path.read_bytes()
            path.unlink()
            for requested in ('ready', 'executing'):
                with self.subTest(name=name, requested=requested):
                    state = self.update(requested)
                    self.assertEqual(state['status'], 'blocked')
                    self.assertIn(name, state['blocked_reason'])
                    event = json.loads([line for line in self.events.read_text(encoding='utf-8-sig').splitlines() if line.strip()][-1])
                    self.assertEqual(event['status'], 'blocked')
                    self.assertIn(name, event['reason'])
            path.write_bytes(original)
            self.assertEqual(self.update('ready')['status'], 'ready')

    def test_multiple_missing_files_and_missing_directory(self):
        (self.feature / 'spec.md').unlink()
        (self.feature / 'plan.md').unlink()
        state = self.update('ready')
        self.assertEqual(state['status'], 'blocked')
        self.assertIn('spec.md', state['blocked_reason'])
        self.assertIn('plan.md', state['blocked_reason'])
        shutil.rmtree(self.feature)
        state = self.update('ready')
        self.assertEqual(state['status'], 'blocked')
        self.assertIn('tasks.md', state['blocked_reason'])

    def test_idle_and_archive_are_ready(self):
        (self.root / '.specify/feature.json').unlink()
        self.assertEqual(self.update('ready')['status'], 'ready')
        self.write('.specify/feature.json', json.dumps({'feature_directory': 'specs/001-regression'}))
        self.completed()
        result = self.invoke('auto-archive-handoff', actor='codex')
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        state = json.loads(self.handoff.read_text(encoding='utf-8-sig'))
        self.assertEqual(state['status'], 'ready')
        self.assertIsNone(state['feature_directory'])


class ConvergenceAdapter(Consumer):
    def test_native_procedure_is_preserved_and_all_inputs_are_read_only(self):
        self.completed()
        before = self.protected()
        result = self.prepare()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        data = json.loads(result.stdout)
        self.assertTrue(data['eligible'])
        adapter = Path(data['adapter_path'])
        self.addCleanup(adapter.unlink, missing_ok=True)
        self.assertFalse(adapter.is_relative_to(self.root))
        self.assertEqual(data['source_sha256'], digest(self.native))
        self.assertEqual(data['feature_directory'], 'specs/001-regression')
        original = self.native.read_text(encoding='utf-8')
        modified = adapter.read_text(encoding='utf-8')
        old = ('This command MUST run only after\n'
               '`$speckit-implement` has run on the current `tasks.md`, and after '
               '`$speckit-tasks` has produced a complete `tasks.md`.')
        new = ('This bridge adapter MUST run only after verified Superpowers completion '
               'of the current `tasks.md`, and after `$speckit-tasks` has produced a complete `tasks.md`.')
        expected = original.replace(old, new).replace('`$speckit-implement`', '`$speckit-superpowers-bridge`')
        self.assertEqual(modified, expected)
        self.assertIn('## Pre-Execution Checks', modified)
        self.assertIn('APPEND-ONLY, NEVER REWRITE', modified)
        self.assertIn('### 9. Check for extension hooks', modified)
        self.assertEqual(before, self.protected())

    def test_complete_without_execution_events_is_rejected(self):
        self.update('complete')
        self.refusal()

    def test_forged_complete_missing_hashes_is_rejected(self):
        state = self.completed()
        del state['artifacts_sha256']
        self.write('.specify/superpowers-handoff.json', json.dumps(state))
        self.refusal()

    def test_changed_artifacts_are_rejected(self):
        for name in ('spec.md', 'plan.md', 'tasks.md'):
            with self.subTest(name=name):
                self.completed()
                path = self.feature / name
                original = path.read_bytes()
                path.write_bytes(original + b'\nchanged\n')
                self.refusal()
                path.write_bytes(original)

    def test_pending_tasks_are_rejected_but_deferred_tasks_are_allowed(self):
        self.write('specs/001-regression/tasks.md', '- [ ] T001 Pending work\n')
        self.completed()
        self.refusal()
        self.write('specs/001-regression/tasks.md', '- [x] T001 Done\n## Deferred\n- [ ] T002 Later\n')
        self.completed()
        result = self.prepare()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        adapter = Path(json.loads(result.stdout)['adapter_path'])
        self.addCleanup(adapter.unlink, missing_ok=True)

    def test_empty_task_contract_is_rejected(self):
        self.write('specs/001-regression/tasks.md', '# Empty tasks\n')
        self.completed()
        self.refusal()

    def test_non_complete_and_mismatched_feature_are_rejected(self):
        self.update('executing')
        self.refusal()
        self.completed()
        self.write('.specify/feature.json', json.dumps({'feature_directory': 'specs/002-other'}))
        self.refusal()

    def test_missing_artifact_is_rejected(self):
        self.completed()
        (self.feature / 'plan.md').unlink()
        self.refusal()

    def test_unrecognized_native_text_is_rejected(self):
        self.completed()
        self.native.write_text('# Changed upstream command\n', encoding='utf-8')
        self.refusal()

    def test_completion_event_must_match_current_snapshot(self):
        self.completed()
        events = [line for line in self.events.read_text(encoding='utf-8-sig').splitlines() if line.strip()]
        last = json.loads(events[-1])
        last['snapshot_id'] = 'unrelated-snapshot'
        self.write('.specify/bridge-events.jsonl', '\n'.join([*events[:-1], json.dumps(last)]) + '\n')
        self.refusal()


if __name__ == '__main__':
    unittest.main()
