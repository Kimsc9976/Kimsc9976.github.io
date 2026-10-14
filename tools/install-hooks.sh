#!/usr/bin/env sh
# Install the plaintext guard without removing an existing pre-commit hook.
set -eu
ROOT=$(git rev-parse --show-toplevel 2>/dev/null) || { echo 'Not in a Git working tree' >&2; exit 1; }
cd "$ROOT"
HOOK_DIR=$(git rev-parse --git-path hooks)
mkdir -p "$HOOK_DIR"
HOOK="$HOOK_DIR/pre-commit"
PREVIOUS="$HOOK_DIR/pre-commit.before-room-guard"
if [ -f "$HOOK" ] && grep -q 'ROOM_GUARD_WRAPPER_V1' "$HOOK"; then
  echo '[room-guard] Already installed'; exit 0
fi
if [ -e "$PREVIOUS" ]; then
  echo "[room-guard] Cannot install: backup already exists at $PREVIOUS" >&2
  exit 1
fi
if [ -e "$HOOK" ]; then
  mv "$HOOK" "$PREVIOUS"
  echo "[room-guard] Existing hook preserved as $PREVIOUS"
fi
cat > "$HOOK" <<'WRAPPER'
#!/usr/bin/env sh
# ROOM_GUARD_WRAPPER_V1
ROOT=$(git rev-parse --show-toplevel) || exit 1
bash "$ROOT/tools/check-room-files.sh" || exit $?
HOOK_DIR=$(CDPATH='' cd "$(dirname "$0")" && pwd)
if [ -x "$HOOK_DIR/pre-commit.before-room-guard" ]; then
  "$HOOK_DIR/pre-commit.before-room-guard" "$@" || exit $?
fi
WRAPPER
chmod +x "$HOOK"
echo "[room-guard] Installed at $HOOK"
