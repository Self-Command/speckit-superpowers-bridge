#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BRIDGE_TEST_FLAVOR=sh python3 "$ROOT/tests/test_bridge_regressions.py" -v
