#!/usr/bin/env bash
set -euo pipefail

BASE_URL=${BASE_URL:-https://realagiorganization.github.io/vlc/}
export BASE_URL

if [[ -n "${DISPLAY:-}" ]] && [[ -S /tmp/.X11-unix/X0 || -S /tmp/.X11-unix/X1 ]]; then
  python3 -m behave /repo/test/bdd/features
else
  xvfb-run -a python3 -m behave /repo/test/bdd/features
fi
