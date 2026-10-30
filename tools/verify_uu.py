"""Check a corpus.d part against its born-digital PDF: the text layer from "Menimbang" to the Lembaran Negara line,
less page headers ("PRESIDEN / REPUBLIK INDONESIA / - n -"), page-end catchwords, BAB/Bagian/Paragraf headings with
their titles and the "Pasal n" lines, must equal the units' text character for character, ignoring whitespace.
Usage: python -X utf8 verify_uu.py <part.json> <pdf>"""
import json, re, sys
import fitz

part = json.load(open(sys.argv[1], encoding='utf-8'))
src = []
for page in fitz.open(sys.argv[2]):
    ls = [re.sub(r'\s+', ' ', l).strip() for l in page.get_text().split('\n')]
    ls = [l for l in ls if l and l != 'www.djpp.kemenkumham.go.id']
    if ls[:2] == ['PRESIDEN', 'REPUBLIK INDONESIA']:
        ls = ls[2:]
    if ls and re.fullmatch(r'-\s*\d+\s*-', ls[0]):
        ls = ls[1:]
    if ls and (ls[-1].endswith('…') or ls[-1].endswith('...')):
        print('catchword dropped:', ls[-1])
        ls = ls[:-1]
    src += ls
i0 = next(i for i, l in enumerate(src) if l.startswith('Menimbang'))
i1 = next(i for i, l in enumerate(src) if re.match(r'LEMBARAN NEGARA REPUBLIK INDONESIA (TAHUN \d+ )?NOMOR', l))
out, head, nxt = [], False, 1
for l in src[i0:i1 + 1]:
    if re.fullmatch(r'(BAB [IVXL]+|Bagian [A-Z][a-z]+|Paragraf \d+)', l):
        head = True
        continue
    if l == f'Pasal {nxt}':
        nxt += 1
        head = False
        continue
    if head:
        continue
    out.append(l)
S = re.sub(r'\s', '', ''.join(out))
U = ''.join(re.sub(r'\s', '', re.sub(r'^# [^\n]*\n', '', u['text'])) for u in part['acts'][0]['versions'][0]['units'].values())
if S == U:
    print('OK', len(S), 'characters identical;', nxt - 1, 'Pasal')
    sys.exit(0)
n = next((i for i in range(min(len(S), len(U))) if S[i] != U[i]), min(len(S), len(U)))
print('MISMATCH at', n, len(S), len(U))
print('src :', S[max(0, n - 100):n + 100])
print('unit:', U[max(0, n - 100):n + 100])
sys.exit(1)
