<!-- lawwatch: written from data/checks by the check trail; edit the records, not this page -->

# Monitoring: what is read and what came of it

[Latviešu valoda](README.md)

How global-law monitors every country: [global-law monitoring/](https://github.com/lexifina/global-law/tree/main/monitoring). This page is the same for Latvia only: every time an official source is read, when, and what came of it (acts added, changed and removed). The machine-readable form is [data/checks/](../data/checks/) (JSON Lines, schema `lexifina-check/1`), in `git log` as `Kind: check` commits, and month by month in [checks/](checks/).

**Last check:** 2026-11-24 05:26 UTC, EU Publications Office (Latvia's measures transposing EU directives): 1 addresses read; 0 added, 0 changed, 0 removed; no change; 6 not published, 0 of them with no reason.

## Sources

| Source | Folders | How often | Last successful check | Last result | State |
| --- | --- | --- | --- | --- | --- |
| [likumi.lv (Latvijas Vēstnesis): consolidated laws](https://likumi.lv/ta/veids/saeima/likumi) | `likumi/`, `satversme/` | daily | 2026-11-24 05:16 UTC | no change | watched: likumi.lv has no open data, API or ELI list, and robots.txt closes its RSS feeds; lists only, no texts. This repository read the texts on likumi.lv (earlier through Internet Archive captures, see REPRODUCE.md) |
| [data.gov.lv: the Saeima's sittings (votes, agendas, debates)](https://data.gov.lv/dati/lv/dataset/saeimas-sedes) | `saeima/` | daily | 2026-11-24 05:26 UTC | no change | watched: parliamentary records, not law text; CC0 |
| [EU Publications Office (Latvia's measures transposing EU directives)](https://publications.europa.eu/webapi/rdf/sparql) | `eu-nim/` | daily | 2026-11-24 05:26 UTC | no change | watched: records of the measures only; their texts are on likumi.lv |
| [Latvijas Vēstnesis, the official gazette (normative acts 1993-1998)](https://www.vestnesis.lv) | `vestnesis/` | — | — | — | closed source: the normative acts published 1993-1998, a finished set: past issues do not change; new laws' publication is followed through likumi.lv (same publisher) |

## The last 30 days

| Started (UTC) | Source | Read | Added | Changed | Removed | Not published (no reason) | Result | Commits |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- | ---: |
| [2026-11-24 05:26](checks/2026-11.md#lv-eu-nim-20261124t052611z) | eu-nim | 1 | 0 | 0 | 0 | 6 (0) | no change | — |
| [2026-11-24 05:16](checks/2026-11.md#lv-saeima-data-20261124t051657z) | saeima-data | 401 | 0 | 0 | 0 | 0 (0) | no change | — |
| [2026-11-24 05:09](checks/2026-11.md#lv-likumi-20261124t050902z) | likumi | 298 | 0 | 0 | 0 | 6 (0) | no change `verify-differ` | — |
| [2026-11-23 22:08](checks/2026-11.md#lv-eu-nim-20261123t220831z) | eu-nim | 1 | 0 | 0 | 0 | 6 (0) | no change | — |
| [2026-11-23 21:58](checks/2026-11.md#lv-saeima-data-20261123t215847z) | saeima-data | 401 | 0 | 0 | 0 | 0 (0) | no change | — |
| [2026-11-23 21:50](checks/2026-11.md#lv-likumi-20261123t215024z) | likumi | 301 | 0 | 0 | 0 | 6 (0) | changes found | [2](https://github.com/lexifina/latvia-law/compare/f3e81c440e51...330b9abcaf93) |
| [2026-11-23 21:39](checks/2026-11.md#lv-eu-nim-20261123t213957z) | eu-nim | 1 | 0 | 0 | 0 | 6 (0) | no change | — |
| [2026-11-23 21:29](checks/2026-11.md#lv-saeima-data-20261123t212935z) | saeima-data | 413 | 0 | 0 | 0 | 0 (0) | changes found | [50](https://github.com/lexifina/latvia-law/compare/e280d36a9c3a...ff951f3370a1) |
| [2026-11-23 21:20](checks/2026-11.md#lv-likumi-20261123t212058z) | likumi | 301 | 0 | 0 | 0 | 6 (0) | changes found `verify-differ` | [9](https://github.com/lexifina/latvia-law/compare/df1688f89268...e280d36a9c3a) |
| [2026-11-23 01:49](checks/2026-11.md#lv-eu-nim-20261123t014940z) | eu-nim | 1 | 0 | 0 | 0 | 6 (1) | changes found, flagged `unexplained-gap` | — |
| [2026-11-23 01:46](checks/2026-11.md#lv-saeima-data-20261123t014627z) | saeima-data | 157 | 0 | 0 | 0 | 8 (0) | no change | — |
| [2026-11-23 01:45](checks/2026-11.md#lv-likumi-20261123t014516z) | likumi | 42 | 0 | 0 | 0 | 14 (0) | no change | — |

## Check it yourself

```
python tools/checktrail.py                      # the latest check of every source
python tools/checktrail.py --day 2026-11-23     # every check of a day
python tools/checktrail.py --act <id>           # when an act was seen and published
git log --grep='^Kind: check' --format='%ci %s'  # the checks in the history
```

Only the official publication has legal force; the texts here are copies for reading and searching.
