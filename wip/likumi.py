"""Read one likumi.lv version page ("redakcija") into units and amendment notes. No network.

A page's text sits in div.doc-body as a flat run of blocks: TV206/TV207 (the act's title), TV208 (preamble),
TV211/TV212 (part and chapter headings), TV213 (articles, data-num="18" or "10.1"), TV216 (signatures), and the
transitional provisions and EU-directive references at the end. Each changed block carries a note,
p.labojumu_pamats: "(30.04.2002. likuma redakcijā, kas stājas spēkā 05.11.2002.)" with a link to the amending law
(/ta/id/<id>-<slug>) and to the version it starts (/redakcijas-datums/YYYY/MM/DD). Notes are not law text: they are
taken out and used only to date and credit changes.
"""
from __future__ import annotations

import re

from bs4 import BeautifulSoup, NavigableString, Tag

ROMAN = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100}
HIDDEN = ('panta-doc-npk', 'info-icon-wrapper', 'labojumu_pamats', 'tooltip', 'helper', 'court', 'panta-piezimite')
BLOCK = {'p', 'div', 'br', 'li', 'tr', 'table', 'center', 'h1', 'h2', 'h3', 'h4', 'ul', 'ol', 'blockquote'}


def roman(s: str) -> int | None:
    if not s or any(c not in ROMAN for c in s):
        return None
    n = 0
    for a, b in zip(s, s[1:] + ' '):
        v = ROMAN[a]
        n += -v if b in ROMAN and ROMAN[b] > v else v
    return n


def norm(s: str) -> str:
    s = s.replace('\xa0', ' ').replace(' ', ' ').replace(' ', ' ')
    for z in ('​', '﻿', '⁠', '\xad'):
        s = s.replace(z, '')
    for q in ('“', '”', '„', '‟', '″'):
        s = s.replace(q, '"')
    s = s.replace('‘', "'").replace('’', "'").replace('‚', "'")
    s = s.replace('–', '-').replace('—', '-')
    s = re.sub(r'[ \t\r\n]+', ' ', s).strip()
    s = re.sub(r' ([,;:.)])', r'\1', s)
    s = re.sub(r'\( ', '(', s)
    return s


def hidden(el: Tag) -> bool:
    cls = el.get('class') or []
    if any(c in HIDDEN for c in cls):
        return True
    st = (el.get('style') or '').replace(' ', '').lower()
    return 'display:none' in st


def lines_of(el: Tag) -> list[str]:
    """One line per paragraph (block element or <br>); sup numbers become '.N' suffix-free plain digits."""
    out, buf = [], []

    def flush():
        t = norm(''.join(buf))
        if t:
            out.append(t)
        buf.clear()

    def walk(n):
        for c in n.children:
            if isinstance(c, NavigableString):
                if c.__class__.__name__ in ('Comment', 'Script', 'Stylesheet'):
                    continue
                buf.append(str(c))
            elif isinstance(c, Tag):
                if c.name in ('script', 'style') or hidden(c):
                    continue
                if c.name == 'br':
                    flush()
                    continue
                if c.name == 'sup':
                    buf.append(c.get_text())
                    continue
                blk = c.name in BLOCK
                if blk:
                    flush()
                walk(c)
                if blk:
                    flush()
    walk(el)
    flush()
    return out


DATE = re.compile(r'(\d\d)\.(\d\d)\.(\d{4})')


def iso(d: str) -> str | None:
    m = DATE.search(d)
    return f'{m.group(3)}-{m.group(2)}-{m.group(1)}' if m else None


def note_events(p: Tag, own_id: int) -> list[dict]:
    """[{law_id, law_slug, law_date, in_force, court}] from one note, in order. A version link closes the laws
    named since the previous one."""
    events, pending = [], []
    for a in p.find_all('a'):
        href = a.get('href') or ''
        m = re.search(r'/ta/id/(\d+)(?:-([a-z0-9-]+))?(?:/redakcijas-datums/(\d{4})/(\d\d)/(\d\d))?', href)
        if not m:
            continue
        lid = int(m.group(1))
        if m.group(3):
            day = f'{m.group(3)}-{m.group(4)}-{m.group(5)}'
            for e in pending:
                e['in_force'] = day
                events.append(e)
            pending = []
            continue
        if lid == own_id:
            continue
        # text just before the link tells a court ruling from a law
        prev = ''
        for s in a.previous_siblings:
            prev = (s.get_text() if isinstance(s, Tag) else str(s)) + prev
            if len(prev) > 80:
                break
        pending.append({'law_id': lid, 'law_slug': m.group(2) or '', 'law_date': iso(a.get_text()),
                        'court': 'Satversmes tiesas' in prev[-80:] or 'spriedum' in (m.group(2) or '')})
    for e in pending:
        e['in_force'] = None
        events.append(e)
    return events


def heading_key(text: str, used: set) -> str:
    t = text.strip()
    m = re.match(r'^([IVXLC]+)\.?\s*(\d*)\.?\s*nodaļa', t, re.I)
    if m and roman(m.group(1).upper()):
        k = f'nodala-{roman(m.group(1).upper()):02d}' + (f'-{m.group(2)}' if m.group(2) else '')
    else:
        m2 = re.match(r'^(\d+)\.\s*(\d*)\.?\s*nodaļa', t)
        if m2:
            k = f'nodala-{int(m2.group(1)):02d}' + (f'-{m2.group(2)}' if m2.group(2) else '')
        else:
            low = t.lower()
            if low.startswith('vispārējā daļa'):
                k = 'dala-1-visparejā'
            elif low.startswith('sevišķā daļa'):
                k = 'dala-2-sevisķa'
            elif low.startswith('pārejas noteikumi'):
                k = 'parejas-noteikumi'
            elif low.startswith('informatīva atsauce'):
                k = 'zz-es-direktivas'
            else:
                k = 'virsraksts-' + re.sub(r'[^a-z0-9]+', '-', ascii_fold(low))[:40].strip('-')
    k = ascii_fold(k)
    base, i = k, 2
    while k in used:
        k = f'{base}-{i}'
        i += 1
    return k


FOLD = str.maketrans('āčēģīķļņōŗšūžĀČĒĢĪĶĻŅŌŖŠŪŽ', 'acegiklnorsuzACEGIKLNORSUZ')


def ascii_fold(s: str) -> str:
    return s.translate(FOLD)


def art_key(num: str) -> str:
    parts = num.split('.')
    return 'pants-' + '-'.join([f'{int(parts[0]):03d}'] + [p for p in parts[1:] if p])


def parse_page(raw: bytes, own_id: int) -> dict:
    """{'version': 'YYYY-MM-DD', 'units': {key: {label, kind, text, events, parent}}, 'removed': {key: events}}"""
    html = raw.decode('utf-8', 'replace')
    soup = BeautifulSoup(html, 'lxml')
    body = soup.select_one('div.doc-body')
    ver = re.search(r'\{"selected":\{"value":"(\d\d)\.(\d\d)\.(\d{4})"', html)
    out = {'version': f'{ver.group(3)}-{ver.group(2)}-{ver.group(1)}' if ver else None, 'units': {}, 'removed': {},
           'order': []}
    used: set = set()
    parent = None
    section = None  # 'pn' inside transitional provisions, 'es' inside the EU-directive note
    for blk in body.find_all(recursive=False):
        cls = blk.get('class') or []
        if not any(c.startswith('TV') for c in cls):
            continue
        tv = next(c for c in cls if c.startswith('TV'))
        events = []
        for p in blk.find_all('p', class_='labojumu_pamats'):
            events += note_events(p, own_id)
        lines = lines_of(blk)
        if not lines:
            continue
        if tv in ('TV206', 'TV207'):
            continue
        num = blk.get('data-num')
        if tv == 'TV213' and num and section is None:
            key, kind = art_key(num), 'art'
            label = f'{num}. pants'
        elif tv == 'TV208':
            key, kind, label = 'ievads', 'preamble', 'Ievads'
        elif tv == 'TV216':
            key, kind, label = 'zz-paraksti', 'signatures', 'Paraksti'
        elif tv in ('TV211', 'TV212', 'TV210', 'TV209') and not num:
            key = heading_key(lines[0], used)
            kind, label = 'heading', lines[0]
            if key == 'parejas-noteikumi':
                section = 'pn'
            elif key == 'zz-es-direktivas':
                section = 'es'
            parent = key
        elif section == 'pn' and num:
            key, kind, label = 'parejas-noteikumi-' + '-'.join(f'{int(x):03d}' if i == 0 else x for i, x in enumerate(num.split('.')) if x), 'transitional', f'Pārejas noteikumu {num}. punkts'
        elif section == 'es':
            key, kind, label = f'zz-es-direktivas-{len([k for k in out["order"] if k.startswith("zz-es-direktivas-")]) + 1:02d}', 'eu-note', 'Informatīva atsauce uz ES direktīvām'
        else:
            key = f'zz-bloks-{tv.lower()}-{len(out["order"]) + 1:03d}'
            kind, label = 'other', tv
        if key in used and kind != 'heading':
            base, i = key, 2
            while key in used:
                key = f'{base}-{i}'
                i += 1
        used.add(key)
        text_lines = [l for l in lines]
        whole = ' '.join(text_lines)
        if kind in ('art', 'transitional') and re.fullmatch(r'[\d.]*\s*\(Izslēgts[^)]*\)\.?', whole) or \
                (kind in ('art', 'transitional') and re.fullmatch(r'[\d.]+\s*\[?\(?Izslēgts.*', whole) and len(whole) < 200):
            evs = []
            for a_p in blk.find_all(['span', 'p']):
                if 'Izslēgts' in a_p.get_text():
                    evs = note_events(a_p, own_id)
                    break
            out['removed'][key] = {'label': label, 'events': evs or events}
            out['order'].append(key)
            continue
        out['units'][key] = {'label': label, 'kind': kind, 'text': '\n'.join(text_lines) + '\n', 'events': events,
                             'parent': parent if kind != 'heading' else None}
        out['order'].append(key)
    return out
