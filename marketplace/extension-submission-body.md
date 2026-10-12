# Extension Submission: Superpowers Implementation Bridge

Local reference template for the maintained Self-Command fork. No upstream submission has been made.

### Extension ID

speckit-superpowers-bridge

### Extension Name

Superpowers Implementation Bridge

### Version

1.4.0

### Description

Maintained repair fork connecting Spec Kit design artifacts to Superpowers execution, with required-document blocking and a separate convergence entry.

### Author

Original: lihan3238. Fork maintainer: Self-Command.

### Repository URL

https://github.com/Self-Command/speckit-superpowers-bridge

### Download URL

https://github.com/Self-Command/speckit-superpowers-bridge/releases/download/v1.4.0/speckit-superpowers-bridge-v1.4.0.zip

Stable alias: https://github.com/Self-Command/speckit-superpowers-bridge/releases/latest/download/speckit-superpowers-bridge.zip

### License

MIT

### Required Spec Kit Version

>=0.8.10; tested combination is SK 1.1.3 / SP 7.0.0 / Codex CLI 0.162.1.

### Required Tools

Bash >=4.0 with jq >=1.6, or Windows PowerShell >=5.1. Native Superpowers skills and Spec Kit agent integration are required.

### Number of Commands

4

### Number of Hooks

5

### Tags

bridge, superpowers, cross-agent, tdd, workflow

### Key Features

- Missing active spec/plan/tasks documents block ready or executing handoffs on both shells.
- Convergence qualifies SP completion evidence and reads the installed native SK procedure into a temporary adapter. Clean tasks remain byte-identical; gaps append traceable tasks and return ready; mandatory post-hook failure blocks.
- Native SK/SP files remain unchanged; original SK converge still requires SK implement.
- Fixed candidate source, ZIP digest, cumulative counters, actual files, commands, task states, sessions and token records establish acceptance.

### Support Matrix

| Target | Result | Evidence |
|---|---|---|
| Linux bash | PASS | Native SK 1.1.3 install and real Codex workflow. |
| Windows PowerShell | PASS | Native SK 1.1.3 install and real Codex workflow. |
| macOS bash | SHELL PASS | Hosted script gates only. |
| Codex | PASS | CLI 0.162.1 / gpt-6.1-sol / low, both platforms. |
| Claude Code | NOT TESTED | Mirrored-source checks only. |

### Release Validation Summary

- `validate-release-readiness.ps1`: final artifact hash and source evidence checked before tagging.
- `bash tests/run-all.sh`: source candidate gate passed.
- `tests/test-release-powershell.ps1`: native source candidate gate passed.
- Final repackaging/install gates must pass before publication.
- [Actual final model evidence](https://github.com/Self-Command/sp-sk-bridge-compat-ci/actions/runs/38292614419); [source script/install gate](https://github.com/Self-Command/speckit-superpowers-bridge/actions/runs/38287975618).

### Testing Checklist

- [x] Candidate ZIP installed through the native extension installer on Linux/Windows.
- [x] Required workflow checks and both-platform convergence passed.
- [x] Original 44-item audit mapping retained; real test PR created.
- [x] 20 main calls and 6 reviews retained across failure/continuation.
- [ ] Public asset download and post-publication installs: recorded after release in verification.md.

### Submission Requirements

- [x] Root/nested manifests match; four commands and five hooks.
- [x] README, CHANGELOG and MIT LICENSE included.
- [ ] Public v1.4.0 release creation: performed only after final package gates.
- [ ] Upstream submission is outside the authorized scope of this run.

### Testing Details

Actual model checks: 90 passed, zero failed/blocked/uncovered after correcting two evidence retrieval defects. Raw results and correction reasons remain available. Candidate runtime SHA256: `086566a6073989bbed12a2568c2890a7271be20f1965c66a32b1a83768561531`. Cumulative usage: 8,697,973 input tokens (7,667,211 cached), 63,070 output tokens; 26 recorded sessions. No additional model calls in evidence regrading.

### Example Usage

```bash
specify extension add speckit-superpowers-bridge --from https://github.com/Self-Command/speckit-superpowers-bridge/releases/latest/download/speckit-superpowers-bridge.zip
```

```text
$speckit-superpowers-bridge
$speckit-speckit-superpowers-bridge-converge
```

Claude Code mirrors these as `/speckit-superpowers-bridge` and `/speckit-speckit-superpowers-bridge-converge`; its live behavior was not tested here.

AI-assistance disclosure: Codex implemented and tested this maintained repair fork. Original upstream attribution and MIT license are preserved.

### Proposed Catalog Entry

```json
{
  "speckit-superpowers-bridge": {
    "name": "Superpowers Implementation Bridge",
    "id": "speckit-superpowers-bridge",
    "description": "Thin orchestrator between Spec Kit (design) and Superpowers (implementation). Cross-agent.",
    "author": "lihan3238",
    "version": "1.4.0",
    "download_url": "https://github.com/Self-Command/speckit-superpowers-bridge/releases/download/v1.4.0/speckit-superpowers-bridge-v1.4.0.zip",
    "repository": "https://github.com/Self-Command/speckit-superpowers-bridge",
    "homepage": "https://github.com/Self-Command/speckit-superpowers-bridge",
    "documentation": "https://github.com/Self-Command/speckit-superpowers-bridge#readme",
    "changelog": "https://github.com/Self-Command/speckit-superpowers-bridge/blob/main/CHANGELOG.md",
    "license": "MIT",
    "category": "process",
    "effect": "read-write",
    "requires": {
      "speckit_version": ">=0.8.10",
      "tools": [
        {
          "name": "powershell",
          "version": ">=5.1",
          "required": false
        },
        {
          "name": "bash",
          "version": ">=4.0",
          "required": false
        },
        {
          "name": "jq",
          "version": ">=1.6",
          "required": false
        }
      ]
    },
    "provides": {
      "commands": 4,
      "hooks": 5
    },
    "tags": [
      "bridge",
      "superpowers",
      "cross-agent",
      "tdd",
      "workflow"
    ],
    "verified": false,
    "downloads": 0,
    "stars": 0,
    "created_at": "2026-05-15T00:00:00Z",
    "updated_at": "2026-10-12T16:57:57Z"
  }
}
```
