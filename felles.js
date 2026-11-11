// Felles oppførsel for alle sidene: meny, språkvelger, karusell og nyhetsbrev.
// Hver del kjører bare hvis siden har elementene den trenger.

// Meny skjules når man scroller ned, vises når man scroller opp
var nav = document.getElementById('nav');
var sisteY = window.scrollY;
window.addEventListener('scroll', function () {
  var y = window.scrollY;
  if (y > sisteY && y > 90 && !nav.classList.contains('nav--apen')) nav.classList.add('nav--skjult');
  else nav.classList.remove('nav--skjult');
  sisteY = y;
}, { passive: true });

// Til toppen-knappen vises når man har scrollet forbi første skjermbilde
var tilToppen = document.querySelector('.til-toppen');
if (tilToppen) {
  var visTilToppen = function () { tilToppen.classList.toggle('til-toppen--synlig', window.scrollY > window.innerHeight * 0.6); };
  window.addEventListener('scroll', visTilToppen, { passive: true });
  visTilToppen();
  tilToppen.addEventListener('click', function (e) {
    e.preventDefault();
    window.scrollTo({ top: 0, behavior: 'smooth' });
    var logo = document.querySelector('.logo'); if (logo) logo.focus({ preventScroll: true });
  });
}

// Hamburgermeny (mobil)
var menyKnapp = document.getElementById('meny-knapp');
function settMeny(apen) {
  nav.classList.toggle('nav--apen', apen);
  document.body.classList.toggle('meny-apen', apen);
  menyKnapp.setAttribute('aria-expanded', apen);
  menyKnapp.setAttribute('aria-label', apen ? 'Lukk meny' : 'Åpne meny');
  if (apen) document.documentElement.style.setProperty('--meny-topp', (nav.getBoundingClientRect().bottom + 16) + 'px');
  if (apen) { var forste = document.querySelector('#meny > a'); if (forste) forste.focus(); }
}
menyKnapp.addEventListener('click', function () {
  settMeny(!nav.classList.contains('nav--apen'));
});
document.querySelectorAll('#meny a').forEach(function (a) {
  a.addEventListener('click', function () { settMeny(false); });
});
document.addEventListener('keydown', function (e) {
  if (e.key === 'Escape' && nav.classList.contains('nav--apen')) { settMeny(false); menyKnapp.focus(); }
});
// Lukk menyen hvis vinduet blir bredt nok til vanlig meny
window.addEventListener('resize', function () {
  if (window.innerWidth > 1000 && nav.classList.contains('nav--apen')) settMeny(false);
});

// Språkvelger
var sprakKnapp = document.getElementById('sprak-knapp');
var sprakListe = document.getElementById('sprak-liste');
function lukkSprak() { sprakListe.hidden = true; sprakKnapp.setAttribute('aria-expanded', 'false'); }
sprakKnapp.addEventListener('click', function (e) {
  e.stopPropagation();
  var apen = sprakListe.hidden;
  sprakListe.hidden = !apen;
  sprakKnapp.setAttribute('aria-expanded', apen);
  if (apen) sprakListe.querySelector('a').focus();
});
document.addEventListener('click', function (e) {
  if (!document.getElementById('sprakvelger').contains(e.target)) lukkSprak();
});
document.addEventListener('keydown', function (e) {
  if (e.key === 'Escape' && !sprakListe.hidden) { lukkSprak(); sprakKnapp.focus(); }
});

// Karusell (forsiden, mobil): coveret lengst til venstre får fokus
(function () {
  var rad = document.querySelector('.karusell');
  if (!rad) return;
  var kortene = Array.prototype.slice.call(rad.querySelectorAll('.kort'));
  var forrige = document.getElementById('pil-forrige');
  var neste = document.getElementById('pil-neste');
  var aktiv = 0;
  function erKarusell() { return getComputedStyle(rad).display === 'flex'; }
  function finnAktiv() {
    // Helt til høyre: siste cover er aktivt
    if (rad.scrollLeft + rad.clientWidth >= rad.scrollWidth - 4) return kortene.length - 1;
    var start = rad.scrollLeft + parseFloat(getComputedStyle(rad).paddingLeft), best = 0, avstand = Infinity;
    kortene.forEach(function (k, i) {
      var d = Math.abs(k.offsetLeft - start);
      if (d < avstand) { avstand = d; best = i; }
    });
    return best;
  }
  function oppdater() {
    aktiv = erKarusell() ? finnAktiv() : -1;
    kortene.forEach(function (k, i) { k.classList.toggle('fokus', i === aktiv); });
    forrige.disabled = aktiv <= 0;
    neste.disabled = aktiv >= kortene.length - 1;
  }
  function gaaTil(i) {
    var k = kortene[i];
    rad.scrollTo({ left: k.offsetLeft - parseFloat(getComputedStyle(rad).paddingLeft), behavior: 'smooth' });
  }
  forrige.addEventListener('click', function () { if (aktiv > 0) gaaTil(aktiv - 1); });
  neste.addEventListener('click', function () { if (aktiv < kortene.length - 1) gaaTil(aktiv + 1); });
  var venter = false;
  rad.addEventListener('scroll', function () {
    if (venter) return; venter = true;
    requestAnimationFrame(function () { oppdater(); venter = false; });
  }, { passive: true });
  window.addEventListener('resize', oppdater);
  oppdater();
})();

// Nyhetsbrev → Brevo.
// Skjemaet sender navn og e-post rett til Brevo-skjemaet «Nettside».
// I Brevo lagres navnet i feltet FIRSTNAME, e-posten i EMAIL.
// Etter påmelding byttes skjemaet ut med en bekreftelse på samme sted.
(function () {
  var BREVO_ADRESSE = 'https://b4f1279e.sibforms.com/serve/MUIFADoYLq1dqSA9n7HtY3Y26w3z2tjc7B2vIFuB-YmtEwrnaNvj2bMzEK6bQj7RcmZT-tGB7WSptkk8k6DNnKfKuLD0uT6nJErKgNnjNk1tmnZAPU8JuKXfwUM_P2RAtXuByCIN7USNrlnCuhWwmFIOIsKJGcWLb_YwZNnDRB2iVvhbwwT4J5QpA8RyT_XjOrJSk40VujB2Ly25ig==';
  var skjema = document.getElementById('paamelding');
  if (!skjema) return;
  var knapp = skjema.querySelector('button[type="submit"]');
  var feil = document.getElementById('skjema-feil');
  var bekreftelse = document.getElementById('bekreftelse');
  var epostFelt = document.getElementById('epost');
  var navnFelt = document.getElementById('navn');

  function visBekreftelse(epost) {
    document.getElementById('bekreftet-epost').textContent = epost;
    skjema.hidden = true;
    bekreftelse.hidden = false;
    bekreftelse.focus();
  }
  function visFeil(tekst) {
    feil.textContent = tekst;
    feil.hidden = false;
  }
  document.getElementById('ny-paamelding').addEventListener('click', function () {
    skjema.reset();
    bekreftelse.hidden = true;
    skjema.hidden = false;
    navnFelt.focus();
  });

  skjema.addEventListener('submit', function (e) {
    e.preventDefault();
    feil.hidden = true;
    var epost = epostFelt.value.trim();
    var data = new FormData();
    data.append('EMAIL', epost);
    data.append('FIRSTNAME', navnFelt.value.trim());
    data.append('email_address_check', '');   // felle for roboter, skal være tom
    data.append('locale', 'nb');
    data.append('html_type', 'simple');

    knapp.setAttribute('aria-busy', 'true'); knapp.disabled = true;
    fetch(BREVO_ADRESSE, { method: 'POST', body: data })
      .then(function (svar) {
        return svar.json().catch(function () { return { success: svar.ok }; });
      })
      .then(function (svar) {
        if (svar && svar.success) visBekreftelse(epost);
        else visFeil('Noe ser ikke helt riktig ut. Sjekk at e-postadressen er skrevet riktig, og prøv igjen.');
      })
      .catch(function () {
        // Nettleseren fikk ikke lese svaret fra Brevo (CORS). Send på nytt uten å lese svaret;
        // Brevo lagrer hver e-post bare én gang, så dobbel innsending er ufarlig.
        return fetch(BREVO_ADRESSE, { method: 'POST', body: data, mode: 'no-cors' })
          .then(function () { visBekreftelse(epost); })
          .catch(function () {
            visFeil('Vi fikk ikke lagret påmeldingen din. Prøv igjen litt senere, eller send en e-post til post@taragot.no.');
          });
      })
      .finally(function () {
        knapp.removeAttribute('aria-busy'); knapp.disabled = false;
      });
  });
})();
