# v1.4.0 verification

## Artifact

- Version: 1.4.0
- SHA256: 6c660203795b8f4bd47deb75f235fbf46039f0a7aefaac0036d3563ca66b9e3a
- Final packaged-docs source: 057f42fec01af8a03fab0402694cba200870b1b6
- Model candidate source: 048cf1e9b839ef34fcf1a36e0af2cabcc1d06e44
- Model candidate ZIP SHA256: b1aad8b436764e7ba95887169cb6bbb4a72ffd14257e323d8b521dc2d25b1146
- Same tested runtime SHA256: 086566a6073989bbed12a2568c2890a7271be20f1965c66a32b1a83768561531

Only README, changelog, verification metadata and source-only evidence changed
after the model candidate. The final package runtime hash matches exactly.
This evidence file is outside the ZIP, so recording its final hash is acyclic.

## Platform matrix

| Platform | Runtime | Result | Evidence |
|---|---|---|---|
| Linux bash | SK 1.1.3 / SP 7.0.0 | PASS | Real-model complete workflow and bridge convergence; final native install/reinstall with installed-script regressions. |
| Windows PowerShell | Native PS 5.1 / SK 1.1.3 / SP 7.0.0 | PASS | Real-model complete workflow and bridge convergence; final native install/reinstall with installed-script regressions. |
| macOS bash | Supported Homebrew Bash + jq | PASS | Hosted source smoke and portability only; no live Codex workflow or public package installation claim. |

Final package gates: [Actions 38293135133](https://github.com/Self-Command/speckit-superpowers-bridge/actions/runs/38293135133).
All three jobs passed after final README/metadata updates.

## Agents

| Agent | Version/model | Result | Evidence |
|---|---|---|---|
| Codex | CLI 0.162.1 / gpt-6.1-sol / low | PASS | Native Linux and Windows; cumulative 20 main calls and 6 reviews. |
| Claude Code | No live version verified | NOT TESTED | Mirrored-source structural checks only. |

| Check | Scope | Result | Evidence |
|---|---|---|---|
| Release workflow inventory | Existing script paths, gates, builder and public install jobs | PASS | Final source gate runs release-tooling self-tests; Linux/Windows/macOS gates precede publishing. |
| Required model coverage | Original 44 mapped checks plus both-platform bridge convergence | PASS | 90 recorded checks passed, including process and retained duplicate checks; zero fail/blocked/uncovered. |
| Independent evidence gate | Actual counters, model settings, same candidate and file bytes | PASS | [Actions 38292614419](https://github.com/Self-Command/sp-sk-bridge-compat-ci/actions/runs/38292614419). |

## Model evidence and observed usage

- [Original model run](https://github.com/Self-Command/sp-sk-bridge-compat-ci/actions/runs/38283007683): 11 main calls and 3 reviewers; raw failure evidence retained.
- [Selective continuation](https://github.com/Self-Command/sp-sk-bridge-compat-ci/actions/runs/38289599150): 9 more main calls and 3 more reviewers, same candidate and actual snapshots; cumulative 20/6.
- [Final no-model evidence gate](https://github.com/Self-Command/sp-sk-bridge-compat-ci/actions/runs/38292614419): PASS, full candidate-final-evidence artifact.
- Actual usage: input 8,697,973; cached input 7,667,211 (subset of input); non-cached input 1,030,762; output 63,070; 26 recorded main/reviewer sessions.
- [Real test PR #5](https://github.com/Self-Command/sp-sk-bridge-compat-ci/pull/5) created, unmerged. Test-repository Issue/MCP and branch evidence retained.

Original failed results are preserved. Free regrading fixes only two proven
retrieval defects: the full malformed-registry parser diagnostic was in earlier
tool output, and the convergence entry was in the final exported sessions rather
than the stale export originally inspected. Original JSON and all three field
adjustments are retained. Independent byte grading also accounts for the exact
Windows CRLF fixture suffix; it does not alter tested snapshots.

Earlier external harness fixes follow the actual SK-selected root unittest layout,
require a real nonempty suite, and recognize failed-then-passed tests inside batch
output. The same native package and actual paid counters were retained. Snapshot
restoration commits are explicitly named as restoration; original Git logs and
rollouts remain the evidence of the original commits.

## Known Blockers and Deferrals

No required release-candidate check remains blocked. The original native SK
convergence command retains its SK implement prerequisite. SP-completed features
use the separately named bridge entry. Native SK/SP skills remain byte-identical;
unrecognized future SK convergence text stops rather than silently adapting.
Claude Code was not live-tested and macOS has only hosted shell coverage.

Public release URLs, final published checksums and post-publication Linux/Windows
installs will be recorded after the tag workflow completes. No upstream marketplace
submission is authorized or performed.

## Local regression evidence

On native PowerShell 5.1, the unpatched ready requests reproduced missing-artifact
failures for spec.md, plan.md and tasks.md. After fixing both predicates, thirteen
subprocess tests passed, including restoration, idle/archive, event/hash/task
qualification, refusal without input mutation and exact adapter-text retention.
The host PSModulePath was isolated to native Windows modules for these tests.
The UTF-8 read fix preserves Unicode text when PS 5.1 prepares the adapter.
