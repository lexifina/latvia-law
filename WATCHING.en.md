<!-- lawwatch: written from data/checks by the check trail; edit the records, not this page -->

# Watching the sources: what is watched for Latvia

[Latviešu valoda](WATCHING.md)

How global-law watches every country's sources: [global-law WATCHING.md](https://github.com/lexifina/global-law/blob/main/WATCHING.md). This page is the same for Latvia only: every official source this repository takes text from, what is read on it, how often and when it was last read. Every read and what came of it: [monitoring/](monitoring/README.en.md).

| Source | What is read | Folders | How often | Last read | State |
| --- | --- | --- | --- | --- | --- |
| [likumi.lv (Latvijas Vēstnesis): consolidated laws](https://likumi.lv/ta/veids/saeima/likumi) | the list of every law in force or not yet in force (the list behind likumi.lv's page of laws, 50 a request), and the newest part of the same list with amending laws, by in-force day (180 days back and every one in force later); the own page of each new or changed law (the version in force today), and of a seventh of the laws held here each day (verify); the official publication of each amending law on www.vestnesis.lv (its title and days; the audit) | `likumi/`, `satversme/` | daily | 2026-11-26 05:02 UTC | watched: likumi.lv has no open data, API or ELI list, and robots.txt closes its RSS feeds; lists only, no texts. This repository read the texts on likumi.lv (earlier through Internet Archive captures, see REPRODUCE.md) |
| [data.gov.lv: the Saeima's sittings (votes, agendas, debates)](https://data.gov.lv/dati/lv/dataset/saeimas-sedes) | the list of the dataset's files (the portal's CKAN API, one request): each sitting's votes, agenda and debates, with size, hash and the day each last changed; the three files of each sitting with a new file, and up to 400 held files a check, each read once to confirm the bytes its records came from | `saeima/` | daily | 2026-11-26 05:10 UTC | watched: parliamentary records, not law text; CC0 |
| [EU Publications Office (Latvia's measures transposing EU directives)](https://publications.europa.eu/webapi/rdf/sparql) | every national implementing measure Latvia notified, with its notification day and the day the record last changed (one SPARQL query) | `eu-nim/` | daily | 2026-11-26 05:19 UTC | watched: records of the measures only; their texts are on likumi.lv |
| [Latvijas Vēstnesis, the official gazette (normative acts 1993-1998)](https://www.vestnesis.lv) | — | `vestnesis/` | — | — | closed source: the normative acts published 1993-1998, a finished set: past issues do not change; new laws' publication is followed through likumi.lv (same publisher) |

Sources are read within their robots.txt and terms, with pauses between requests.
