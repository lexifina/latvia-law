# How this repository was made (Latvia)

This file is written by the build on 2026-10-29, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| likumi.lv (VSIA "Latvijas Vēstnesis") | <https://likumi.lv> | 2026-10-29 | no copyright in legislation (Autortiesību likums art. 6); re-use terms of the official publisher apply (vestnesis.lv/atkalizmantosana) |
| Internet Archive Wayback Machine | <https://web.archive.org/> | 2026-10-29 | Internet Archive terms of use |
| Latvijas Vēstnesis, official gazette (www.vestnesis.lv) | <https://www.vestnesis.lv> | 2026-10-29 | official publication; re-use to be agreed in writing with the publisher (MK noteikumi Nr. 536) |
| data.gov.lv (Latvian open data portal) | <https://data.gov.lv> | 2026-10-29 | n/a |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `satversme` | Latvijas Republikas Satversme | 17 | 1922-11-07 to 2019-01-01 |
| `kriminallikums` | Krimināllikums | 83 | 1999-04-01 to 2026-10-15 |
| `fizisko-personu-datu-apstrades-likums` | Fizisko personu datu apstrādes likums | 3 | 2018-07-05 to 2021-06-04 |
| `darba-likums` | Darba likums | 29 | 2002-06-01 to 2024-10-22 |

The build made 152 commits:

| Commits | Kind |
| ---: | --- |
| 4 | first version of an act |
| 142 | one law on its in-force day |
| 6 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `nakotne`: laws not yet in force on 2026-10-29.
- 3 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 130 laws in the record.
- 260 tags.

## Dates

Each commit is dated at noon (Europe/Riga) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: Satversme art. 69: a law takes effect fourteen days after its promulgation unless the law sets another term ("Likums stājas spēkā četrpadsmit dienas pēc izsludināšanas, ja likumā nav noteikts cits termiņš"). Each in-force day here is the one likumi.lv records for the version or provision, which applies that rule or the law's own clause. https://likumi.lv/ta/id/57980-latvijas-republikas-satversme

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `134924cb3c92e32f25548a47e505ad13e86ae0f5492102d6e5335656be1ee9b7` (4035862 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `a4faa25af85facb64b956b372f6b528aafdd7ec1`, `check.py` `3d00541d258745461ab52b1b0cb4e1716a27a95d`, `on.py` `644a6c0857fbcc72562032b58d57aa113fee0641`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

132 versions of 4 acts read back from git on the day each took effect and on the day before: 0 mismatches. Trailers: 0 commits whose trailers git cannot parse. Health: 0 merge commits on main, 0 commit dates that go backwards, 0 commits dated after the build.

A second build from the same corpus into an empty folder gave identical hashes for all 152 history commits and 260 tags (history tip `8526d35773f8a14854e91b9eba7501503293ba0e`).

## Decisions made by hand

- Built in Latvian, the official language; the README is in English first.
- Text comes from likumi.lv, the consolidated-legislation site of VSIA "Latvijas Vēstnesis" (the official publisher). likumi.lv states that its consolidated texts are informative; the official publication is the gazette "Latvijas Vēstnesis" (vestnesis.lv), from which each amending law's title and publication are taken.
- Every version page is an Internet Archive capture of likumi.lv, pinned by timestamp in source_url; the page's own version selector must name the version.
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
- DL: no capture of the likumi.lv base version (2002-06-01) is archived; the first version is the act as published in the official gazette (https://www.vestnesis.lv/ta/id/26019), which in force from 2002-06-01 is the act as enacted.
- DL: the only archived page of the 2020-01-01 version was captured on 2019-09-22, before the version before it took effect, so it may predate later amendments; it is not used and the version counts as not archived.
- DL: likumi.lv lists a version from 2005-04-08, but no capture of it is archived and no note in the next version names that day, so the record has no commit on it; any change made that day shows on 2005-11-16.
- DL: likumi.lv lists a version from 2011-05-04, but no capture of it is archived and no note in the next version names that day, so the record has no commit on it; any change made that day shows on 2011-07-20.
- DL: likumi.lv lists a version from 2022-06-01, but no capture of it is archived and no note in the next version names that day, so the record has no commit on it; any change made that day shows on 2022-08-01.
- DL: the 2012-07-25 capture shows 46. pants differently from the versions before and after it, with no note for that day; it is read as a slip of that capture and keeps their text.
- DL: the 2012-07-25 capture shows 76. pants differently from the versions before and after it, with no note for that day; it is read as a slip of that capture and keeps their text.
- DL: the 2012-07-25 capture shows 155. pants differently from the versions before and after it, with no note for that day; it is read as a slip of that capture and keeps their text.
- DL: 36. nodaļa is shown on likumi.lv from 2019-11-19 with no note, and a later page puts the same words in force on 2020-07-01; it is absent until then.
- DL: 158. pants is shown on likumi.lv from 2019-11-19 with no note, and a later page puts the same words in force on 2020-07-01; it is absent until then.
- DL: 159. pants is shown on likumi.lv from 2019-11-19 with no note, and a later page puts the same words in force on 2020-07-01; it is absent until then.
- DL: 160. pants is shown on likumi.lv from 2019-11-19 with no note, and a later page puts the same words in force on 2020-07-01; it is absent until then.
- DL: 161. pants is shown on likumi.lv from 2019-11-19 with no note, and a later page puts the same words in force on 2020-07-01; it is absent until then.
- DL: 162. pants is shown on likumi.lv from 2019-11-19 with no note, and a later page puts the same words in force on 2020-07-01; it is absent until then.
- DL: 163. pants is shown on likumi.lv from 2019-11-19 with no note, and a later page puts the same words in force on 2020-07-01; it is absent until then.
- DL: E DAĻA is shown on likumi.lv from 2019-11-19 with no note, and a later page puts the same words in force on 2020-07-01; it is absent until then.
- DL: the 2002-06-01 text is the gazette publication (vestnesis.lv/ta/id/26019, Latvijas Vēstnesis Nr. 105, 06.07.2001). Its web copy differs from the oldest archived likumi.lv version (2003-01-01) in six articles only by spelling and typesetting (94: "pa-skaidrojumus"; 98: "piedāvātājiem"; 115 and 138: "jaunaka(s)"; 134: "pa-stāv", "pār stāvji"; 146: a missing full stop), with no note for that day; these show on 2003-01-01 as unexplained publisher changes.
- DL: the EU directives reference block ("Informatīva atsauce uz Eiropas Savienības direktīvām") is editorial; its change on 2012-03-08 has no note and is an unexplained publisher change.
- DL: law links on captures from about 2025 have the form /doc.php?id=<id> (the same id as /ta/id/<id>); they are read as law links for this act, so the law of 01.11.2018 (id 303008) is credited.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- Claude Code with Claude Opus 5.5 (claude-opus-5-5) chose the sources and wrote Lexifina's code; it did not write, edit or summarise any legal text. The code is deterministic and runs no model; every line of law comes from an archived likumi.lv page.
