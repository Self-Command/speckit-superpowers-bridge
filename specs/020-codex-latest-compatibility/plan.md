# Implementation plan: latest Codex compatibility

## Summary

Patch the existing handoff predicates in Bash/PS 5.1, add a narrow convergence
adapter over the installed SK command, and verify the packaged result using the
existing isolated consumer/controller infrastructure.

## Constitution check

- Lightweight/repo-local: no daemon, persistent adapter state or new runtime tool.
- Canonical artifacts: SK documents remain the contract; convergence uses the
  upstream assessment/append rules, never a second planner.
- Ownership: one maintainer writes control artifacts; actual model consumers
  cannot modify installed source files or external validators.
- Cross-agent: mirrored instructions, per-host native command paths, both shells.
- Observability: retain handoff/events/hash behavior and honest evidence labels.
- Native-first: upstream already owns assessment. Its implement-only prerequisite
  does not accept the bridge's alternate executor. The user explicitly selected
  a separate bridge entry; adapt that seam, retain native command bytes, and
  delegate all remaining procedure to its installed text. An upstream issue
  alone cannot deliver the user-authorized fork release in this request.

The post-design check passes with this bounded adapter rather than a copied
convergence algorithm. No constitution amendment is required.

## Interfaces

prepare-convergence.{sh,ps1} accepts an optional native-command path and actor,
checks eligibility read-only, and emits JSON with eligible, feature_directory,
adapter_path and source_sha256. Refusal exits 1 with a reason; usage errors exit 2.
Only a uniquely named OS-temporary adapter is created. The command consumes it
in the current consumer and removes it after the native procedure completes.

The handoff schema and guard semantics stay unchanged. A successful gap result
uses the existing ready transition; a mandatory post-hook failure uses blocked.

## Verification and release

Use real script subprocess tests in disposable Git consumers, then the existing
Linux/Windows full model suite with the candidate ZIP pinned by SHA256. Preserve
the original audit and count every retry in this new 20/6 budget. Source CI also
retains macOS Bash, package, readiness and native Windows gates. Final docs and
metadata must not invalidate the tested runtime digest. Verify published URLs
and clean native installs before closing this feature.
