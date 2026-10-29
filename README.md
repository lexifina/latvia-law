# Latvia: law history in git

The law of Latvia as a git history: one file per provision, one commit per law on the day its change took effect, and the law that made each change as the commit's author. `git blame` names the law behind every line; `git log` lists every change to an article; picking a date gives the text in force that day.

It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `lv/`.

**What is in it now**

| Folder | Act | Versions | History |
| --- | --- | ---: | --- |
| `satversme/` | Latvijas Republikas Satversme (the Constitution, 1922) | 17 | As adopted by the Constituent Assembly (in force 7 November 1922), the 1933 amendment, and every amendment from 1994 to the one in force on 1 January 2019, still current |
| `kriminallikums/` | Krimināllikums (the Criminal Law, 1998) | 83 | As enacted (in force 1 April 1999) to the version in force on 15 October 2026, through every consolidated version likumi.lv lists but one |
| `fizisko-personu-datu-apstrades-likums/` | Fizisko personu datu apstrādes likums (the Personal Data Processing Law, 2018) | 3 | As enacted (in force 5 July 2018) to today, through its two amending laws |
| `darba-likums/` | Darba likums (the Labour Law, 2001) | 29 | As enacted (in force 1 June 2002) to the version in force on 22 October 2024, still current, through every consolidated version likumi.lv lists but four |

The text is in Latvian, the official language. The consolidated versions ("redakcijas") come from [likumi.lv](https://likumi.lv), the legislation site of VSIA "Latvijas Vēstnesis", the official publisher of the Republic of Latvia. likumi.lv says its consolidated texts are for information; the official publication is the gazette *Latvijas Vēstnesis* ([vestnesis.lv](https://www.vestnesis.lv)), where each amending law was published. The per-act `README.md` in each folder lists every provision, how often it changed and when.

## A lawyer's questions as git commands

| Question | Command |
| --- | --- |
| What did article 18 of the Satversme say on 1 June 2002? | `python tools/on.py 2002-06-01 satversme pants-018` |
| The same, with raw git (bash) | `git show $(git rev-list -1 --before="2002-06-01T23:59:59Z" main -- satversme/pants-018.md):satversme/pants-018.md` |
| The same, in PowerShell | `$r = git rev-list -1 --before="2002-06-01T23:59:59Z" main -- satversme/pants-018.md; git show "$($r):satversme/pants-018.md"` |
| Which law wrote each paragraph of article 36 of the Criminal Law? | `git blame kriminallikums/pants-036.md` |
| Every change to the preamble of the Satversme, word by word | `git log -p --word-diff satversme/ievads.md` |
| Every law in the record, in order | `git log --reverse --format="%ad %an" --date=short main` |
| Everything one law changed | `git show law/likums-2014-06-19-267428` (tags `law/<key>`; the key is the law's adoption day and its likumi.lv id) |
| The whole act on a date | `python tools/on.py 2015-01-01 kriminallikums` |
| The act on a version's in-force day | `git show satversme/1998-11-06` (tags `<act>/<in-force day>`) |

File names: `pants-018.md` is article 18, `pants-070-11.md` is article 70.¹¹, `nodala-08.md` is the heading of chapter VIII, `ievads.md` the preamble, `parejas-noteikumi-024.md` item 24 of the transitional provisions, and `zz-*.md` the closing lines (adoption, signatures). After a rebuild, refresh tags with `git fetch --force --tags`: a plain fetch keeps stale tags.

## Dates

- Each commit is dated at **noon, Europe/Riga, on the day the change took effect**. The day is in the `In-force:` trailer, which the tools read.
- **The day is the one likumi.lv gives**: each consolidated version starts on its in-force day, and each changed article carries a note such as "(30.04.2002. likuma redakcijā, kas stājas spēkā 05.11.2002.)". A law takes effect fourteen days after promulgation unless it sets another term (Satversme, art. 69); likumi.lv applies that rule or the law's own clause, so none is applied here.
- **A change shown before its day.** likumi.lv's version of 24 May 2002 already shows the new article 18 (the MPs' oath), with a note putting it in force on 5 November 2002. Here article 18 keeps its earlier words until 5 November 2002, and that day is a commit of its own.
- **Before 1970.** Git cannot store dates before 1970, so the commits for 1922 and 1933 are dated 1 January 1970, a second apart; the real day is in the `In-force:` trailer and in the tags.
- `--before="YYYY-MM-DD"` alone uses your clock's time of day, so a change that took effect that day may be missed before noon. Use `T23:59:59Z` as above, or the tool.

## How it is checked

- **Against today's text.** The newest archived likumi.lv page of each act (captured 18 and 19 October and 3 October 2026) shows the version in force. Replaying every version in this record gives that page exactly, provision by provision: 125 files of the Satversme, 534 of the Criminal Law and 58 of the Personal Data Processing Law.
- **Every version is a dated source.** Each version names its source page (an Internet Archive capture of likumi.lv, with the capture time in the address, or the gazette page) and the sha256 of the bytes it was read from, and the page's own version selector must name that version.
- Every version of every act is read back from git on the day it took effect and on the day before (`tools/check_repo.py`); both must match `corpus.json`. Results are in `REPRODUCE.md`.
- Health checks: no merge commits on `main`, commit dates never go backwards, nothing dated in the future, and every commit's trailers parse with `git interpret-trailers --parse`.
- The repository is rebuilt from the same data a second time and must give identical hashes.

## What "author" means

The author of a commit is the law that made the change, with an e-mail address that cannot exist (`likums-2014-06-19-267428@likumi.lv.invalid`), so `git blame` and `git log --author` name it. The committer is always Lexifina.

- **Credits come only from the source.** An article is credited to the law its likumi.lv note names for that day. Where a note lists several laws but dates only the last ("Ar grozījumiem, kas izdarīti ar 12.02.2004., … un 13.12.2012. likumu, kas stājas spēkā 01.04.2013."), an earlier law in the list is credited only on a day another note gives as its in-force day. A chapter replaced as a whole (chapter VIII of the Satversme, 1998) credits its articles through the chapter's note.
- **Unexplained changes** are committed by the publisher, labelled "unexplained", when no note explains them. There are five: article 52 of the Satversme reads "Valsts prezidents" in the only archived capture of the 1922 version and "Valsts Prezidents" in every later one and in the 1993 official republication (shown on 14 April 1933); and in the Criminal Law articles 55 and 58.1 on 1 January 2006 (the probation service), article 225 on 1 January 2015 and article 289 on 1 January 2022, whose notes do not name that day.
- **The first commit of each act** is the act as enacted, credited to it: the Constituent Assembly's Satversme of 15 February 1922, the Criminal Law of 17 June 1998 and the Personal Data Processing Law of 21 June 2018.
- Superscript numbers of inserted articles and paragraphs are kept as Unicode superscript digits, as printed: 70.¹¹, (2²).
- Blame credits whole lines (one paragraph per line). Use `git log -p --word-diff` to see exactly which words each law changed.

## What it does not show

- **The Satversme's interruption.** It is kept as in force from 1922. Its operation was cut short by the coup of 1934 and by the occupation (1940–1990); the Supreme Council restored it in part on 4 May 1990, and in full when the 5th Saeima met on 6 July 1993. These events changed no words, so they are not commits.
- **One Criminal Law version.** likumi.lv lists a version from 9 April 2014, but no capture of it is archived and no note in the next version names that day; any change made that day shows on 14 June 2014.
- **Four Labour Law versions.** likumi.lv lists versions from 8 April 2005, 4 May 2011, 1 January 2020 and 1 June 2022 whose pages are not available (for 1 January 2020, only a copy made before the version before it took effect, which is not used). No note in the next version names those days, so the record has no commit on them; any change made then shows on the next version (for 1 January 2020, one article whose note gives that day). Articles 158–163 (Part E, administrative liability), shown by likumi.lv from 19 November 2019, are committed on 1 July 2020, the day its notes put them in force.
- **The Labour Law as enacted.** Its first version is the act as published in the official gazette (Latvijas Vēstnesis Nr. 105, 6 July 2001). Six articles differ from likumi.lv's oldest available version (1 January 2003) only in spelling and typesetting; they show on that day as changes with no law named.
- **The base versions on likumi.lv.** No capture of likumi.lv's base version of the Criminal Law (1 April 1999) or of the Personal Data Processing Law (5 July 2018) is archived. Their first versions are the acts as published in the official gazette (Latvijas Vēstnesis Nr. 199/200, 8 July 1998, and Nr. 132, 4 July 2018). The gazette page and likumi.lv lay paragraphs out differently; text that differs only in spacing or line breaks takes the later layout and is not a change.
- **likumi.lv's notes and editorial material** are not law text and are not in the files: the amendment notes, the "PIEZĪMES" that quote amending laws' own transitional clauses, and placeholders for provisions not yet in force ("(Punkts stājas spēkā 01.01.2022. un iekļauts likuma redakcijā uz 01.01.2022. …)"). A provision the consolidated text shows only as "(Izslēgts ar … likumu …)" is removed on that day; repealed paragraphs inside an article keep likumi.lv's "(izslēgta ar … likumu)" line.
- **Court rulings.** Judgments of the Satversmes tiesa that void a provision appear only when likumi.lv's consolidated text changes; none is a separate commit in these four acts.

## How it is built

Lexifina reads the sources listed here and records each act's dated versions, and the laws that made each change, in one corpus file. `tools/build.py` writes this repository from that file, and the same corpus always gives the same commit hashes; `REPRODUCE.md` gives the details and the checks. A model (Claude) wrote Lexifina's code; it wrote no legal text, and no model runs when the history is built.

No AI model wrote or changed legal text. Claude Opus 5.5 wrote the scripts and chose the sources; see `REPRODUCE.md`.

## Sources

| Source | Kind | Past versions | Names the amending act | API or bulk | Notes |
| --- | --- | --- | --- | --- | --- |
| [likumi.lv](https://likumi.lv) | Official publisher's consolidated legislation (VSIA "Latvijas Vēstnesis") | yes, every version with its in-force day | yes, a note per article | no | Used, through Internet Archive captures |
| [Latvijas Vēstnesis](https://www.vestnesis.lv) | Official gazette | the act as published | n/a | no | Used: amending laws' publication; base versions of the Criminal Law and the Personal Data Processing Law |
| [Internet Archive](https://web.archive.org/) | Web archive | the captures it holds | n/a | – | Used: every likumi.lv page read is a pinned capture |
| – | Web archive | n/a | n/a | yes | Checked: holds likumi.lv's current pages only |
| [data.gov.lv](https://data.gov.lv) | Open data portal | n/a | n/a | CKAN API | Checked: no legislation dataset |
| [legalize-lv](https://github.com/legalize-dev/legalize-lv) | Volunteer git repo built from likumi.lv | no, for these acts | no | n/a | Checked: one commit (today's text) for the Criminal Law and the data law, 2026 snapshots for the Satversme; no text taken |
| [blame-likumi.lv](https://github.com/viktor-gusev/blame-likumi.lv) | Volunteer git blame for likumi.lv | yes | partly | n/a | Prior art; not read, no text copied |

Research guides that cover every country: [GlobaLex](https://www.nyulawglobal.org/globalex/) and the [Law Library of Congress Guide to Law Online](https://www.loc.gov/research-centers/law-library-of-congress/researcher-resources/guide-to-law-online/).

## Licence

Laws and other normative acts are not protected by copyright in Latvia (Autortiesību likums, art. 6). Source: likumi.lv and the official gazette "Latvijas Vēstnesis", VSIA "Latvijas Vēstnesis". Latvijas Vēstnesis states that re-use of officially published information is to be agreed with the official publisher in writing ([vestnesis.lv/atkalizmantosana](https://www.vestnesis.lv/atkalizmantosana)); no such agreement has been made, and this repository is private. The arrangement, tables, commit messages and tools are by Lexifina, under the terms in `LICENSE`.

This repository is not legal advice and not an official publication.

## Latviski

Latvijas tiesību aktu vēsture git repozitorijā: katrs pants ir atsevišķs fails, katrs grozījumu likums ir atsevišķa revīzija tā spēkā stāšanās dienā, un revīzijas autors ir likums, kas grozījumu izdarīja. Teksts ir no likumi.lv konsolidētajām redakcijām (VSIA "Latvijas Vēstnesis"), kas lasītas no Internet Archive kopijām, un no oficiālā izdevuma "Latvijas Vēstnesis". Konsolidētie teksti ir informatīvi; juridisks spēks ir oficiālajai publikācijai. Šī nav juridiska konsultācija un nav oficiāla publikācija.
