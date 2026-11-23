<!-- lawwatch: written from data/checks by the check trail; edit the records, not this page -->

# Uzraudzība: kas tiek lasīts un kas no tā izriet

[English](README.en.md)

Kā global-law uzrauga visas valstis: [global-law monitoring/](https://github.com/lexifina/global-law/tree/main/monitoring). Šī lapa ir tas pats tikai par valsti Latvija: katra reize, kad tiek lasīts oficiāls avots, kad tas notika un kas no tā izrietēja (pievienoti, grozīti un atcelti akti). Mašīnlasāmā forma ir [data/checks/](../data/checks/) (JSON Lines, shēma `lexifina-check/1`), `git log` kā `Kind: check` commit un pa mēnešiem mapē [checks/](checks/).

**Pēdējā pārbaude:** 2026-11-23 21:40 UTC, ES Publikāciju birojs (Latvijas pasākumi ES direktīvu pārņemšanai): nolasītas 1 adreses; pievienoti 0, grozīti 0, atcelti 0; bez izmaiņām; nepublicēti 6, no tiem bez iemesla 0.

## Avoti

| Avots | Mapes | Cik bieži | Pēdējā sekmīgā pārbaude | Pēdējais rezultāts | Stāvoklis |
| --- | --- | --- | --- | --- | --- |
| [likumi.lv ("Latvijas Vēstnesis"): konsolidētie likumi](https://likumi.lv/ta/veids/saeima/likumi) | `likumi/`, `satversme/` | katru dienu | 2026-11-23 21:29 UTC | atrastas izmaiņas | vērots: likumi.lv nav atvērto datu, API vai ELI saraksta, un robots.txt slēdz tā RSS plūsmas; tikai saraksti, ne teksti. Šis repozitorijs tekstus lasīja likumi.lv (agrāk ar Internet Archive kopijām, sk. REPRODUCE.md) |
| [data.gov.lv: Saeimas sēdes (balsojumi, darba kārtības, debates)](https://data.gov.lv/dati/lv/dataset/saeimas-sedes) | `saeima/` | katru dienu | 2026-11-23 21:39 UTC | atrastas izmaiņas | vērots: parlamenta ieraksti, nevis tiesību aktu teksts; CC0 |
| [ES Publikāciju birojs (Latvijas pasākumi ES direktīvu pārņemšanai)](https://publications.europa.eu/webapi/rdf/sparql) | `eu-nim/` | katru dienu | 2026-11-23 21:40 UTC | bez izmaiņām | vērots: tikai pasākumu ieraksti; to teksti ir likumi.lv |
| ["Latvijas Vēstnesis", oficiālais izdevums (normatīvie akti 1993-1998)](https://www.vestnesis.lv) | `vestnesis/` | — | — | — | slēgts avots: 1993.-1998. gadā publicētie normatīvie akti, noslēgts kopums: pagātnes laidieni nemainās; jaunu likumu publikāciju seko caur likumi.lv (tas pats izdevējs) |

## Pēdējās 30 dienas

| Sākums (UTC) | Avots | Nolasīts | Pievienoti | Grozīti | Atcelti | Nepublicēti (bez iemesla) | Rezultāts | Commit |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- | ---: |
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
