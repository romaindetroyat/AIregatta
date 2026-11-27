"""Fabrique la présentation de la masterclass en UN seul fichier HTML qui marche sans internet :
images, régate 3D, moteur three.js et polices intégrés.
Lancer depuis la racine du dépôt :  python3 tools/masterclass_hors_ligne.py
Sortie : docs/Battleboats-2027-AI-Regatta-masterclass.html
Arguments : [three.min.js local] [page source dans docs/] [fichier de sortie dans docs/]"""
import base64, re, pathlib, sys, urllib.request

D = pathlib.Path('docs')
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36'
THREE = 'https://cdn.jsdelivr.net/npm/three@0.147.0/build/three.min.js'
cache = {}

def get(url, binary=False):
    if url not in cache:
        req = urllib.request.Request(url, headers={'User-Agent': UA})
        cache[url] = urllib.request.urlopen(req, timeout=60).read()
    return cache[url] if binary else cache[url].decode()

def inline_fonts(html):
    """Remplace le lien Google Fonts par les polices intégrées (alphabets latin et latin étendu)."""
    html = re.sub(r'<link rel="preconnect" href="https://fonts\.g[^"]*"( crossorigin)?>\n?', '', html)
    def repl(m):
        css = get(m.group(1).replace('&amp;', '&'))
        keep = []
        for comment, block in re.findall(r'/\* ([\w-]+) \*/\s*(@font-face \{.*?\})', css, re.S):
            if comment not in ('latin', 'latin-ext'):
                continue
            url = re.search(r'url\((https://[^)]+)\)', block).group(1)
            data = base64.b64encode(get(url, True)).decode()
            keep.append(block.replace(url, 'data:font/woff2;base64,' + data))
        return '<style>\n' + '\n'.join(keep) + '\n</style>'
    return re.sub(r'<link rel="stylesheet" href="(https://fonts\.googleapis\.com/[^"]+)">', repl, html)

SRC = sys.argv[2] if len(sys.argv) > 2 else 'masterclass-ai-regatta.html'
OUT = sys.argv[3] if len(sys.argv) > 3 else 'Battleboats-2027-AI-Regatta-masterclass.html'
s = (D / SRC).read_text()
s = inline_fonts(s)
# images
mime = {'.jpg': 'image/jpeg', '.png': 'image/png', '.mp4': 'video/mp4', '.webp': 'image/webp'}
s = re.sub(r'masterclass(?:-leger)?/[\w.-]+\.(?:jpg|png|mp4|webp)',
           lambda m: 'data:%s;base64,%s' % (mime[pathlib.Path(m.group(0)).suffix], base64.b64encode((D / m.group(0)).read_bytes()).decode()), s)
# régate 3D : polices et three.js intégrés, mode « embed » forcé
r3 = inline_fonts((D / 'regate-3d.html').read_text())
tag = '<script src="%s"></script>' % THREE
assert tag in r3
three = pathlib.Path(sys.argv[1]).read_text() if len(sys.argv) > 1 else get(THREE)
assert 'REVISION="147"' in three.replace(' ', '') or '"147"' in three
r3 = r3.replace(tag, '<script>' + three + '</script>')
r3 = ('<!doctype html><html lang="fr" class="embed"><head><meta charset="utf-8">'
      '<meta name="viewport" content="width=device-width, initial-scale=1">' + r3)
s = s.replace("ifr.src='regate-3d.html#embed';",
              "ifr.srcdoc=document.getElementById('r3d').textContent.split('<\\\\/script>').join('</'+'script>');")
old = '<a class="open" href="regate-3d.html" target="_blank" rel="noopener">Ouvrir dans un onglet ↗</a>'
assert old in s
s = s.replace(old, '')
assert s.count('<script>\n(function(){') == 1
s = s.replace('<script>\n(function(){', '<script type="text/plain" id="r3d">' + r3.replace('</script>', '<\\/script>') + '</script>\n<script>\n(function(){')
assert 'fonts.googleapis' not in s and 'cdn.jsdelivr' not in s.replace(THREE, '')
out = D / OUT
out.write_text(s)
print(out, len(s) // 1024, 'Ko')
