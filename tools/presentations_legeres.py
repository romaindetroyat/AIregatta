"""Versions légères (< 10 Mo) des deux présentations hors ligne : images et vidéo recompressées
(dossier docs/masterclass-leger/). Usage : python3 tools/presentations_legeres.py [three.min.js local]"""
import pathlib, subprocess, sys
D = pathlib.Path('docs')
three = sys.argv[1:2]
for src, out in [('masterclass-ai-regatta.html', 'Battleboats-2027-AI-Regatta-masterclass-leger.html'),
                 ('ai-regatta-2027-proposition.html', 'AI-Regatta-2027-proposition-leger.html')]:
    tmp = D / ('_leger-' + src)
    tmp.write_text((D / src).read_text().replace('masterclass/', 'masterclass-leger/'))
    subprocess.run([sys.executable, 'tools/masterclass_hors_ligne.py', *(three or ['']), tmp.name, out], check=True)
    tmp.unlink()
