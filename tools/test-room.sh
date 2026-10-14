#!/usr/bin/env bash
# Isolated smoke checks: never writes ciphertext or dummy lyrics into the actual repo.
set -euo pipefail
# Parse the browser-side JavaScript before any encrypted fixture tests.
node -e 'const fs=require("fs"); const h=fs.readFileSync(process.argv[1],"utf8"); const s=h.match(/<script>([\s\S]*?)<\/script>/); if(!s)throw Error("missing inline JS"); new Function(s[1]);' "$(cd "$(dirname "$0")/.." && pwd)/room/index.html"
SOURCE_ROOT=$(cd "$(dirname "$0")/.." && pwd)
TEMP=$(mktemp -d)
trap 'rm -rf "$TEMP"' EXIT
mkdir -p "$TEMP/tools" "$TEMP/.private/lyrics"
cp "$SOURCE_ROOT/tools/room-encrypt.mjs" "$TEMP/tools/"
cp "$SOURCE_ROOT/tools/check-room-files.sh" "$TEMP/tools/"
cp "$SOURCE_ROOT/tools/install-hooks.sh" "$TEMP/tools/"
cat > "$TEMP/.private/lyrics/dummy.json" <<'JSON'
{"id":"demo","title":"Dummy Test","artist":"Local Only","youtube":"dQw4w9WgXcQ","lines":[{"t":0,"o":"TEST_ONLY_PRIVATE_LYRICS_43fa","p":"test","k":"translation"}]}
JSON
cd "$TEMP"
export ROOM_PASSWORD='correct-horse-battery-staple-2026'
node tools/room-encrypt.mjs > /dev/null
if grep -qr 'TEST_ONLY_PRIVATE_LYRICS_43fa' assets/room; then
  echo 'FAIL: plaintext found in published assets' >&2; exit 1
fi
# Cross-compatibility: decrypt Node-encrypted artifacts through the same
# WebCrypto derivation and AES-GCM inputs used by the browser page.
node --input-type=module <<'JS'
import { readFileSync, readdirSync } from 'node:fs';
import { webcrypto, createHmac } from 'node:crypto';
const { subtle } = webcrypto;
const read = f => JSON.parse(readFileSync(`assets/room/${f}`, 'utf8'));
const dec64 = s => new Uint8Array(Buffer.from(s, 'base64'));
const manifest = read('manifest.json');
const pw = process.env.ROOM_PASSWORD.normalize('NFC');
const key = await subtle.importKey('raw', new TextEncoder().encode(pw), 'PBKDF2', false, ['deriveBits']);
const bits = new Uint8Array(await subtle.deriveBits({ name: 'PBKDF2', hash: 'SHA-256', salt: dec64(manifest.salt), iterations: manifest.iter }, key, 512));
const aes = await subtle.importKey('raw', bits.slice(0, 32), 'AES-GCM', false, ['decrypt']);
const open = async filename => {
  const { iv, ct } = read(filename);
  const plain = await subtle.decrypt({ name: 'AES-GCM', iv: dec64(iv), additionalData: new TextEncoder().encode('room-v1') }, aes, dec64(ct));
  return JSON.parse(new TextDecoder().decode(plain));
};
const index = await open('index.enc.json');
if (index.songs.length !== 1 || index.songs[0].title !== 'Dummy Test') throw Error('browser cannot decrypt index');
const item = index.songs[0];
const expectedFilename = createHmac('sha256', Buffer.from(bits.slice(32, 64))).update(item.id).digest('hex').slice(0,24) + '.enc.json';
if (expectedFilename !== item.file || !readdirSync('assets/room').includes(item.file)) throw Error('HMAC filename mismatch');
const song = await open(item.file);
if (song.lines[0].o !== 'TEST_ONLY_PRIVATE_LYRICS_43fa') throw Error('browser cannot decrypt lyrics');
JS
if ROOM_PASSWORD='wrong-password-2026' node tools/room-encrypt.mjs > /dev/null 2>&1; then
  echo 'FAIL: re-encryption accepted a wrong password' >&2; exit 1
fi
# Rotation must invalidate the old password, but keep content recoverable.
ROOM_PASSWORD='rotated-long-passphrase-2026' node tools/room-encrypt.mjs --rotate > /dev/null
if ROOM_PASSWORD='correct-horse-battery-staple-2026' node tools/room-encrypt.mjs > /dev/null 2>&1; then
  echo 'FAIL: old password accepted after rotation' >&2; exit 1
fi
export ROOM_PASSWORD='rotated-long-passphrase-2026'
node tools/room-encrypt.mjs > /dev/null
rm .private/lyrics/dummy.json
node tools/room-encrypt.mjs > /dev/null
node - <<'JS'
const fs = require('fs');
const f = fs.readdirSync('assets/room');
if (f.length !== 2 || !f.includes('manifest.json') || !f.includes('index.enc.json')) {
  throw new Error('deleting the last song left encrypted artifacts');
}
JS
# The hook must preserve a pre-existing hook and reject force-added plaintext.
unset ROOM_PASSWORD
git init -q
git config user.email test@example.com
git config user.name 'Room Test'
mkdir -p .git/hooks
printf '#!/bin/sh\nprintf "existing-hook-ran\\n" >> existing-hook.log\n' > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
sh tools/install-hooks.sh > /dev/null
sh tools/install-hooks.sh > /dev/null
git add tools assets/room
git commit -qm 'test: valid ciphertext passes both hooks'
test -f existing-hook.log || { echo 'FAIL: existing hook not executed' >&2; exit 1; }
echo '{"lines":"never stage plaintext"}' > .private/lyrics/bad.json
git add -f .private/lyrics/bad.json
if git commit -qm 'test: bad plaintext' >/dev/null 2>&1; then
  echo 'FAIL: plaintext commit was accepted' >&2; exit 1
fi
git restore --staged .private/lyrics/bad.json
# Git hooks can be bypassed via --no-verify; CI must still detect it.
git add -f .private/lyrics/bad.json
git -c core.hooksPath=/dev/null commit -qm 'simulate: bypassed local hook'
if bash tools/check-room-files.sh --tracked >/dev/null 2>&1; then
  echo 'FAIL: CI tracked-file guard accepted a bypassed plaintext commit' >&2; exit 1
fi
git reset --hard -q HEAD~1
printf '{"iv":"AA==","ct":"AA==","lines":"plaintext"}\n' > assets/room/bad.enc.json
git add assets/room/bad.enc.json
if git commit -qm 'test: invalid envelope' >/dev/null 2>&1; then
  echo 'FAIL: invalid encrypted envelope was accepted' >&2; exit 1
fi
git restore --staged assets/room/bad.enc.json
bash tools/check-room-files.sh --tracked > /dev/null
echo 'PASS: WebCrypto compatibility, HMAC names, wrong password, rotation, last-song deletion, preserved hook, plaintext rejection, envelope rejection, tracked-file guard including bypass'
