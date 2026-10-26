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
  if (window.innerWidth > 767 && nav.classList.contains('nav--apen')) settMeny(false);
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

// Karusell (forsiden, mobil): kortet nærmest midten får fokus
(function () {
  var rad = document.querySelector('.karusell');
  if (!rad) return;
  var kortene = Array.prototype.slice.call(rad.querySelectorAll('.kort'));
  var forrige = document.getElementById('pil-forrige');
  var neste = document.getElementById('pil-neste');
  var aktiv = 0;
  function erKarusell() { return getComputedStyle(rad).display === 'flex'; }
  function finnAktiv() {
    var midt = rad.scrollLeft + rad.clientWidth / 2, best = 0, avstand = Infinity;
    kortene.forEach(function (k, i) {
      var d = Math.abs(k.offsetLeft + k.offsetWidth / 2 - midt);
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
    rad.scrollTo({ left: k.offsetLeft - (rad.clientWidth - k.offsetWidth) / 2, behavior: 'smooth' });
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

// Nyhetsbrev → 5b CRM.
// CRM_ADRESSE fylles inn når crm.5b.no har et åpent mottak for påmeldinger.
// Skjemaet sender da JSON: { navn, epost, kilde: "nettside" }.
(function () {
  var CRM_ADRESSE = '';
  var skjema = document.getElementById('paamelding');
  if (!skjema) return;
  var takk = document.getElementById('takk');
  skjema.addEventListener('submit', function (e) {
    e.preventDefault();
    takk.style.display = 'block';
    if (!CRM_ADRESSE) {
      takk.textContent = 'Takk! (Påmeldingen er ikke koblet til CRM-et ennå.)';
      return;
    }
    takk.textContent = 'Sender …';
    fetch(CRM_ADRESSE, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        navn: document.getElementById('navn').value,
        epost: document.getElementById('epost').value,
        kilde: 'nettside'
      })
    }).then(function (svar) {
      if (!svar.ok) throw new Error(svar.status);
      takk.textContent = 'Takk! Du er nå påmeldt nyhetsbrevet.';
      skjema.reset();
    }).catch(function () {
      takk.textContent = 'Noe gikk galt. Prøv igjen, eller send en e-post til post@taragot.no.';
    });
  });
})();
