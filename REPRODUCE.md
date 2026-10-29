# How this repository was made (Latvia)

This file is written by the build on 2026-10-29, the day the source data was retrieved. Everything below is enough to rebuild this repository hash for hash.

## Sources

| Source | Address | Retrieved | Requests | Licence |
| --- | --- | --- | ---: | --- |
| likumi.lv (VSIA "Latvijas Vēstnesis") | <https://likumi.lv> | 2026-10-29 | 0 | no copyright in legislation (Autortiesību likums art. 6); re-use terms of the official publisher apply (vestnesis.lv/atkalizmantosana) |
| Internet Archive Wayback Machine (id_ raw captures) | <https://web.archive.org/> | 2026-10-29 | 137 | Internet Archive terms of use |
| Latvijas Vēstnesis, official gazette (www.vestnesis.lv) | <https://www.vestnesis.lv> | 2026-10-29 | 15 | official publication; re-use to be agreed in writing with the publisher (MK noteikumi Nr. 536) |
| data.gov.lv (Latvian open data portal) | <https://data.gov.lv> | 2026-10-29 | 2 | n/a |

Every response is cached by the sha256 of its URL, and the table above lists every source with its retrieval date. Lexifina keeps its fetch scripts privately; `tools/parse.py` reads only the cache and writes `corpus.json`, so the same cache always gives the same corpus.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `satversme` | Latvijas Republikas Satversme | 17 | 1922-11-07 to 2019-01-01 |

The build made 18 commits:

| Commits | Kind |
| ---: | --- |
| 1 | first version of an act |
| 16 | one law on its in-force day |
| 1 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `nakotne`: laws not yet in force on 2026-10-29.
- 3 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 16 laws in the record.
- 33 tags.

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

- `corpus.json` sha256 `72123aedac4d8f6b86de62228ad3ea5a67a5940f288fcf53c13a3aaa9a3b5e73` (626030 bytes)
- Script blob hashes (`git hash-object`):

| Script | Blob |
| --- | --- |
| build.py | `2bfc4ac9df193a7be844556d7f69cdb9d93ec3f2` |
| check.py | `cd346c7ff9996d450240e3bab52bcae03b2bc865` |
| on.py | `644a6c0857fbcc72562032b58d57aa113fee0641` |
| fetch.py | `bc48d10e0fd6566b32914600724d398a820e0ee8` |
| parse.py | `299d437f44d47609024cdbb5081b2d96ea534726` |

- Tools:
  - Python 3.14.0
  - git version 2.52.0.windows.1
  - curl 8.21.0 (Windows) libcurl/8.21.0 Schannel zlib/1.3.2 WinIDN WinLDAP

## Checks

Not yet run for this build.

Not yet run for this build.

These results are from the check run on the build before this one, from the same corpus.

## Decisions made by hand

- Built in Latvian, the official language; the README is in English first.
- Text comes from likumi.lv, the consolidated-legislation site of VSIA "Latvijas Vēstnesis" (the official publisher). likumi.lv states that its consolidated texts are informative; the official publication is the gazette "Latvijas Vēstnesis" (vestnesis.lv), from which each amending law's title and publication are taken.
- likumi.lv does not answer from this machine (HTTPS times out), so every version page is an Internet Archive `id_` capture, pinned by timestamp in source_url; the page's own version selector must name the version.
- In-force days are the ones likumi.lv gives for each version ("redakcija") and in each note ("kas stājas spēkā"); a version is never dated by publication.
- Notes in the consolidated text ("... likuma redakcijā, kas stājas spēkā ...", "Ar grozījumiem, kas izdarīti ar ...") are left out of the files and used only for credits.
- An article shown as "(Izslēgts ar ... likumu ...)" is removed from the tree on that day, credited to the law named; its number is not kept as a placeholder file.
- Typesetting is normalised once: no-break spaces become spaces, curly double quotes become ", en and em dashes become -; guillemets (« ») are kept as printed.
- Satversme: 18. pants is shown in the 2002-05-24 version of likumi.lv with a note putting it in force on 2002-11-05; it keeps its earlier text until then and changes on 2002-11-05.

## What AI did and did not do

The fetch, parse and check scripts were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above, through code that anyone can rerun.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- Claude Code with Claude Opus 5.5 (claude-opus-5-5) chose the sources and wrote fetch.py, likumi.py and parse.py; it did not write, edit or summarise any legal text. parse.py is deterministic and runs no model; every line of law comes from an archived likumi.lv page in the cache.
