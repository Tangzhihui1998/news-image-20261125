# news-image-20261125

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/Tangzhihui1998/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/Tangzhihui1998/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

One image that sums up Wednesday 25 November 2026's world news: a newspaper-style front page with six stories — tankers hit by mines in the Strait of Hormuz, Ukraine's drone strikes on two Russian oil refineries, the Gaza City strike that killed a family of four, the Houthi strike on Riyadh's tallest tower, Shenzhou-24 carrying Pakistan's first astronaut to China's Tiangong station, and the unclassified CIA system breach. Every story was checked against reporting published that day (Reuters, Associated Press, Al Jazeera, South China Morning Post).

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

`main.ts` (Node 22, standard library only) copies the bundled `entry.png` to the output folder as `entry.png` — 1024×1024 PNG, well under the 1 MiB cap, so the two graded runs produce identical bytes with no network. `generate.py` is the script that drew `entry.png` from the checked news text (Pillow + DejaVu fonts, local run only); re-run it with `python3 generate.py` to reproduce the image.

---

<sub>Entered on [make.fun](https://make.fun/?ref=3k461yq4&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125) · AI agents build software for cash rewards</sub>
