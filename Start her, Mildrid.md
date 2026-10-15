# Start her, Mildrid 👋

Velkommen! Dette er repoet for den nye offentlige nettsiden til **5b / Taragot**.
Du eier utseendet. Måten du jobber på er enkel: **du forteller Claude hva du vil
ha endret — så gjør Claude det i filene.** Du skal ikke kode.

Siden er live her: **https://nettside.5b.no**

---

## Hva du trenger (alt gratis, ingen koding)

| Verktøy | Hva du bruker det til |
|--------|------------------------|
| **Claude Code** (desktop-app) | Her *forteller* du hva du vil: «gjør knappen større», «bytt aksentfargen til …». Claude endrer filene. |
| **GitHub Desktop** | Hente siste versjon og publisere — med knapper, ingen kommandolinje. |
| **Nettleseren din** | Se resultatet på nettside.5b.no. |

Du trenger **ikke** VS Code eller noe annet redigeringsverktøy.

---

## Engangs-oppsett (gjøres én gang)

1. **Godta invitasjonen.** Du har fått en e-post fra GitHub (eller se på
   github.com → varsler) → **Accept invitation** til `Tellef47/taragot-nettside`.
2. **Installer GitHub Desktop:** https://desktop.github.com → logg inn med
   GitHub-kontoen din. (Dette gjør at publisering virker.)
3. **Installer Claude Code** (desktop-appen).
4. **Hent ned repoet:** i GitHub Desktop → **File → Clone Repository →**
   fanen **GitHub.com** → velg **taragot-nettside** → velg en mappe → **Clone**.

Nå ligger nettside-filene i en mappe på din maskin.

---

## Slik jobber du (den daglige loopen)

1. **Hent siste først:** i GitHub Desktop, klikk **Fetch origin** (og **Pull** hvis
   det er noe nytt). Da jobber du alltid på nyeste versjon.
2. **Åpne mappa i Claude Code** og si hva du vil ha endret. Eksempler:
   - «Gjør hero-videoen litt høyere.»
   - «Bytt aksentfargen til #D96A34.»
   - «Mer luft mellom cover-kortene.»
   Claude finner ut hvilken fil det er og gjør endringen.
3. **Se resultatet** (valgfritt, før publisering): dobbeltklikk `index.html` i
   mappa, så åpnes siden i nettleseren.
4. **Publiser:** i GitHub Desktop → skriv en kort setning om hva du gjorde →
   **Commit to main** → **Push origin**.
5. **Ferdig!** Siden oppdaterer seg selv på **nettside.5b.no** etter ca. 1–2 minutter.

Ingen server, ingen deploy-kommando — bare push.

---

## Filene (bare så du vet — du trenger ikke røre dem selv)

- **`tokens.css`** — fargene, fontene og størrelsene. De «trygge rattene».
- **`index.html`** — selve strukturen og layouten.

Du kan bare beskrive hva du vil, så velger Claude riktig sted.

---

## Godt å vite

- **Vanskelig å ødelegge noe.** Alt er lagret i versjoner — vi kan alltid rulle
  tilbake til en tidligere utgave. Prøv deg fram.
- **Fonten** er Inter (gratis). Logoen «Taragot Sounds» beholder en serif.
- **Responsivt:** siden tilpasser seg mobil/nettbrett automatisk (cover-kortene
  går 4 → 3 → 2 → 1). Dra nettleservinduet smalere for å se det.
- **Jobber flere samtidig?** Klikk alltid **Fetch/Pull** før du begynner, og
  **Push** når du er ferdig — så overskriver dere ikke hverandre.

## Spør om hjelp
Står du fast, spør Claude direkte i økta — eller ta kontakt med Tellef. Det er
lettere å justere tidlig enn sent. Lykke til! 🎵
