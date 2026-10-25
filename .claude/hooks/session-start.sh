#!/bin/bash
# Install the OpenSpec CLI in Claude Code cloud sessions so the /opsx:* commands work.
set -euo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

if ! command -v openspec >/dev/null 2>&1; then
  npm install -g @fission-ai/openspec@latest >/dev/null 2>&1
fi

if [ -n "${CLAUDE_ENV_FILE:-}" ]; then
  echo "export OPENSPEC_TELEMETRY=0" >> "$CLAUDE_ENV_FILE"
fi
