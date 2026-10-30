# How this repository was made (Indonesia)

This file is written by the build on 2026-10-30, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| Buku Saku UUD 1945 dan UU MK (Mahkamah Konstitusi, Pusdik) | <https://pusdik.mkri.id/materi/materi_294_Buku%20Saku%20UUD%201945%20dan%20UU%20MK_2020.pdf> | 2026-10-29 | Official publication of the Constitutional Court; no licence stated. |
| Peraturan BPK (JDIH BPK): UU 1/2023, official salinan scan | <https://peraturan.bpk.go.id/Download/287456> | 2026-10-30 | Statutes carry no copyright in Indonesia: UU 28/2014 (Hak Cipta) Pasal 42 letter b. |
| Peraturan BPK (JDIH BPK): UU 13/2003, official PDF | <https://peraturan.bpk.go.id/Details/43013/uu-no-13-tahun-2003> | 2026-10-30 | Statutes carry no copyright in Indonesia: UU 28/2014 (Hak Cipta) Pasal 42 letter b. |
| Peraturan BPK (JDIH BPK): UU 8/1981, official PDF | <https://peraturan.bpk.go.id/Details/47041/uu-no-8-tahun-1981> | 2026-10-30 | Statutes carry no copyright in Indonesia: UU 28/2014 (Hak Cipta) Pasal 42 letter b. |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `uud-1945` | Undang-Undang Dasar Negara Republik Indonesia Tahun 1945 (Constitution) | 2 | 1945-08-18 to 2002-08-10 |
| `kuhp` | Kitab Undang-Undang Hukum Pidana (Penal Code), UU 1/2023 | 1 | 2026-01-02 to 2026-01-02 |
| `uu-ketenagakerjaan` | Undang-Undang Nomor 13 Tahun 2003 tentang Ketenagakerjaan | 1 | 2003-03-25 to 2003-03-25 |
| `kuhap-1981` | Undang-Undang Nomor 8 Tahun 1981 tentang Hukum Acara Pidana (KUHAP) | 2 | 1981-12-31 to 2026-01-02 |

The build made 6 commits:

| Commits | Kind |
| ---: | --- |
| 4 | first version of an act |
| 2 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `future`: laws not yet in force on 2026-10-30.
- 1 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 6 laws in the record.
- 12 tags.

## Dates

Each commit is dated at noon (Asia/Jakarta) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: A Constitution amendment takes effect on the day the MPR adopts it https://pusdik.mkri.id

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `fdb8fe8f3b15ac63453c72b741232b58c7feabbb8285bd46e82f287fc00726bc` (806205 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `a4faa25af85facb64b956b372f6b528aafdd7ec1`, `check.py` `3d00541d258745461ab52b1b0cb4e1716a27a95d`, `on.py` `644a6c0857fbcc72562032b58d57aa113fee0641`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

6 versions of 4 acts read back from git on the day each took effect and on the day before: 0 mismatches. Trailers: 0 commits whose trailers git cannot parse. Health: 0 merge commits on main, 0 commit dates that go backwards, 0 commits dated after the build.

A second build from the same corpus into an empty folder gave identical hashes for all 6 history commits and 12 tags (history tip `ceef1b45bc42777222473a9846ba91ff269224e9`).

## Decisions made by hand

- Language: Indonesian, the official language. No English text was used.
- The four amendments (1999, 2000, 2001, 2002) are shown as one step dated 10 August 2002, the day of the last, because the source gives only the original text and the final compilation.
- Units differing between the original and the compilation are credited to the combined amendments entry; no per-amendment credit was guessed.
- The Preamble (Pembukaan) is carried over unchanged from the original: it was not amended, and the compilation only differs in typesetting.
- Chapter (BAB) headings, page numbers, footnote keys and amendment asterisks were dropped; the Elucidation (Penjelasan) of the original was not included.
- Hard line wraps were joined; hyphenation at line ends was closed without a space.
- KUHP (UU 1/2023): text recognised by OCR from the official BPK scan (Tesseract 5.4, language ind) because the scan's own text layer has hundreds of errors; page headers, footers and page-end catchwords were removed; the Penjelasan is left out.
- KUHP version dated 2026-01-02, the day the code took effect under its Pasal 624 (3 years after promulgation on 2023-01-02), not its enactment date.
- UU 13/2003 (Ketenagakerjaan): one version, the act as enacted, dated 2003-03-25, the day it was promulgated and took effect (Pasal 193). Later amendments (UU 11/2020 and UU 6/2023, Cipta Kerja) and Constitutional Court rulings on it are not in this record.
- UU 13/2003: text from the PDF text layer as published, including its own word splits (for example "per baikan"); page headers, page numbers and page-end catchwords were removed, chapter/part/paragraph headings are not kept as files, and wrapped lines were joined.
- KUHAP 1981 (UU 8/1981): the act as enacted, dated 1981-12-31, the day it was promulgated and took effect (Pasal 286). Constitutional Court rulings that struck or conditioned parts of it between 2010 and 2025 are not in this record.
- KUHAP 1981: a second version on 2026-01-02 removes every unit, credited to UU 20/2025 (the new KUHAP), which repealed it on the day it took effect. The repeal and its date are read from the BPK record of UU 20/2025 (archived copy); the new KUHAP text itself is not built, because the official PDF is a scan.
- The BPK copy of UU 8/1981 is a retyped, born-digital text (from the Ministry of Law and Human Rights legislation database); its typing slips (for example "pennintaan", "fungai") are kept as published.
- UU 8/1981: text from the PDF text layer as published; page footers were removed, chapter/part/paragraph headings are not kept as files, and wrapped lines were joined.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- OCR (Tesseract 5.4, tessdata_best ind) of 345 page images for the KUHP; no model-generated text. Paragraph/line fixes were mechanical (headers, catchwords, ayat breaks).
- Claude Code wrote the parser; it did not write or alter any legal text.
- Claude Code wrote the parser; it did not write or alter any legal text.
