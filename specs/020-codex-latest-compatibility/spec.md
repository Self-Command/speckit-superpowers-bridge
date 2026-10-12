# Feature: Codex compatibility with SK 1.1.3 and SP 7.0.0

## Context

The original v1.3.0 audit covered 44 Linux/Windows scenarios. Six missing-artifact
cases incorrectly wrote ready; native SK converge rejected SP-completed tasks;
PR creation was blocked by the test repository's Actions setting.

## User stories

- **US1 (P1)**: A maintainer receives blocked when an active feature lacks any
  required design artifact, and ready after the files are restored.
- **US2 (P1)**: A Codex user assesses an SP-completed feature through a bridge
  convergence entry without running or claiming to have run SK implement.
- **US3 (P2)**: A user installs a release whose exact package and compatibility
  claims have been checked by the bounded Actions regression suite.

## Functional requirements

- FR-001: Both shell flavors block ready/executing requests when an identified
  feature lacks spec.md, plan.md or tasks.md. Exit conventions remain compatible.
- FR-002: Idle ready and completed-feature archival remain supported.
- FR-003: Provide speckit.speckit-superpowers-bridge.converge; keep five hooks.
- FR-004: Qualify convergence using feature identity, executing/completion events,
  complete SP handoff, exact artifact hashes and completed non-deferred tasks.
  Reject ineligible or unrecognized input without modifying consumer artifacts.
- FR-005: Adapt the installed native converge instructions in a temporary file:
  replace only its execution prerequisite and executor references. Preserve
  native intent assessment, append-only rules and before/after convergence hooks.
- FR-006: Inspect real implementation and verification results. No gaps means
  byte-identical tasks; gaps append traceable increasing IDs and restore ready.
  Mandatory post-hook failure leaves blocked. Never write application code.
- FR-007: Keep official installed SK/SP bytes intact; retain the native SK
  implement prerequisite as a documented limitation of the original entry.
- FR-008: Test pinned SK 1.1.3/SP 7.0.0/Codex 0.162.1 with gpt-6.1-sol low,
  at most 20 new main calls and six reviewers across all attempts.
- FR-009: Release v1.4.0 from Self-Command's fork only after required gates pass.
  Keep root/nested manifests identical; report actual platform/agent evidence.

## Success criteria

- SC-001: Native PS 5.1 and Linux regressions pass for each missing file,
  multiple missing files, restoration, idle and archive cases.
- SC-002: Both platforms demonstrate clean convergence and gap assessment with
  append-only tasks, immutable spec/plan/code and unchanged upstream skills.
- SC-003: The new Actions coverage maps back to all 44 audit items, with the
  chosen convergence entry separately distinguished from original SK behavior.
- SC-004: Published versioned/stable ZIPs match checked SHA256 values and install
  on Linux and Windows; macOS receives its existing shell gate.

## Boundaries

No new planner, state machine, schema version, registered hooks, upstream source
patches or unsolicited marketplace submissions. Claude runtime verification is
not inferred from skill parity. The detailed Chinese tutorial stays outside this
source repository in the user's local workspace.
