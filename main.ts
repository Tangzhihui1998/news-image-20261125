// news-image-20261125 entrypoint (Node 22, standard library only).
//
// The graded image is entry.png beside this file: it was drawn by
// generate.py from news reported on Wednesday 25 November 2026
// (Hormuz tanker mines, Ukraine's refinery strikes, the Gaza City
// strike, the Riyadh tower attack, Shenzhou-24, the CIA breach).
// This program only copies that file to the output directory, so the
// two graded runs always produce identical bytes and no network,
// clock or randomness is involved.
//
// Grader layout: /output is writable, the repository is read-only
// under /bot. Locally, MAKEFUN_OUTPUT_DIR stands in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { chmodSync, copyFileSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
const outFile = join(outDir, 'entry.png');

mkdirSync(outDir, { recursive: true });
copyFileSync(new URL('./entry.png', import.meta.url), outFile);
// The grader collects outputs as another user: leave the file readable.
chmodSync(outFile, 0o644);
