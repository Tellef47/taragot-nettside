# Legger til skjulte søkeord (data-sok) på kort i katalog.html.
# Bruk: python3 verktoy/sokeord.py "Navn som skal legges til" "artist-tekst som begynner slik" ...
import re, sys, html
p = 'katalog.html'; s = open(p).read()
navn = sys.argv[1]
for start in sys.argv[2:]:
    pat = re.compile(r'<a class="kort"( data-sok="([^"]*)")? href="([^"]+)"((?:(?!</a>).)*?<p class="artist">' + re.escape(html.escape(start, quote=False)) + r')')
    treff = list(pat.finditer(s)); assert treff, start
    for m in reversed(treff):
        gamle = m.group(2) or ''
        if navn.lower() in (gamle + m.group(4)).lower(): print('har allerede:', m.group(3)); continue
        ny = (gamle + ' ' + navn).strip()
        s = s[:m.start()] + f'<a class="kort" data-sok="{ny}" href="{m.group(3)}"' + m.group(4) + s[m.end():]
        print('lagt til:', m.group(3))
open(p, 'w').write(s)
