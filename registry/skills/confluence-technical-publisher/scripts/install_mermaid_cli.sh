#!/usr/bin/env bash
set -euo pipefail

if ! command -v npm >/dev/null 2>&1; then
  echo "npm is required. Install Node.js/npm first, then rerun this script." >&2
  exit 1
fi

if command -v mmdc >/dev/null 2>&1; then
  echo "mmdc already installed: $(mmdc --version)"
  exit 0
fi

echo "Installing @mermaid-js/mermaid-cli globally..."
npm install -g @mermaid-js/mermaid-cli

echo "Installed: $(mmdc --version)"
