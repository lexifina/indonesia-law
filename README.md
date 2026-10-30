# Indonesia: law history in git

A small build of the law of Indonesia as a git history: one file per article, one commit per law on the day it took effect, and the law that made the change as the commit's author. It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `id/`.

Language: Indonesian (Bahasa Indonesia), the official language. The text is in Indonesian; this README is in English.

## What is in it now

| Folder | Instrument | Versions | History |
| --- | --- | ---: | --- |
| `uud-1945/` | Undang-Undang Dasar Negara Republik Indonesia Tahun 1945 (the Constitution) | 2 | The original text of 18 August 1945, and the Constitution as amended four times (1999-2002), in force from 10 August 2002 |
| `kuhp/` | Kitab Undang-Undang Hukum Pidana, Undang-Undang Nomor 1 Tahun 2023 (the new Penal Code), Pasal 1 to 624 | 1 | The code as promulgated on 2 January 2023, in force from 2 January 2026 (Pasal 624). **Text recognised by OCR, see below.** |

## What it does not show

- **The four amendments one by one.** The source gives the original text and the final compilation, so the 1999, 2000, 2001 and 2002 amendments appear as one commit dated 10 August 2002 (the day of the last), credited to a combined entry. `git blame` therefore names that entry, not the individual amendment.
- **The compilation is not itself official.** The Constitutional Court states that the single-text version ("Dalam Satu Naskah") is not an official text; the official texts are the original and the four amendment texts. The Preamble is carried over from the original, since it was never amended.
- **Not included:** the Elucidation (Penjelasan) of the original text, chapter headings, the Elucidation (Penjelasan) of the KUHP, and every statute other than the KUHP (the Civil Code and the Commercial Code are colonial-era texts with no official Indonesian-language edition found). Between 1949 and 1959 other constitutions applied; they are not here.

## About the KUHP text: OCR

The only official copy of UU 1/2023 reachable was the signed scan published by the Peraturan BPK database (`peraturan.bpk.go.id/Download/287456`, 345 pages). Its embedded text layer has hundreds of errors, so the pages were read again with Tesseract 5.4 (language `ind`, two passes, the better pass kept per page). **The KUHP files are therefore OCR text, not a typed copy.** Mechanical clean-up: page headers, footers and page-end catchword lines were removed, wrapped lines joined, ayat and list markers renumbered in sequence where the OCR misread a digit, and the semicolons that end list items (which Tesseract reads as commas) were restored. A few errors found by checking pages against the scan were corrected by hand (Pasal 3, 82 and 113). Spot checks of scan pages 29, 40 and 200 against the text matched word for word. Other OCR slips may remain, especially digits inside cross-references: **check the signed scan before relying on any wording.** The Elucidation (Penjelasan) printed after the law is not included.

## Dates and authors

Each commit is dated at noon, Asia/Jakarta, on the day the change took effect. The author is the law that made the change, with an address that cannot exist (`perubahan-uud-1999-2002@mkri.id.invalid`). The first version is credited to the original text, `uud-1945`.

## Sources

| Source | Kind | Notes |
| --- | --- | --- |
| [Buku Saku UUD 1945 dan UU MK (Mahkamah Konstitusi)](https://pusdik.mkri.id/materi/materi_294_Buku%20Saku%20UUD%201945%20dan%20UU%20MK_2020.pdf) | Official publication of the Constitutional Court | Used; retrieved 29 October 2026 |
| [Peraturan BPK: UU 1/2023 (signed scan)](https://peraturan.bpk.go.id/Download/287456) | Official legislation database (BPK) | Used for the KUHP; retrieved 30 October 2026; OCR |
| [peraturan.go.id](https://peraturan.go.id) | Official legislation database | – |

Research guides that cover every country: [GlobaLex](https://www.nyulawglobal.org/globalex/) and the [Law Library of Congress Guide to Law Online](https://www.loc.gov/research-centers/law-library-of-congress/researcher-resources/guide-to-law-online/).

## Licence

The Constitution is an official text of the Republic of Indonesia; the Court's publication states no reuse licence. Statutes carry no copyright in Indonesia (UU 28/2014, Pasal 42 letter b). See `LICENSE`. This repository is not legal advice and not an official publication. No AI model wrote or changed legal text; the KUHP words come from OCR (Tesseract), with the small hand corrections named above.
