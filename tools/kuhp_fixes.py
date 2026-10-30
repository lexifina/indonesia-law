# Hand corrections to the OCR text, each checked against the scan page image. Run inside parse_kuhp.py (uses U and re).
FIXES = [
    ('pasal-082',
     'jam. 3) Jika pada saat menjalani pidana pengganti sebagian 88 pidana denda dibayar, lama pidana pengganti dikurangi menurut ukuran yang sepadan. REPUBLIK INDONESIA.\n(3) Perhitungan',
     'jam.\n(3) Jika pada saat menjalani pidana pengganti sebagian pidana denda dibayar, lama pidana pengganti dikurangi menurut ukuran yang sepadan.\n(4) Perhitungan'),
    ('pasal-113',
     'f. pencabutan Surat izin mengemudi, dan/atau 8\n',
     'f. pencabutan Surat izin mengemudi; dan/atau\ng. perbaikan akibat Tindak Pidana.\n'),
    ('pasal-113',
     'paling lama 1 (satu) tahun. perbaikan akibat Tindak Pidana.\n',
     'paling lama 1 (satu) tahun.\n'),
]
FIXES += [('pasal-003', 'ayat (3) dan ayat (9) tidak', 'ayat (3) dan ayat (5) tidak')]
for k, bad, good in FIXES:
    assert bad in U[k]['text'], (k, bad)
    U[k]['text'] = U[k]['text'].replace(bad, good)
for u in U.values():
    u['text'] = re.sub(r'\s+RE[A-Z]{2,6}K INDONESIA\.?(?=\n|$)', '', u['text'])
for u in U.values():
    u['text'] = re.sub(r"\s+-\.?\d+-(?=\n|$)", '', u['text'])
    u['text'] = re.sub(r"\s+'(?=\n|$)", '', u['text'])
