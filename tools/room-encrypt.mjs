#!/usr/bin/env node
// ─────────────────────────────────────────────────────────────
// 비밀방(/room/) 가사 암호화 스크립트
//
//   평문:   .private/lyrics/*.json      ← git에 절대 안 올라감 (.gitignore)
//   암호문: assets/room/*.enc.json      ← 이것만 커밋/배포
//
// 사용법
//   node tools/room-encrypt.mjs             # 비밀번호 입력 프롬프트
//   ROOM_PASSWORD=... node tools/room-encrypt.mjs
//   node tools/room-encrypt.mjs --rotate    # 비밀번호 변경 (salt 재생성, 전부 재암호화)
//
// 암호 방식: PBKDF2-SHA256(600,000회) → AES-256-GCM. 파일 이름은 HMAC으로 만들어
// 곡 이름이 파일명에서 드러나지 않습니다. 외부 패키지 없이 Node 18+ 내장 기능만 사용.
// ─────────────────────────────────────────────────────────────
import { readFile, writeFile, readdir, mkdir, unlink } from "node:fs/promises";
import { existsSync } from "node:fs";
import { createHmac, randomBytes, webcrypto } from "node:crypto";
import { join, dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import readline from "node:readline";

const subtle = webcrypto.subtle;
const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const SRC = join(ROOT, ".private", "lyrics");
const OUT = join(ROOT, "assets", "room");
const ITER = 600_000;
const AAD = new TextEncoder().encode("room-v1");

const b64 = (u8) => Buffer.from(u8).toString("base64");
const unb64 = (s) => new Uint8Array(Buffer.from(s, "base64"));

function fail(msg) {
  console.error(`\n✖ ${msg}\n`);
  process.exit(1);
}

async function askPassword(prompt) {
  if (process.env.ROOM_PASSWORD) return process.env.ROOM_PASSWORD;
  if (!process.stdin.isTTY) fail("비밀번호가 없습니다. ROOM_PASSWORD 환경변수로 넘겨주세요.");
  return new Promise((res) => {
    const rl = readline.createInterface({ input: process.stdin, output: process.stdout, terminal: true });
    rl._writeToOutput = (s) => { if (s.includes(prompt)) rl.output.write(s); else rl.output.write("*"); };
    rl.question(prompt, (a) => { rl.output.write("\n"); rl.close(); res(a); });
  });
}

async function deriveBits(password, salt, iter) {
  const base = await subtle.importKey("raw", new TextEncoder().encode(password.normalize("NFC")), "PBKDF2", false, ["deriveBits"]);
  const bits = new Uint8Array(await subtle.deriveBits({ name: "PBKDF2", hash: "SHA-256", salt, iterations: iter }, base, 512));
  return { aesRaw: bits.slice(0, 32), nameKey: bits.slice(32, 64) };
}

async function encryptJson(aesKey, obj) {
  const iv = randomBytes(12);
  const ct = new Uint8Array(await subtle.encrypt({ name: "AES-GCM", iv, additionalData: AAD }, aesKey, new TextEncoder().encode(JSON.stringify(obj))));
  return { iv: b64(iv), ct: b64(ct) };
}

async function decryptJson(aesKey, box) {
  const pt = await subtle.decrypt({ name: "AES-GCM", iv: unb64(box.iv), additionalData: AAD }, aesKey, unb64(box.ct));
  return JSON.parse(new TextDecoder().decode(pt));
}

function youtubeId(v) {
  if (!v) return "";
  const s = String(v).trim();
  if (/^[\w-]{11}$/.test(s)) return s;
  const m = s.match(/(?:v=|youtu\.be\/|embed\/|shorts\/|live\/)([\w-]{11})/);
  return m ? m[1] : "";
}

function validate(song, file) {
  const where = `.private/lyrics/${file}`;
  if (!song || typeof song !== "object") fail(`${where}: JSON 객체가 아닙니다.`);
  for (const k of ["id", "title"]) {
    if (typeof song[k] !== "string" || !song[k].trim()) fail(`${where}: "${k}" 는 비어 있지 않은 문자열이어야 합니다.`);
  }
  const yt = youtubeId(song.youtube);
  if (!yt) fail(`${where}: "youtube" 에 YouTube 주소나 영상 ID(11자)를 넣어주세요.`);
  if (!Array.isArray(song.lines) || song.lines.length === 0 || song.lines.length > 10000)
    fail(`${where}: "lines" 는 1~10000줄이어야 합니다.`);
  let prev = -Infinity;
  song.lines.forEach((l, i) => {
    if (!l || typeof l !== "object" || typeof l.t !== "number" || !Number.isFinite(l.t) || l.t < 0)
      fail(`${where}: lines[${i}] 의 시간(t)은 0 이상의 유한한 숫자여야 합니다.`);
    for (const k of ["o", "p", "k"]) {
      if (l[k] !== undefined && typeof l[k] !== "string") fail(`${where}: lines[${i}].${k} 는 문자열이어야 합니다.`);
    }
    if (l.t < prev) fail(`${where}: lines[${i}] 시간이 앞 줄보다 빠릅니다 (${l.t} < ${prev}).`);
    prev = l.t;
  });
  return {
    id: String(song.id),
    title: String(song.title),
    artist: song.artist ? String(song.artist) : "",
    youtube: yt,
    offset: typeof song.offset === "number" && Number.isFinite(song.offset) ? song.offset : 0,
    lines: song.lines.map((l) => ({ t: Math.round(l.t * 1000) / 1000, o: l.o || "", p: l.p || "", k: l.k || "" })),
  };
}

async function main() {
  const rotate = process.argv.includes("--rotate");

  if (!existsSync(SRC)) {
    await mkdir(SRC, { recursive: true });
    fail(`가사 폴더가 없어서 만들었습니다: .private/lyrics/\n  비밀방의 '싱크 편집기'에서 받은 JSON 파일을 여기에 넣고 다시 실행하세요.`);
  }
  const files = (await readdir(SRC)).filter((f) => f.endsWith(".json")).sort();
  // The last song can be deleted too: publish an encrypted empty index and
  // remove stale per-song encrypted files on the next run.
  // A first-time empty vault is still an error to prevent accidental setup.
  if (files.length === 0 && !existsSync(join(OUT, "manifest.json")))
    fail(".private/lyrics/ 에 JSON 파일이 없습니다. 첫 곡을 추가하세요.");

  const songs = [];
  const ids = new Set();
  for (const f of files) {
    let raw;
    try { raw = JSON.parse(await readFile(join(SRC, f), "utf8")); } catch (e) { fail(`.private/lyrics/${f}: JSON 형식 오류 — ${e.message}`); }
    const s = validate(raw, f);
    if (ids.has(s.id)) fail(`id "${s.id}" 가 두 파일에 중복됩니다.`);
    ids.add(s.id);
    songs.push(s);
  }

  await mkdir(OUT, { recursive: true });
  const manifestPath = join(OUT, "manifest.json");
  let manifest = existsSync(manifestPath) ? JSON.parse(await readFile(manifestPath, "utf8")) : null;
  const existingVault = !!manifest;

  const password = await askPassword(manifest && !rotate ? "비밀번호: " : "새 비밀번호: ");
  if (!password || password.length < 8) fail("비밀번호는 8자 이상으로 해주세요. (길수록 안전합니다)");

  if (!manifest || rotate) {
    if (!process.env.ROOM_PASSWORD) {
      const again = await askPassword("한 번 더: ");
      if (again !== password) fail("두 비밀번호가 다릅니다.");
    }
    manifest = { v: 1, kdf: "PBKDF2-SHA256", iter: ITER, salt: b64(randomBytes(16)) };
  }

  const { aesRaw, nameKey } = await deriveBits(password, unb64(manifest.salt), manifest.iter);
  const aesKey = await subtle.importKey("raw", aesRaw, "AES-GCM", false, ["encrypt", "decrypt"]);

  // 기존 비밀번호와 다른 비밀번호로 실수로 덮어쓰지 않도록 확인
  const indexPath = join(OUT, "index.enc.json");
  if (existingVault && !rotate && !existsSync(indexPath))
    fail("기존 manifest는 있지만 index.enc.json이 없습니다. 백업을 복원하거나 --rotate로 전체 재암호화하세요.");
  if (!rotate && existsSync(indexPath)) {
    try { await decryptJson(aesKey, JSON.parse(await readFile(indexPath, "utf8"))); }
    catch { fail("기존 비밀번호와 다릅니다. 비밀번호를 바꾸려면 --rotate 옵션을 붙여 실행하세요."); }
  }

  const fileFor = (id) => createHmac("sha256", nameKey).update(id).digest("hex").slice(0, 24) + ".enc.json";
  const index = { v: 1, updated: new Date().toISOString(), songs: [] };
  const written = new Set(["manifest.json", "index.enc.json"]);

  for (const s of songs) {
    const name = fileFor(s.id);
    await writeFile(join(OUT, name), JSON.stringify(await encryptJson(aesKey, s)) + "\n");
    written.add(name);
    index.songs.push({ id: s.id, file: name, title: s.title, artist: s.artist, n: s.lines.length });
  }
  index.songs.sort((a, b) => a.title.localeCompare(b.title, "ko"));

  await writeFile(indexPath, JSON.stringify(await encryptJson(aesKey, index)) + "\n");
  await writeFile(manifestPath, JSON.stringify(manifest, null, 2) + "\n");

  // 더 이상 없는 곡의 암호문 정리
  let removed = 0;
  for (const f of await readdir(OUT)) {
    if (f.endsWith(".enc.json") && !written.has(f)) { await unlink(join(OUT, f)); removed++; }
  }

  console.log(`\n✔ ${songs.length}곡 암호화 완료 → assets/room/  (정리된 옛 파일 ${removed}개)`);
  for (const s of index.songs) console.log(`   · ${s.title}${s.artist ? " — " + s.artist : ""} (${s.n}줄)`);
  console.log("\n  이제 assets/room/ 만 커밋하면 됩니다. .private/ 는 절대 커밋하지 마세요.\n");
}

main().catch((e) => fail(e.stack || e.message));
