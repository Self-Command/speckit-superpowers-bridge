# v1.4.0 verification

## Artifact

- Version: 1.4.0
- SHA256: Pending final artifact

## Platform matrix

| Platform | Result | Evidence |
|---|---|---|
| Linux bash | PENDING | Candidate Actions and bounded model regression have not run. |
| Windows PowerShell | PENDING | Thirteen local subprocess regressions passed; hosted/native installation and model regression pending. |
| macOS bash | PENDING | Existing hosted shell gate retained; live Codex workflow not in scope. |

## Agents

| Agent | Result | Evidence |
|---|---|---|
| Codex | PENDING | Exact pinned Linux/Windows model run pending. |
| Claude Code | NOT TESTED | Only mirrored-source structural checks are planned; no live-agent compatibility claim. |

| Check | Result | Evidence |
|---|---|---|
| Release workflow inventory | PENDING | Final publication gates not run. |

## Known Blockers and Deferrals

The original native SK convergence command still requires SK implement. The new
bridge entry adapts the executor seam explicitly, without editing upstream files.
Publication is blocked until the candidate suite passes. This file records
observed outcomes only; local regressions do not prove model compatibility.

## Local regression evidence

On native PowerShell 5.1, the unpatched ready requests reproduced missing-artifact
failures for spec.md, plan.md and tasks.md. After fixing both predicates, thirteen
subprocess tests passed, including restoration, idle/archive, event/hash/task
qualification, refusal without input mutation and exact adapter-text retention.
The host PSModulePath was isolated to native Windows modules for these tests.
The UTF-8 read fix preserves Unicode text when PS 5.1 prepares the adapter.
