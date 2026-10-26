# taragot-nettside

Offentlig nettside for plateselskapet **5b / Taragot** — frittstående prototype
i ren HTML/CSS.

## Filer
- `index.html` — forsida.
- `katalog.html` — alle utgivelser.
- `om-oss.html` — om selskapet og menneskene bak.
- `stil.css` — felles oppsett for alle sidene (meny, seksjoner, kort, footer).
- `felles.js` — felles oppførsel: meny, språkvelger, karusell, nyhetsbrev.
- `tokens.css` — designtokens: farger, fonter og størrelser som CSS-variabler.
  Her endrer man uttrykket uten å røre resten.
- `bilder/` — logo, coverbilder (`bilder/covers/`) og bilder til Om oss (`bilder/om-oss/`).

Toppmeny og footer står i hver side. Endres de, må alle tre sidene oppdateres.

Fonten **Inter** (gratis, Google Fonts) brukes for all tekst.

## Redigere og publisere
Loopen er: **endre → lagre → `git push` → siden publiseres automatisk** (GitHub
Pages).

1. Klon repoet og åpne mappa i en editor (f.eks. VS Code — gratis).
2. Endre `tokens.css` (farger/størrelser) eller `index.html`.
3. Se endringen lokalt: dobbeltklikk `index.html` (husk at `tokens.css` må ligge
   i samme mappe), eller bruk VS Code-utvidelsen **Live Server** for
   auto-oppdatering mens du redigerer.
4. Publiser:
   ```bash
   git add -A && git commit -m "Beskriv endringen" && git push
   ```
   Innen et par minutter er det live.

## Responsivt
Siden er **én side som tilpasser seg** skjermbredden (cover-kort 4 → 3 → 2 → 1).
Åpne siden på telefon/nettbrett for å se de versjonene, eller dra
nettleservinduet smalere på PC.

## Jobbe flere sammen
Kjør `git pull` før du begynner å redigere, og `git push` når du er ferdig — så
unngår dere å overskrive hverandre.
