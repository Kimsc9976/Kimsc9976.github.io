#!/usr/bin/env bash
# Guard both staged changes (pre-commit) and all tracked files (CI).
# In addition to file extensions, validate the entire JSON envelope: the
# encrypted files must contain ONLY iv/ct and the manifest ONLY KDF metadata.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
mode="${1:-}"
case "$mode" in
  --tracked) cmd=(git ls-files -z) ;;
  "")        cmd=(git diff --cached --name-only --diff-filter=ACMR -z) ;;
  *) echo "Usage: $0 [--tracked]" >&2; exit 2 ;;
esac
bad=0
while IFS= read -r -d '' file; do
  case "$file" in
    .private/*)
      printf 'ERROR: private plaintext cannot be committed: %s\n' "$file" >&2
      bad=1 ;;
    assets/room/*)
      case "$file" in
        assets/room/manifest.json|assets/room/*.enc.json)
          if [[ "$mode" == "--tracked" ]]; then ref="HEAD:$file"; else ref=":$file"; fi
          if ! git show "$ref" | node -e '
let s="";
process.stdin.setEncoding("utf8");
process.stdin.on("data", d => s += d);
process.stdin.on("end", () => {
  try {
    const o = JSON.parse(s);
    const b64 = x => typeof x === "string" && /^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$/.test(x);
    const k = Object.keys(o).sort().join(",");
    if (process.argv[1] === "manifest.json") {
      if (k !== "iter,kdf,salt,v" || o.v !== 1 || o.kdf !== "PBKDF2-SHA256" || !Number.isInteger(o.iter) || o.iter < 600000 || !b64(o.salt) || Buffer.from(o.salt,"base64").length < 16) throw Error("invalid manifest schema");
    } else {
      if (k !== "ct,iv" || !b64(o.ct) || !b64(o.iv) || Buffer.from(o.iv,"base64").length !== 12 || Buffer.from(o.ct,"base64").length < 16) throw Error("encrypted file must contain only valid iv/ct");
    }
  } catch (e) { console.error("invalid encrypted JSON or manifest: " + e.message); process.exitCode=1; }
});
' "${file##*/}"; then
            printf 'ERROR: invalid assets/room artifact: %s\n' "$file" >&2
            bad=1
          fi ;;
        *)
          printf 'ERROR: unencrypted/unexpected room artifact: %s\n' "$file" >&2
          bad=1 ;;
      esac ;;
  esac
done < <("${cmd[@]}")
if [[ "$bad" -ne 0 ]]; then
  echo 'Run: git restore --staged <path>, or regenerate via node tools/room-encrypt.mjs' >&2
  exit 1
fi
echo '[room-guard] OK'
