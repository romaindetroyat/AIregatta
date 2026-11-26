"""Retire l’enveloppe <!doctype>/<html>/<head>/<body> d’une page autonome pour la publier en Artifact.
Usage : python3 tools/fragment_artifact.py docs/page-autonome.html sortie.html"""
import sys
s = open(sys.argv[1]).read()
head = '<!doctype html>\n<html lang="fr">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
assert s.startswith(head); s = s[len(head):]
a = '</style>\n</head>\n<body>\n'; assert s.count(a) == 1; s = s.replace(a, '</style>\n')
assert s.endswith('</body>\n</html>\n'); s = s[:-len('</body>\n</html>\n')]
open(sys.argv[2], 'w').write(s)
