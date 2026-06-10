import json
import random

# ============================================
# KONFIGURAATIO
# ============================================
AVAINSANOJEN_MÄÄRÄ = 10000

# ============================================
# AIHEET SUOMEKSI
# ============================================
aiheet = {
    "matematiikka": {
        "aiheet": ["matematiikka", "laskenta", "algebra", "geometria", "trigonometria", 
                   "tilastotiede", "todennäköisyys", "derivaatat", "integraalit", "rajat", 
                   "funktiot", "matriisit", "vektorit", "yhtälöt", "logaritmit", 
                   "murtoluvut", "prosentit", "juuret", "potenssit", "polynomit", 
                   "kompleksiluvut", "differentiaaliyhtälöt", "lineaarialgebra",
                   "pallotrigonometria", "vektorilaskenta", "topologia", "lukuteoria"]
    },
    "fysiikka": {
        "aiheet": ["fysiikka", "mekaniikka", "termodynamiikka", "sähkömagnetismi", "optiikka", 
                   "akustiikka", "kinematiikka", "dynamiikka", "nesteet", "kvanttifysiikka", 
                   "suhteellisuusteoria", "energia", "työ", "teho", "liike", 
                   "voimat", "painovoima", "sähkö", "magnetismi", "aallot",
                   "astrofysiikka", "kosmologia", "ydinfysiikka", "molekyylifysiikka"]
    },
    "kemia": {
        "aiheet": ["kemia", "orgaaninen kemia", "epäorgaaninen kemia", "analyyttinen kemia", 
                   "biokemia", "kemialliset reaktiot", "tasapainotus", "stökiometria", 
                   "jaksollinen järjestelmä", "kemialliset sidokset", "molekyylit", "atomit", 
                   "kemialliset yhdisteet", "hapot", "emäkset", "ph", "liuokset", 
                   "kaasut", "termokemia", "kvanttikemia", "sähkökemia"]
    },
    "biologia": {
        "aiheet": ["biologia", "solubiologia", "molekyylibiologia", "genetiikka", 
                   "anatomia", "fysiologia", "ekologia", "evoluutio", "kasvitiede", 
                   "eläintiede", "mikrobiologia", "dna", "rna", "proteiinit", "entsyymit", 
                   "aineenvaihdunta", "solut", "kudokset", "elimet", "kehon järjestelmät",
                   "neurotiede", "immunologia", "alkiontutkimus"]
    },
    "ohjelmointi": {
        "aiheet": ["ohjelmointi", "python", "javascript", "java", "c++", "c#", "php", 
                   "ruby", "swift", "kotlin", "go", "rust", "html", "css", "sql", 
                   "mongodb", "git", "react", "angular", "vue", "nodejs", "django",
                   "flask", "spring boot", "laravel", "typescript", "graphql"]
    },
    "tekoäly": {
        "aiheet_erityiset": ["koneoppiminen", "syväoppiminen", "gpt", "llm"],
        "aiheet": ["tekoäly", "neuroverkot", "luonnollisen kielen käsittely", 
                   "tietokonenäkö", "chatbotit", "transformaattorit", "automaatio",
                   "koneoppiminen", "syväoppiminen", "luonnollisen kielen käsittely", "tietokonenäkö"]
    },
    "tietoturva": {
        "aiheet": ["tietoturva", "eettinen hakkerointi", "palomuurit", "salaaminen", 
                   "tietoturva", "tunkeutumistestaus", "haittaohjelmat", "kiristysohjelmat", 
                   "tietojenkalastelu", "sosiaalinen manipulointi", "kryptografia", "verkkoturvallisuus",
                   "verkkoturvallisuus", "mobiiliturvallisuus", "eettinen hakkerointi"]
    },
    "ruoanlaitto": {
        "aiheet": ["ruoanlaitto", "helppoja reseptejä", "jälkiruoat", "leivonta", "leivonnaiset", 
                   "meksikolainen ruoka", "italialainen ruoka", "espanjalainen ruoka", "juomat", 
                   "cocktailit", "cocktailit", "viinin yhdistäminen", "viini", "käsityöläisolut",
                   "molekyyligastronomia", "kasvisruoanlaitto", "vegaaninen ruoanlaitto"]
    },
    "urheilu": {
        "aiheet": ["urheilu", "jalkapallo", "koripallo", "tennis", "uinti", "juoksu", 
                   "kuntoilu", "kuntosali", "jooga", "pilates", "crossfit", "urheiluravitsemus",
                   "toiminnallinen harjoittelu", "kehonpainoharjoittelu", "nyrkkeily", "kamppailulajit"]
    },
    "liiketoiminta": {
        "aiheet": ["liiketoiminta", "yrittäjyys", "startupit", "digitaalinen markkinointi", "myynti", 
                   "henkilökohtainen talous", "sijoittaminen", "verkkoliiketoiminta", "verkkokauppa", 
                   "logistiikka", "johtajuus", "liikkeenjohto", "henkilöstöhallinto",
                   "asiakaspalvelu", "brändäys", "seo", "sem", "sähköpostimarkkinointi"]
    }
}

# ============================================
# ETULIITTEET
# ============================================
etuliitteet = [
    "miten oppia", "miten hallita", "täydellinen opas", "opetusohjelma", "kurssi",
    "hallita", "ymmärtää", "harjoitella", "ratkaista ongelmia", "harjoituksia",
    "johdanto", "peruskäsitteet", "käsikirja", "teoria",
    "esimerkkejä", "perusteet", "vinkkejä oppimiseen", "resursseja opiskeluun",
    "oppitunteja", "oppitunteja", "miten parantaa", "miten käyttää"
]

# ============================================
# JÄLKILIITTEET
# ============================================
jälkiliitteet = [
    "aloittelija", "keskitaso", "edistynyt", "ammattilainen", "täydellinen",
    "helppo", "nopea", "aloittelijoille", "tyhjästä", "askel askeleelta",
    "harjoituksilla", "verkossa", "ilmainen", "sertifioitu", "yliopistotaso",
    "lapsille", "aikuisille", "tehostettu", "käytännöllinen", "teoreettinen"
]

# ============================================
# KYSYMYKSET
# ============================================
kysymykset = [
    "mikä on", "miten se toimii", "mihin sitä käytetään", "missä oppia",
    "milloin käyttää", "miksi se on tärkeää", "mitä hyötyjä on",
    "kuinka kauan oppiminen kestää", "mitä tarvitsen opiskeluun"
]

# ============================================
# AVAINSANOJEN LUONTI
# ============================================
avainsanat = set()

print("🔄 Luodaan suomalaisia avainsanoja...")

for etuliite in etuliitteet:
    for cat_data in aiheet.values():
        for aihe in cat_data["aiheet"]:
            avainsanat.add(f"{etuliite} {aihe}")
        for aihe_erityinen in cat_data.get("aiheet_erityiset", []):
            avainsanat.add(f"{etuliite} {aihe_erityinen}")

for jälkiliite in jälkiliitteet:
    for cat_data in aiheet.values():
        for aihe in cat_data["aiheet"][:15]:
            avainsanat.add(f"{aihe} {jälkiliite}")
        for aihe_erityinen in cat_data.get("aiheet_erityiset", []):
            avainsanat.add(f"{aihe_erityinen} {jälkiliite}")

for kysymys in kysymykset:
    for cat_data in aiheet.values():
        for aihe in cat_data["aiheet"][:15]:
            avainsanat.add(f"{kysymys} {aihe}")
        for aihe_erityinen in cat_data.get("aiheet_erityiset", []):
            avainsanat.add(f"{kysymys} {aihe_erityinen}")

verbit = ["opi", "hallitse", "harjoittele", "opiskele", "ymmärrä", "sovella"]
for verbi in verbit:
    for cat_data in aiheet.values():
        for aihe in cat_data["aiheet"][:15]:
            avainsanat.add(f"{verbi} {aihe}")

for cat_data in aiheet.values():
    kaikki_aiheet = cat_data["aiheet"] + cat_data.get("aiheet_erityiset", [])
    if len(kaikki_aiheet) >= 2:
        for _ in range(min(30, len(kaikki_aiheet) * 3)):
            aihe1, aihe2 = random.sample(kaikki_aiheet, 2)
            avainsanat.add(f"ero {aihe1}:n ja {aihe2}:n välillä")
            avainsanat.add(f"{aihe1} vs {aihe2}")
            avainsanat.add(f"vertailu {aihe1} ja {aihe2}")

for cat_data in aiheet.values():
    for aihe in cat_data["aiheet"][:10]:
        avainsanat.add(f"yleiset virheet kohteessa {aihe}")
        avainsanat.add(f"miten välttää virheitä kohteessa {aihe}")
        avainsanat.add(f"ratkaisu {aihe} ongelmiin")

tasot = ["aloittelija", "keskitaso", "edistynyt", "ammattilainen", "tehostettu"]
for taso in tasot:
    for cat_data in aiheet.values():
        for aihe in cat_data["aiheet"][:12]:
            avainsanat.add(f"{taso} {aihe} kurssi")
            avainsanat.add(f"{aihe} {taso} tason oppitunnit")

for cat_data in aiheet.values():
    for aihe in cat_data["aiheet"][:10]:
        avainsanat.add(f"sertifiointi {aihe}:ssa")
        avainsanat.add(f"{aihe} tentti")
        avainsanat.add(f"{aihe} kirjat")
        avainsanat.add(f"{aihe} videot")

for cat_data in aiheet.values():
    for aihe in cat_data["aiheet"][:10]:
        avainsanat.add(f"vinkkejä {aihe}:een")
        avainsanat.add(f"neuvoja parantaa {aihe}:ssa")

for i in range(1, 2000):
    cat_name = random.choice(list(aiheet.keys()))
    aihe = random.choice(aiheet[cat_name]["aiheet"])
    avainsanat.add(f"{aihe} oppitunti {i}")
    avainsanat.add(f"{aihe} luku {i}")
    avainsanat.add(f"{aihe} yksikkö {i}")

# ============================================
# RAJOITA
# ============================================
avainsana_lista = sorted(list(avainsanat))
random.shuffle(avainsana_lista)

if len(avainsana_lista) < AVAINSANOJEN_MÄÄRÄ:
    print(f"⚠ Vain {len(avainsana_lista)} avainsanaa luotu. Toistetaan joitakin saavuttaaksemme {AVAINSANOJEN_MÄÄRÄ}...")
    while len(avainsana_lista) < AVAINSANOJEN_MÄÄRÄ:
        avainsana_lista.extend(avainsana_lista[:min(1000, AVAINSANOJEN_MÄÄRÄ - len(avainsana_lista))])

lopulliset_avainsanat = avainsana_lista[:AVAINSANOJEN_MÄÄRÄ]
random.shuffle(lopulliset_avainsanat)

# ============================================
# TALLENNA
# ============================================
with open('keywords/fi.json', 'w', encoding='utf-8') as f:
    json.dump(lopulliset_avainsanat, f, indent=2, ensure_ascii=False)

# ============================================
# RAPORTTI
# ============================================
print(f"\n✅ {len(lopulliset_avainsanat)} suomalaista avainsanaa luotu")
print(f"📁 Tallennettu: keywords/fi.json")
print(f"\n📊 Esikatselu (30 ensimmäistä avainsanaa):")
for i, kw in enumerate(lopulliset_avainsanat[:30]):
    print(f"   {i+1}. {kw}")
