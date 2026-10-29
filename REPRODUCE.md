# How this repository was made (Latvia)

This file is written by the build on 2026-10-29, the day the source data was retrieved. Everything below is enough to rebuild this repository hash for hash.

## Sources

| Source | Address | Retrieved | Requests | Licence |
| --- | --- | --- | ---: | --- |
| likumi.lv (VSIA "Latvijas Vēstnesis") | <https://likumi.lv> | 2026-10-29 | 0 | no copyright in legislation (Autortiesību likums art. 6); re-use terms of the official publisher apply (vestnesis.lv/atkalizmantosana) |
| Internet Archive Wayback Machine (id_ raw captures) | <https://web.archive.org/> | 2026-10-29 | 182 | Internet Archive terms of use |
| Latvijas Vēstnesis, official gazette (www.vestnesis.lv) | <https://www.vestnesis.lv> | 2026-10-29 | 120 | official publication; re-use to be agreed in writing with the publisher (MK noteikumi Nr. 536) |
| data.gov.lv (Latvian open data portal) | <https://data.gov.lv> | 2026-10-29 | 2 | n/a |

Every response is cached by the sha256 of its URL, and the table above lists every source with its retrieval date. Lexifina keeps its fetch scripts privately; `tools/parse.py` reads only the cache and writes `corpus.json`, so the same cache always gives the same corpus.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `satversme` | Latvijas Republikas Satversme | 17 | 1922-11-07 to 2019-01-01 |
| `kriminallikums` | Krimināllikums | 83 | 1999-04-01 to 2026-10-15 |
| `fizisko-personu-datu-apstrades-likums` | Fizisko personu datu apstrādes likums | 3 | 2018-07-05 to 2021-06-04 |

The build made 122 commits:

| Commits | Kind |
| ---: | --- |
| 3 | first version of an act |
| 115 | one law on its in-force day |
| 4 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `nakotne`: laws not yet in force on 2026-10-29.
- 3 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 105 laws in the record.
- 207 tags.

## Dates

Each commit is dated at noon (Europe/Riga) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: Satversme art. 69: a law takes effect fourteen days after its promulgation unless the law sets another term ("Likums stājas spēkā četrpadsmit dienas pēc izsludināšanas, ja likumā nav noteikts cits termiņš"). Each in-force day here is the one likumi.lv records for the version or provision, which applies that rule or the law's own clause. https://likumi.lv/ta/id/57980-latvijas-republikas-satversme

## Commands, in order

```sh
# fill the cache from the sources listed above (network; Lexifina's fetch scripts are kept privately)
python -X utf8 tools/parse.py                  # cache -> corpus.json (no network)
python -X utf8 tools/build.py <folder> --repo <empty folder> --docs-date 2026-10-29
python -X utf8 tools/check_repo.py <repo> --corpus <folder>/corpus.json --write
python -X utf8 tools/build.py <folder> --repo <another empty folder> --docs-date 2026-10-29 --compare <repo>
```

In the main Lexifina repository these files live as follows:
- `fetch.py`, `parse.py` and `repo/`: in `scripts/latvia-law/`.
- `build.py`, `check_repo.py` (`check.py` there) and `on.py`: in `scripts/gitlaw_common/`, with the corpus format in `SCHEMA.md`.

## Exact inputs

- `corpus.json` sha256 `7490457da363eccea86043e2a9689483a61ac3d41b6304ebf15ba0d70db2abc5` (3401116 bytes)
- Script blob hashes (`git hash-object`):

| Script | Blob |
| --- | --- |
| build.py | `2bfc4ac9df193a7be844556d7f69cdb9d93ec3f2` |
| check.py | `cd346c7ff9996d450240e3bab52bcae03b2bc865` |
| on.py | `644a6c0857fbcc72562032b58d57aa113fee0641` |
| fetch.py | `91770a043ec7fdf3f44a9464761df1cf54059c55` |
| parse.py | `54e1e7a14664aadd3a5ad61f3db2493a3dbc28e6` |

- Tools:
  - Python 3.14.0
  - git version 2.52.0.windows.1
  - curl 8.21.0 (Windows) libcurl/8.21.0 Schannel zlib/1.3.2 WinIDN WinLDAP

## Checks

Not yet run for this build.

A second build from the same corpus into an empty folder gave identical hashes for all 122 history commits and 207 tags (history tip `d6cac5ec6010ffd20fd63d3e98039c06714c15a4`).

These results are from the check run on the build before this one, from the same corpus.

## Decisions made by hand

- Built in Latvian, the official language; the README is in English first.
- Text comes from likumi.lv, the consolidated-legislation site of VSIA "Latvijas Vēstnesis" (the official publisher). likumi.lv states that its consolidated texts are informative; the official publication is the gazette "Latvijas Vēstnesis" (vestnesis.lv), from which each amending law's title and publication are taken.
- likumi.lv does not answer from this machine (HTTPS times out), so every version page is an Internet Archive `id_` capture, pinned by timestamp in source_url; the page's own version selector must name the version.
- In-force days are the ones likumi.lv gives for each version ("redakcija") and in each note ("kas stājas spēkā"); a version is never dated by publication.
- Notes in the consolidated text ("... likuma redakcijā, kas stājas spēkā ...", "Ar grozījumiem, kas izdarīti ar ...") are left out of the files and used only for credits.
- An article shown as "(Izslēgts ar ... likumu ...)" is removed from the tree on that day, credited to the law named; its number is not kept as a placeholder file.
- Typesetting is normalised once: no-break spaces become spaces, curly double quotes become ", en and em dashes become -; guillemets (« ») are kept as printed; superscript numbers (70.<sup>11</sup>) become Unicode superscript digits (70.¹¹).
- Captures from different years break the same paragraphs differently; a unit whose text differs from the next version only in spacing or line breaks takes the next version's layout, so spacing alone is never a change.
- likumi.lv editorial blocks are left out: "PIEZĪMES" (TV430, quoting amending laws' own transitional clauses), placeholders for provisions not yet in force ("(Punkts stājas spēkā ... un iekļauts likuma redakcijā uz ...)"), and the second copy of the transitional provisions that pages captured before about 2016 repeat.
- A note that lists several amending laws but dates only the last ("ar A., B. un C. likumu, kas stājas spēkā D") dates only C; A and B are credited on a day only when another note of the act gives that day for them. Notes that name a law by its date without a link are resolved to the one law of that date linked elsewhere in the act.
- legalize-dev/legalize-lv was checked (data "brīvi pieejams"): for these acts it holds no real history (one commit of today's text for the Criminal Law and the data law; 2026 snapshots for the Satversme), so no text was taken from it.
- Satversme: 18. pants is shown in the 2002-05-24 version of likumi.lv with a note putting it in force on 2002-11-05; it keeps its earlier text until then and changes on 2002-11-05.
- KL: no capture of the likumi.lv base version (1999-04-01) is archived; the first version is the act as published in the official gazette (https://www.vestnesis.lv/ta/id/88966), which in force from 1999-04-01 is the act as enacted.
- KL: likumi.lv lists a version from 2014-04-09, but no capture of it is archived and no note in the next version names that day, so the record has no commit on it; any change made that day shows on 2014-06-14.
- FPDAL: no capture of the likumi.lv base version (2018-07-05) is archived; the first version is the act as published in the official gazette (https://www.vestnesis.lv/ta/id/300099), which in force from 2018-07-05 is the act as enacted.
- Satversme: the only archived capture of the 1922 base version (2021-11-13) reads "Valsts prezidents" in art. 52, where every later version and the 1993 official republication (Latvijas Vēstnesis Nr. 43, 01.07.1993) read "Valsts Prezidents"; the change shows on 1933-04-14 as an unexplained publisher change.
- Satversme: the 1922 text is kept as likumi.lv gives it from 7 November 1922. Its operation was interrupted from 1934 and under occupation (1940-1990) and restored in full on 6 July 1993 (Likums par Latvijas Republikas Satversmes spēkā stāšanos un ievešanu); these events changed no words and are described in the README, not committed.
- Satversme: the 1933 amending law (21.03.1933., arts. 74 and 79) predates vestnesis.lv; its title is the one likumi.lv gives and its publication day is left empty.

## What AI did and did not do

The fetch, parse and check scripts were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above, through code that anyone can rerun.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- Claude Code with Claude Opus 5.5 (claude-opus-5-5) chose the sources and wrote fetch.py, likumi.py and parse.py; it did not write, edit or summarise any legal text. parse.py is deterministic and runs no model; every line of law comes from an archived likumi.lv page in the cache.
