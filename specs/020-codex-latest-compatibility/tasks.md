# Tasks: latest Codex compatibility

Generated following Spec Kit 1.1.3's installed tasks command from spec.md and
plan.md. Exactly one maintainer owns these control artifacts.

## Phase 1: Setup

- [x] T001 Create the isolated fork checkout and record the approved scope in specs/020-codex-latest-compatibility/spec.md and plan.md.

## Phase 2: Foundation

- [x] T002 Add subprocess regression fixtures in tests/test_bridge_regressions.py and the native converge fixture in tests/fixtures/.

## Phase 3: US1 — required artifacts

- [x] T003 [US1] Observe the missing-ready failures, correct both update-handoff shell predicates, and verify restoration/idle/archive behavior.

## Phase 4: US2 — convergence

- [x] T004 [US2] Implement both prepare-convergence shell flavors with read-only eligibility and a temporary native-text adapter.
- [x] T005 [US2] Register the convergence command and synchronize project-owned Codex/Claude instructions, command counts and package tests.
- [x] T006 [US2] Verify refusal, hashes, events, task completion, upstream immutability and adapter parity with actual subprocesses.

## Phase 5: US3 — verified release

- [x] T007 [US3] Add candidate Actions gates and adapt the existing test controller to consume the pinned candidate package.
- [x] T008 [US3] Run the full bounded Codex Linux/Windows regression, including real PR creation and both-platform convergence.
- [x] T009 [US3] Update README support claims, verification evidence and all version metadata after required checks pass.
- [ ] T010 [US3] Run final package gates and publish v1.4.0 with both ZIP names and SHA256 checksums.
- [ ] T011 [US3] Verify published installs and write the evidence-based detailed Chinese tutorial in the external local workspace.

## Dependencies and strategy

T001 → T002 → T003; T004/T005 → T006; T003/T006 → T007 → T008 → T009 →
T010 → T011. Shell implementations touch separate files but one maintainer keeps
control writes sequential. The first shippable slice is US1; release includes
all three stories. Every completion checkbox requires observed evidence.
