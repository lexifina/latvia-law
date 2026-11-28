<!-- lawwatch: written from data/checks by the check trail; edit the records, not this page -->

# Uzraudzība: kas tiek lasīts un kas no tā izriet

[English](README.en.md)

Kā global-law uzrauga visas valstis: [global-law monitoring/](https://github.com/lexifina/global-law/tree/main/monitoring). Šī lapa ir tas pats tikai par valsti Latvija: katra reize, kad tiek lasīts oficiāls avots, kad tas notika un kas no tā izrietēja (pievienoti, grozīti un atcelti akti). Mašīnlasāmā forma ir [data/checks/](../data/checks/) (JSON Lines, shēma `lexifina-check/1`), `git log` kā `Kind: check` commit un pa mēnešiem mapē [checks/](checks/).

**Pēdējā pārbaude:** 2026-11-28 09:01 UTC, ES Publikāciju birojs (Latvijas pasākumi ES direktīvu pārņemšanai): nolasītas 1 adreses; pievienoti 0, grozīti 1, atcelti 0; atrastas izmaiņas; nepublicēti 6, no tiem bez iemesla 0. Atzīmes: `publish-lag`.

## Avoti

| Avots | Mapes | Cik bieži | Pēdējā sekmīgā pārbaude | Pēdējais rezultāts | Stāvoklis |
| --- | --- | --- | --- | --- | --- |
| [likumi.lv ("Latvijas Vēstnesis"): konsolidētie likumi](https://likumi.lv/ta/veids/saeima/likumi) | `likumi/`, `satversme/` | katru dienu | 2026-11-28 05:09 UTC | atrastas izmaiņas | vērots: likumi.lv nav atvērto datu, API vai ELI saraksta, un robots.txt slēdz tā RSS plūsmas; tikai saraksti, ne teksti. Šis repozitorijs tekstus lasīja likumi.lv (agrāk ar Internet Archive kopijām, sk. REPRODUCE.md) |
| [data.gov.lv: Saeimas sēdes (balsojumi, darba kārtības, debates)](https://data.gov.lv/dati/lv/dataset/saeimas-sedes) | `saeima/` | katru dienu | 2026-11-28 05:09 UTC | bez izmaiņām | vērots: parlamenta ieraksti, nevis tiesību aktu teksts; CC0 |
| [ES Publikāciju birojs (Latvijas pasākumi ES direktīvu pārņemšanai)](https://publications.europa.eu/webapi/rdf/sparql) | `eu-nim/` | katru dienu | 2026-11-28 09:01 UTC | atrastas izmaiņas | vērots: tikai pasākumu ieraksti; to teksti ir likumi.lv |
| ["Latvijas Vēstnesis", oficiālais izdevums (normatīvie akti 1993-1998)](https://www.vestnesis.lv) | `vestnesis/` | — | — | — | slēgts avots: 1993.-1998. gadā publicētie normatīvie akti, noslēgts kopums: pagātnes laidieni nemainās; jaunu likumu publikāciju seko caur likumi.lv (tas pats izdevējs) |

## Pēdējās 30 dienas

| Sākums (UTC) | Avots | Nolasīts | Pievienoti | Grozīti | Atcelti | Nepublicēti (bez iemesla) | Rezultāts | Commit |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- | ---: |
| [2026-11-28 09:01](checks/2026-11.md#lv-eu-nim-20261128t090133z) | eu-nim | 1 | 0 | 1 | 0 | 6 (0) | atrastas izmaiņas `publish-lag` | — |
| [2026-11-28 08:01](checks/2026-11.md#lv-eu-nim-20261128t080133z) | eu-nim | 0 | 0 | 0 | 0 | 0 (0) | pārbaude neizdevās | — |
| [2026-11-28 07:01](checks/2026-11.md#lv-eu-nim-20261128t070133z) | eu-nim | 0 | 0 | 0 | 0 | 0 (0) | pārbaude neizdevās | — |
| [2026-11-28 05:09](checks/2026-11.md#lv-eu-nim-20261128t050955z) | eu-nim | 4 | 0 | 0 | 0 | 0 (0) | avots neatbildēja | — |
| [2026-11-28 05:09](checks/2026-11.md#lv-saeima-data-20261128t050949z) | saeima-data | 1 | 0 | 0 | 0 | 0 (0) | bez izmaiņām | — |
| [2026-11-28 05:01](checks/2026-11.md#lv-likumi-20261128t050135z) | likumi | 302 | 0 | 1 | 0 | 8 (0) | atrastas izmaiņas `verify-differ` | [2](https://github.com/lexifina/latvia-law/compare/9bbb0f3fe3ff...ab2c730080a5) |
| [2026-11-27 05:10](checks/2026-11.md#lv-eu-nim-20261127t051033z) | eu-nim | 1 | 0 | 0 | 0 | 6 (0) | bez izmaiņām `publish-lag` | — |
| [2026-11-27 05:09](checks/2026-11.md#lv-saeima-data-20261127t050942z) | saeima-data | 32 | 0 | 0 | 0 | 0 (0) | bez izmaiņām | — |
| [2026-11-27 05:01](checks/2026-11.md#lv-likumi-20261127t050135z) | likumi | 300 | 0 | 0 | 0 | 8 (0) | bez izmaiņām `verify-differ` | — |
| [2026-11-26 05:19](checks/2026-11.md#lv-eu-nim-20261126t051954z) | eu-nim | 1 | 0 | 0 | 0 | 6 (0) | bez izmaiņām `publish-lag` | — |
| [2026-11-26 05:10](checks/2026-11.md#lv-saeima-data-20261126t051030z) | saeima-data | 401 | 0 | 0 | 0 | 0 (0) | bez izmaiņām | — |
| [2026-11-26 05:02](checks/2026-11.md#lv-likumi-20261126t050206z) | likumi | 301 | 0 | 0 | 0 | 8 (0) | bez izmaiņām | — |
| [2026-11-25 05:19](checks/2026-11.md#lv-eu-nim-20261125t051938z) | eu-nim | 1 | 0 | 0 | 0 | 6 (0) | bez izmaiņām | — |
| [2026-11-25 05:10](checks/2026-11.md#lv-saeima-data-20261125t051041z) | saeima-data | 401 | 0 | 0 | 0 | 0 (0) | bez izmaiņām | — |
| [2026-11-25 05:01](checks/2026-11.md#lv-likumi-20261125t050133z) | likumi | 305 | 0 | 0 | 0 | 7 (0) | atrastas izmaiņas `verify-differ` | [5](https://github.com/lexifina/latvia-law/compare/b6b26a42565e...4fa6247cfaf5) |
| [2026-11-24 05:26](checks/2026-11.md#lv-eu-nim-20261124t052611z) | eu-nim | 1 | 0 | 0 | 0 | 6 (0) | bez izmaiņām | — |
| [2026-11-24 05:16](checks/2026-11.md#lv-saeima-data-20261124t051657z) | saeima-data | 401 | 0 | 0 | 0 | 0 (0) | bez izmaiņām | — |
| [2026-11-24 05:09](checks/2026-11.md#lv-likumi-20261124t050902z) | likumi | 298 | 0 | 0 | 0 | 6 (0) | bez izmaiņām `verify-differ` | — |
| [2026-11-23 22:08](checks/2026-11.md#lv-eu-nim-20261123t220831z) | eu-nim | 1 | 0 | 0 | 0 | 6 (0) | bez izmaiņām | — |
| [2026-11-23 21:58](checks/2026-11.md#lv-saeima-data-20261123t215847z) | saeima-data | 401 | 0 | 0 | 0 | 0 (0) | bez izmaiņām | — |
| [2026-11-23 21:50](checks/2026-11.md#lv-likumi-20261123t215024z) | likumi | 301 | 0 | 0 | 0 | 6 (0) | atrastas izmaiņas | [2](https://github.com/lexifina/latvia-law/compare/f3e81c440e51...330b9abcaf93) |
| [2026-11-23 21:39](checks/2026-11.md#lv-eu-nim-20261123t213957z) | eu-nim | 1 | 0 | 0 | 0 | 6 (0) | bez izmaiņām | — |
| [2026-11-23 21:29](checks/2026-11.md#lv-saeima-data-20261123t212935z) | saeima-data | 413 | 0 | 0 | 0 | 0 (0) | atrastas izmaiņas | [50](https://github.com/lexifina/latvia-law/compare/e280d36a9c3a...ff951f3370a1) |
| [2026-11-23 21:20](checks/2026-11.md#lv-likumi-20261123t212058z) | likumi | 301 | 0 | 0 | 0 | 6 (0) | atrastas izmaiņas `verify-differ` | [9](https://github.com/lexifina/latvia-law/compare/df1688f89268...e280d36a9c3a) |
| [2026-11-23 01:49](checks/2026-11.md#lv-eu-nim-20261123t014940z) | eu-nim | 1 | 0 | 0 | 0 | 6 (1) | atrastas izmaiņas, ar atzīmi `unexplained-gap` | — |
| [2026-11-23 01:46](checks/2026-11.md#lv-saeima-data-20261123t014627z) | saeima-data | 157 | 0 | 0 | 0 | 8 (0) | bez izmaiņām | — |
| [2026-11-23 01:45](checks/2026-11.md#lv-likumi-20261123t014516z) | likumi | 42 | 0 | 0 | 0 | 14 (0) | bez izmaiņām | — |

## Pārbaudiet paši

```
python tools/checktrail.py                      # katra avota pēdējā pārbaude
python tools/checktrail.py --day 2026-11-23     # visas vienas dienas pārbaudes
python tools/checktrail.py --act <id>           # kad akts tika ieraudzīts un publicēts
git log --grep='^Kind: check' --format='%ci %s'  # pārbaudes vēsturē
```

Juridisks spēks ir tikai oficiālajai publikācijai ("Latvijas Vēstnesis"); šeit esošie teksti ir kopijas lasīšanai un meklēšanai.
