"""Builds index.html from src.html: pastes in Flicks Demo Kit v1.1 and the Flick tags (exact copies from flam-links/tags)."""
import json, sys
KIT, TAGS = sys.argv[1], sys.argv[2]
s = open('src.html').read()
s = s.replace('/*KIT*/', open(KIT).read())
tag = lambda slug: open(f'{TAGS}/{slug}/tag.txt').read().strip()
# Silverado's own "Shop Now" is a plain button, not a vertex trigger, so the kit cannot hide it. Nextdoor's CTA replaces it.
HIDE = ('<script>(function(){var n=0;(function f(){var v=document.querySelector("vertex-player"),r=v&&v.shadowRoot;'
        'if(r&&!r.querySelector("style[data-nd]")){var s=document.createElement("style");s.setAttribute("data-nd","");'
        's.textContent="button[data-node]:not([data-vertex-diff]){visibility:hidden!important;pointer-events:none!important}";r.appendChild(s)}'
        'if(++n<240)setTimeout(f,250)})()})();</script>')
B = {'lovesac': ('Lovesac', 'lovesac', ''), 'silverado': ('Chevrolet Silverado', 'chevrolet-silverado', HIDE),
     'bmo': ('BMO', 'bmo-bank-2', ''), 'barkbox': ('BarkBox', 'barkbox', ''), 'geico': ('GEICO', 'geico', ''),
     'lc': ('Little Caesars', 'little-caesars', '')}
br = {k: {'name': n, 'ar': 'square', 'bg': '#f2f2f2', 'tag': tag(sl) + ('\n' + x if x else '')} for k, (n, sl, x) in B.items()}
s = s.replace('/*BRANDS*/', json.dumps(br, ensure_ascii=False).replace('</', '<\\/'))
open('index.html', 'w').write(s)
print('index.html', len(s))
