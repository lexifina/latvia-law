<!-- lawwatch: written from data/checks by the check trail; edit the records, not this page -->

# Avotu vērošana: kas tiek vērots valstī Latvija

[English](WATCHING.en.md)

Kā global-law vēro katras valsts avotus: [global-law WATCHING.md](https://github.com/lexifina/global-law/blob/main/WATCHING.md). Šī lapa ir tas pats tikai par valsti Latvija: katrs oficiālais avots, no kura šis repozitorijs ņem tekstu, kas tajā tiek lasīts, cik bieži un kad tas pēdējo reizi lasīts. Katra nolasīšana un tās rezultāts: [monitoring/](monitoring/README.md).

| Avots | Kas tiek lasīts | Mapes | Cik bieži | Pēdējoreiz lasīts | Stāvoklis |
| --- | --- | --- | --- | --- | --- |
| [likumi.lv ("Latvijas Vēstnesis"): konsolidētie likumi](https://likumi.lv/ta/veids/saeima/likumi) | visu spēkā esošo un vēl spēkā nestājušos likumu saraksts (saraksts, no kura veidota likumi.lv likumu lapa, 50 vienā pieprasījumā), un tā paša saraksta jaunākā daļa ar grozījumu likumiem pēc spēkā stāšanās dienas (180 dienas atpakaļ un visi, kas stāsies spēkā vēlāk); katra jaunā vai grozītā likuma lapa (šodien spēkā esošā redakcija) un katru dienu septītās daļas šeit esošo likumu lapas (pārbaude); katra grozījumu likuma oficiālā publikācija www.vestnesis.lv (nosaukums un datumi; otrā pārbaude) | `likumi/`, `satversme/` | katru dienu | 2026-11-23 21:20 UTC | vērots: likumi.lv nav atvērto datu, API vai ELI saraksta, un robots.txt slēdz tā RSS plūsmas; tikai saraksti, ne teksti. Šis repozitorijs tekstus lasīja likumi.lv (agrāk ar Internet Archive kopijām, sk. REPRODUCE.md) |
| [data.gov.lv: Saeimas sēdes (balsojumi, darba kārtības, debates)](https://data.gov.lv/dati/lv/dataset/saeimas-sedes) | datu kopas failu saraksts (portāla CKAN API, viens pieprasījums): katras sēdes balsojumi, darba kārtība un debates ar izmēru, kontrolsummu un pēdējo izmaiņu dienu; katras sēdes, kurai ir jauns fails, trīs faili un līdz 400 šeit esošiem failiem vienā pārbaudē, katrs vienreiz, lai apstiprinātu saturu, no kura veidoti ieraksti | `saeima/` | katru dienu | 2026-11-23 21:29 UTC | vērots: parlamenta ieraksti, nevis tiesību aktu teksts; CC0 |
| [ES Publikāciju birojs (Latvijas pasākumi ES direktīvu pārņemšanai)](https://publications.europa.eu/webapi/rdf/sparql) | visi Latvijas paziņotie valsts īstenošanas pasākumi ar paziņošanas dienu un ieraksta pēdējo izmaiņu dienu (viens SPARQL vaicājums) | `eu-nim/` | katru dienu | 2026-11-23 21:39 UTC | vērots: tikai pasākumu ieraksti; to teksti ir likumi.lv |
| ["Latvijas Vēstnesis", oficiālais izdevums (normatīvie akti 1993-1998)](https://www.vestnesis.lv) | — | `vestnesis/` | — | — | slēgts avots: 1993.-1998. gadā publicētie normatīvie akti, noslēgts kopums: pagātnes laidieni nemainās; jaunu likumu publikāciju seko caur likumi.lv (tas pats izdevējs) |

Avoti tiek lasīti, ievērojot to robots.txt un lietošanas noteikumus, ar pauzēm starp pieprasījumiem.
