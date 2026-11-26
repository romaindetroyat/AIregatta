"""Fabrique docs/masterclass-ai-regatta-autonome.html : la présentation en un seul fichier
(images intégrées, régate 3D intégrée dans l’iframe). Lancer depuis la racine du dépôt."""
import base64, html, re, pathlib
D = pathlib.Path('docs')
s = (D / 'masterclass-ai-regatta.html').read_text()
mime = {'.jpg': 'image/jpeg', '.png': 'image/png'}
def data(m):
    p = D / m.group(1)
    return 'data:%s;base64,%s' % (mime[p.suffix], base64.b64encode(p.read_bytes()).decode())
s = re.sub(r'(masterclass/[\w.-]+\.(?:jpg|png))', data, s)
# régate 3D : copie intégrée (mode « embed » forcé), chargée dans l’iframe via srcdoc
r3 = ('<!doctype html><html lang="fr" class="embed"><head><meta charset="utf-8">'
      '<meta name="viewport" content="width=device-width, initial-scale=1">' + (D / 'regate-3d.html').read_text())
s = s.replace("ifr.src='regate-3d.html#embed';", "ifr.srcdoc=document.getElementById('r3d').textContent.split('<\\\\/script>').join('</'+'script>');")
old = '<a class="open" href="regate-3d.html" target="_blank" rel="noopener">Ouvrir dans un onglet ↗</a>'
assert old in s
s = s.replace(old, '')
assert s.count('<script>\n(function(){') == 1
s = s.replace('<script>\n(function(){', '<script type="text/plain" id="r3d">' + r3.replace('</script>', '<\\/script>') + '</script>\n<script>\n(function(){')
(D / 'masterclass-ai-regatta-autonome.html').write_text(s)
print(len(s) // 1024, 'Ko')
