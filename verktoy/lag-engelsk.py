"""
Lager de engelske sidene i en/ fra de norske sidene.

Kjør etter hver endring i en norsk side:   python3 verktoy/lag-engelsk.py
Albumtitler, artistnavn, navn, e-post og telefon oversettes ikke.
Hver tekst som skal byttes, MÅ finnes i den norske siden, ellers stopper
skriptet og sier hvilken tekst som mangler (slik at ingenting blir glemt).
"""
import os, sys

ROT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXT_NO = '<span class="sr-only"> (åpnes i ny fane)</span>'
EXT_EN = '<span class="sr-only"> (opens in a new tab)</span>'

SIDER = {  # norsk fil -> engelsk fil
    'index.html': 'index.html',
    'katalog.html': 'catalogue.html',
    'om-oss.html': 'about.html',
    'personvern.html': 'privacy.html',
}

# Tekst som er lik på alle sider (meny, footer, nyhetsbrev, kort)
FELLES = [
    ('<html lang="nb">', '<html lang="en">'),
    ('aria-label="Taragot Sounds — til forsiden"', 'aria-label="Taragot Sounds — home"'),
    ('aria-label="Hovedmeny"', 'aria-label="Main menu"'),
    ('>Katalog</a>', '>Catalogue</a>'),
    ('>Om oss</a>', '>About</a>'),
    ('>Kontakt</a>', '>Contact</a>'),
    ('Butikk&nbsp;<span aria-hidden="true">↗</span><span class="sr-only"> på Bandcamp (åpnes i ny fane)</span>',
     'Shop&nbsp;<span aria-hidden="true">↗</span><span class="sr-only"> on Bandcamp (opens in a new tab)</span>'),
    ('<span class="sr-only">Språk: </span>NO', '<span class="sr-only">Language: </span>EN'),
    ('aria-label="Åpne meny"', 'aria-label="Open menu"'),
    ('aria-label="Til toppen"', 'aria-label="Back to top"'),
    ('<h2 class="tittel">Kontakt oss</h2>', '<h2 class="tittel">Contact us</h2>'),
    ('<h3>Generelle henvendelser</h3>', '<h3>General enquiries</h3>'),
    ('<h3>Adresse</h3>', '<h3>Address</h3>'),
    ('<h3>Følg oss</h3>', '<h3>Follow us</h3>'),
    ('Org. nr. 997 677 897', 'Org. no. 997 677 897'),
    (' – hør på Bandcamp (åpnes i ny fane)', ' – listen on Bandcamp (opens in a new tab)'),
    (' – forhåndslytt på Bandcamp (åpnes i ny fane)', ' – pre-listen on Bandcamp (opens in a new tab)'),
    ('<span class="slipp-merke">Slippes 21. nov.</span>', '<span class="slipp-merke">Out 21 Nov</span>'),
    ('<a class="hopp" href="#innhold">Hopp til innhold</a>', '<a class="hopp" href="#innhold">Skip to content</a>'),
    ('<meta property="og:locale" content="nb_NO">', '<meta property="og:locale" content="en_GB">'),
    ('<a class="lenke" href="personvern.html" aria-current="page">Personvern</a>', '<a class="lenke" href="personvern.html" aria-current="page">Privacy</a>'),
    ('<a class="lenke" href="personvern.html">Personvern</a>', '<a class="lenke" href="personvern.html">Privacy</a>'),
    (EXT_NO, EXT_EN),
]

PER_SIDE = {
'index.html': [
    ('content="Norsk plateselskap med en katalog bestående av skandinavisk folkemusikk og tradisjonsmusikk, fri improvisasjon og samtidsjazz."',
     'content="Norwegian record label with a catalogue of Scandinavian folk and traditional music, free improvisation and contemporary jazz."'),
    ('''<h1>Norsk plateselskap med en katalog bestående av skandinavisk folkemusikk og
        tradisjonsmusikk, fri&nbsp;improvisasjon og samtidsjazz.</h1>''',
     '''<h1>Norwegian record label with a catalogue of Scandinavian folk and
        traditional music, free&nbsp;improvisation and contemporary jazz.</h1>'''),
    ('<h2 class="tittel">Nyeste utgivelser</h2>', '<h2 class="tittel">Latest releases</h2>'),
    ('aria-label="Forrige utgivelse"', 'aria-label="Previous release"'),
    ('aria-label="Neste utgivelse"', 'aria-label="Next release"'),
    ('>Se alle utgivelser\n', '>See all releases\n'),
    ('<h2 class="tittel">Nyhetsbrev</h2>', '<h2 class="tittel">Newsletter</h2>'),
    ('<p class="ingress">Få siste nytt om våre artister og utgivelser!</p>', '<p class="ingress">Get the latest news about our artists and releases!</p>'),
    ('<label for="navn">Ditt navn*</label>', '<label for="navn">Your name*</label>'),
    ('<label for="epost">Din e-post*</label>', '<label for="epost">Your email*</label>'),
    ('Vi bruker e-posten din bare til nyhetsbrevet. Du kan melde deg av når som helst. <a href="personvern.html">Personvern</a>',
     'We only use your email for the newsletter. You can unsubscribe at any time. <a href="personvern.html">Privacy</a>'),
    ('<button class="knapp" type="submit">Meld på\n', '<button class="knapp" type="submit">Subscribe\n'),
    ('<h3 class="bekreftelse-tittel">Takk, du er påmeldt!</h3>', '<h3 class="bekreftelse-tittel">Thank you, you’re subscribed!</h3>'),
    ('Vi sender nyheter om artister og utgivelser til <strong', 'We’ll send news about artists and releases to <strong'),
    ('>Meld på en annen e-post</button>', '>Subscribe another email</button>'),
],
'katalog.html': [
    ('<title>Katalog — Taragot Sounds</title>', '<title>Catalogue — Taragot Sounds</title>'),
    ('content="Katalog — Taragot Sounds"', 'content="Catalogue — Taragot Sounds"'),
    ('content="Alle utgivelser fra Taragot Sounds."', 'content="All releases from Taragot Sounds."'),
    ('<h1 class="sidetittel">Katalog</h1>', '<h1 class="sidetittel">Catalogue</h1>'),
    ('id="alle-utgivelser">Alle utgivelser</h2>', 'id="alle-utgivelser">All releases</h2>'),
    ('<span class="sr-only">Søk i katalogen</span>', '<span class="sr-only">Search the catalogue</span>'),
    ('placeholder="Søk etter album eller artist"', 'placeholder="Search for an album or artist"'),
    ('aria-label="Tøm søket"', 'aria-label="Clear search"'),
],
'om-oss.html': [
    ('<title>Om oss — Taragot Sounds</title>', '<title>About — Taragot Sounds</title>'),
    ('content="Om oss — Taragot Sounds"', 'content="About — Taragot Sounds"'),
    ('content="Taragot Sounds er et uavhengig norsk plateselskap etablert i 2014."', 'content="Taragot Sounds is an independent Norwegian record label founded in 2014."'),
    ('<h1 class="sidetittel">Om oss</h1>', '<h1 class="sidetittel">About</h1>'),
    ('id="menneskene">Menneskene bak</h2>', 'id="menneskene">The people behind it</h2>'),
    ('<p>Grunnlegger. Musiker, produsent og folkemusikkforsker</p>', '<p>Founder. Musician, producer and folk music researcher</p>'),
    ('<p>Komponist, fele- og hardingfelespiller</p>', '<p>Composer, fiddle and Hardanger fiddle player</p>'),
    ('<p>Komponist, trommeslager og vibrafonist</p>', '<p>Composer, drummer and vibraphonist</p>'),
    ('<h2 class="tittel">Historien</h2>', '<h2 class="tittel">Our story</h2>'),
    ('<p>Taragot Sounds er et uavhengig norsk plateselskap etablert i 2014 av musiker, produsent og folkemusikkforsker Tellef Kvifte. Selskapet ble opprinnelig startet som en plattform for prosjektene til Tellef, Guro Kvifte Nesheim (komponist, fele- og hardingfelespiller) og Knut Kvifte Nesheim (komponist, trommeslager og vibrafonist). Sammen har de bygget et selskap som utgir tradisjonsmusikk, folkemusikk, samtidsjazz og fri improvisasjon, med et musikalsk uttrykk som spenner fra akustisk til elektronisk, og fra tradisjonelt til eksperimentelt.</p>',
     '<p>Taragot Sounds is an independent Norwegian record label founded in 2014 by musician, producer and folk music researcher Tellef Kvifte. The label was originally set up as a platform for the projects of Tellef, Guro Kvifte Nesheim (composer, fiddle and Hardanger fiddle player) and Knut Kvifte Nesheim (composer, drummer and vibraphonist). Together they have built a label that releases traditional music, folk music, contemporary jazz and free improvisation, with a musical expression that ranges from acoustic to electronic, and from traditional to experimental.</p>'),
    ('<p>Etter hvert har også en større krets av medmusikanter og venner blitt involvert, og i dag teller katalogen nærmere 50 utgivelser. Felles for alle utgivelsene er et musikalsk tvisyn med blikk for både røtter og nyskaping.</p>',
     '<p>Over time, a wider circle of fellow musicians and friends has joined in, and today the catalogue counts close to 50 releases. What they all share is a musical double vision, with an eye for both roots and renewal.</p>'),
    ('<p>Navnet Taragot er hentet fra det østeuropeiske blåseinstrumentet tárogató, som har røtter i rumensk og ungarsk folkemusikk, men også brukt av kjente jazzmusikere som Charles Lloyd og Joe Lovano. På samme måte som instrumentet, favner Taragot Sounds musikk i spenningsfeltet mellom tradisjon og samtid.</p>',
     '<p>The name Taragot comes from the Eastern European wind instrument tárogató, which has its roots in Romanian and Hungarian folk music, but has also been played by renowned jazz musicians such as Charles Lloyd and Joe Lovano. Like the instrument, Taragot Sounds embraces music in the space between tradition and the contemporary.</p>'),
    ('<p>Alle utgivelser er til salgs på <a', '<p>All releases are for sale on <a'),
    (', og tilgjengelig på alle strømmetjenester.</p>', ', and available on every streaming service.</p>'),
    ('<div class="bilde-plass">Portrett<img', '<div class="bilde-plass">Portrait<img'),
],
'personvern.html': [
    ('<title>Personvern — Taragot Sounds</title>', '<title>Privacy — Taragot Sounds</title>'),
    ('content="Personvern — Taragot Sounds"', 'content="Privacy — Taragot Sounds"'),
    ('content="Slik behandler Taragot Sounds personopplysninger."', 'content="How Taragot Sounds handles personal data."'),
    ('<h1 class="sidetittel">Personvern</h1>', '<h1 class="sidetittel">Privacy</h1>'),
    ('<p>Her forklarer vi hvilke personopplysninger Taragot Sounds samler inn gjennom denne nettsiden, hva vi bruker dem til, og hvilke rettigheter du har.</p>',
     '<p>This page explains what personal data Taragot Sounds collects through this website, what we use it for, and what rights you have.</p>'),
    ('<h2>Hvem er ansvarlig</h2>', '<h2>Who is responsible</h2>'),
    ('<p>Taragot Sounds er ansvarlig for personopplysningene som samles inn på denne nettsiden. Du kan kontakte oss på <a',
     '<p>Taragot Sounds is responsible for the personal data collected on this website. You can contact us at <a'),
    ('</a> eller i Skedsmogata 5, 0655 Oslo.</p>', '</a> or at Skedsmogata 5, 0655 Oslo, Norway.</p>'),
    ('<h2>Nyhetsbrevet</h2>', '<h2>The newsletter</h2>'),
    ('<p>Når du melder deg på nyhetsbrevet, lagrer vi navnet og e-postadressen din. Vi bruker dem bare til å sende deg nyheter om våre artister og utgivelser. Grunnlaget er ditt samtykke, som du gir når du melder deg på.</p>',
     '<p>When you subscribe to the newsletter, we store your name and email address. We only use them to send you news about our artists and releases. The legal basis is your consent, which you give when you subscribe.</p>'),
    ('<p>Opplysningene lagres hos Brevo, tjenesten vi bruker til å sende nyhetsbrev. Brevo behandler opplysningene på våre vegne og lagrer dem i EU. Vi deler dem ikke med andre.</p>',
     '<p>The data is stored with Brevo, the service we use to send newsletters. Brevo processes the data on our behalf and stores it in the EU. We do not share it with anyone else.</p>'),
    ('<p>Vi tar vare på opplysningene til du melder deg av. Du kan melde deg av når som helst med lenken nederst i hvert nyhetsbrev, eller ved å sende oss en e-post.</p>',
     '<p>We keep the data until you unsubscribe. You can unsubscribe at any time using the link at the bottom of every newsletter, or by sending us an email.</p>'),
    ('<h2>Når du besøker nettsiden</h2>', '<h2>When you visit the website</h2>'),
    ('<p>Vi bruker ingen informasjonskapsler (cookies) og ingen verktøy for å spore eller analysere besøk.</p>',
     '<p>We do not use cookies or any tools to track or analyse visits.</p>'),
    ('<p>Nettsiden ligger hos GitHub Pages, som registrerer IP-adressen din i tekniske logger for å holde tjenesten sikker. Noen av albumcoverne vises direkte fra Bandcamp, og da får også Bandcamp vite IP-adressen din.</p>',
     '<p>The website is hosted by GitHub Pages, which records your IP address in technical logs to keep the service secure. Some of the album covers are shown directly from Bandcamp, which means Bandcamp also receives your IP address.</p>'),
    ('<p>Når du følger en lenke til Bandcamp, Instagram eller Facebook, gjelder personvernreglene til den tjenesten.</p>',
     '<p>When you follow a link to Bandcamp, Instagram or Facebook, that service’s privacy policy applies.</p>'),
    ('<h2>Dine rettigheter</h2>', '<h2>Your rights</h2>'),
    ('<p>Du har rett til å få vite hvilke opplysninger vi har om deg, og til å få dem rettet eller slettet. Du kan også trekke tilbake samtykket ditt når som helst. Send oss en e-post på <a',
     '<p>You have the right to know what data we hold about you, and to have it corrected or deleted. You can also withdraw your consent at any time. Send us an email at <a'),
    ('</a>, så hjelper vi deg.</p>', '</a> and we will help you.</p>'),
    ('<p>Mener du at vi behandler opplysningene dine i strid med reglene, kan du klage til <a', '<p>If you believe we are handling your data in breach of the rules, you can complain to the Norwegian Data Protection Authority, <a'),
    ('<p class="oppdatert">Sist oppdatert 11. november 2026.</p>', '<p class="oppdatert">Last updated 11 November 2026.</p>'),
],
}

# Lenker mellom sidene og stier til felles filer (en/ ligger én mappe ned)
STIER = [
    ('href="tokens.css"', 'href="../tokens.css"'),
    ('href="stil.css"', 'href="../stil.css"'),
    ('src="felles.js"', 'src="../felles.js"'),
    ('src="bilder/', 'src="../bilder/'),
    ('href="katalog.html"', 'href="catalogue.html"'),
    ('href="om-oss.html"', 'href="about.html"'),
    ('href="personvern.html"', 'href="privacy.html"'),
    ('href="favicon-32.png"', 'href="../favicon-32.png"'),
    ('href="apple-touch-icon.png"', 'href="../apple-touch-icon.png"'),
]

def sprakvelger(norsk, engelsk_fil, norsk_fil, er_engelsk):
    """Lenker i språkvelgeren og hreflang i <head>."""
    gammel = norsk[norsk.index('<ul class="sprak-liste"'):norsk.index('</ul>', norsk.index('<ul class="sprak-liste"'))+5]
    if er_engelsk:
        ny = ('<ul class="sprak-liste" id="sprak-liste" hidden>\n'
              f'          <li><a href="../{norsk_fil}" lang="nb" hreflang="nb">Norsk</a></li>\n'
              f'          <li><a href="{engelsk_fil}" lang="en" aria-current="true">English</a></li>\n'
              '        </ul>')
    else:
        ny = ('<ul class="sprak-liste" id="sprak-liste" hidden>\n'
              f'          <li><a href="{norsk_fil}" lang="nb" aria-current="true">Norsk</a></li>\n'
              f'          <li><a href="en/{engelsk_fil}" lang="en" hreflang="en">English</a></li>\n'
              '        </ul>')
    return gammel, ny

def bytt(tekst, par, fil):
    for gammel, ny in par:
        if gammel not in tekst:
            sys.exit(f'STOPP: fant ikke denne teksten i {fil}:\n  {gammel[:90]}')
        tekst = tekst.replace(gammel, ny)
    return tekst

os.makedirs(os.path.join(ROT, 'en'), exist_ok=True)
for norsk_fil, engelsk_fil in SIDER.items():
    sti = os.path.join(ROT, norsk_fil)
    norsk = open(sti, encoding='utf-8').read()

    # 1) Norsk side: riktig lenke til engelsk versjon
    g, n = sprakvelger(norsk, engelsk_fil, norsk_fil, er_engelsk=False)
    norsk = norsk.replace(g, n)
    open(sti, 'w', encoding='utf-8').write(norsk)

    # 2) Engelsk side
    en = norsk
    g, n = sprakvelger(norsk, engelsk_fil, norsk_fil, er_engelsk=True)
    en = en.replace(g, n)
    en = bytt(en, PER_SIDE[norsk_fil], norsk_fil)
    for gammel, ny in FELLES:
        en = en.replace(gammel, ny)
    en = bytt(en, [p for p in STIER if p[0] in en], norsk_fil)
    open(os.path.join(ROT, 'en', engelsk_fil), 'w', encoding='utf-8').write(en)
    print(f'{norsk_fil} -> en/{engelsk_fil}')
