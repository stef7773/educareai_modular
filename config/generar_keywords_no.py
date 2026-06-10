import json
import random

# ============================================
# KONFIGURASJON
# ============================================
ANTALL_NØKKELORD = 10000

# ============================================
# EMNER PÅ NORSK
# ============================================
emner = {
    "matematikk": {
        "emner": ["matematikk", "kalkulus", "algebra", "geometri", "trigonometri", 
                   "statistikk", "sannsynlighet", "deriverte", "integraler", "grenser", 
                   "funksjoner", "matriser", "vektorer", "likninger", "logaritmer", 
                   "brøker", "prosent", "røtter", "potenser", "polynomer", 
                   "komplekse tall", "differensiallikninger", "lineær algebra",
                   "sfærisk trigonometri", "vektorregning", "topologi", "tallteori"]
    },
    "fysikk": {
        "emner": ["fysikk", "mekanikk", "termodynamikk", "elektromagnetisme", "optikk", 
                   "akustikk", "kinematikk", "dynamikk", "væsker", "kvantefysikk", 
                   "relativitetsteori", "energi", "arbeid", "effekt", "bevegelse", 
                   "krefter", "tyngdekraft", "elektrisitet", "magnetisme", "bølger",
                   "astrofysikk", "kosmologi", "kjernefysikk", "molekylærfysikk"]
    },
    "kjemi": {
        "emner": ["kjemi", "organisk kjemi", "uorganisk kjemi", "analytisk kjemi", 
                   "biokjemi", "kjemiske reaksjoner", "balansering", "støkiometri", 
                   "periodesystemet", "kjemiske bindinger", "molekyler", "atomer", 
                   "kjemiske forbindelser", "syrer", "baser", "ph", "løsninger", 
                   "gasser", "termokjemi", "kvantekjemi", "elektrokjemi"]
    },
    "biologi": {
        "emner": ["biologi", "cellebiologi", "molekylærbiologi", "genetikk", 
                   "anatomi", "fysiologi", "økologi", "evolusjon", "botanikk", 
                   "zoologi", "mikrobiologi", "dna", "rna", "proteiner", "enzymer", 
                   "metabolisme", "celler", "vev", "organer", "kroppssystemer",
                   "nevrovitenskap", "immunologi", "embryologi"]
    },
    "programmering": {
        "emner": ["programmering", "python", "javascript", "java", "c++", "c#", "php", 
                   "ruby", "swift", "kotlin", "go", "rust", "html", "css", "sql", 
                   "mongodb", "git", "react", "angular", "vue", "nodejs", "django",
                   "flask", "spring boot", "laravel", "typescript", "graphql"]
    },
    "kunstig_intelligens": {
        "emner_spesielle": ["maskinlæring", "dyp læring", "gpt", "llm"],
        "emner": ["kunstig intelligens", "nevrale nettverk", "naturlig språkbehandling", 
                   "datasyn", "chatboter", "transformatorer", "automatisering",
                   "maskinlæring", "dyp læring", "naturlig språkbehandling", "datasyn"]
    },
    "cybersikkerhet": {
        "emner": ["cybersikkerhet", "etisk hacking", "brannmurer", "kryptering", 
                   "informasjonssikkerhet", "penetrasjonstesting", "skadelig programvare", "løsepengeprogramvare", 
                   "phishing", "sosial manipulering", "kryptografi", "nettverkssikkerhet",
                   "netsikkerhet", "mobil sikkerhet", "etisk hacking"]
    },
    "matlaging": {
        "emner": ["matlaging", "enkle oppskrifter", "desserter", "baking", "bakverk", 
                   "meksikansk mat", "italiensk mat", "spansk mat", "drikkevarer", 
                   "cocktailer", "cocktailer", "vinparing", "vin", "håndverksøl",
                   "molekylær gastronomi", "vegetarisk matlaging", "vegansk matlaging"]
    },
    "sport": {
        "emner": ["sport", "fotball", "basketball", "tennis", "svømming", "løping", 
                   "fitness", "treningssenter", "yoga", "pilates", "crossfit", "sportsernæring",
                   "funksjonell trening", "kroppsvektstrening", "boksing", "kampsport"]
    },
    "forretning": {
        "emner": ["forretning", "entreprenørskap", "oppstartsbedrifter", "digital markedsføring", "salg", 
                   "personlig økonomi", "investeringer", "nettbasert forretning", "e-handel", 
                   "logistikk", "lederskap", "bedriftsledelse", "menneskelige ressurser",
                   "kundeservice", "merkevarebygging", "seo", "sem", "e-postmarkedsføring"]
    }
}

# ============================================
# PREFIKSER
# ============================================
prefikser = [
    "hvordan lære", "hvordan mestre", "fullstendig guide til", "veiledning om", "kurs i",
    "mestre", "forstå", "øve", "løse problemer med", "øvelser i",
    "introduksjon til", "grunnleggende konsepter i", "håndbok for", "teori om",
    "eksempler på", "grunnleggende om", "tips for å lære", "ressurser for å studere",
    "leksjoner i", "leksjoner i", "hvordan forbedre seg i", "hvordan bruke"
]

# ============================================
# SUFFIKSER
# ============================================
suffikser = [
    "nybegynner", "mellomnivå", "avansert", "profesjonell", "komplett",
    "enkel", "rask", "for nybegynnere", "fra bunnen", "trinn for trinn",
    "med øvelser", "online", "gratis", "sertifisert", "universitetsnivå",
    "for barn", "for voksne", "intensiv", "praktisk", "teoretisk"
]

# ============================================
# SPØRSMÅL
# ============================================
spørsmål = [
    "hva er", "hvordan fungerer", "hva brukes det til", "hvor lærer man",
    "når skal man bruke", "hvorfor er det viktig", "hva er fordelene med",
    "hvor lang tid tar det å lære", "hva trenger jeg for å studere"
]

# ============================================
# GENERER NØKKELORD
# ============================================
nøkkelord = set()

print("🔄 Genererer norske nøkkelord...")

for prefiks in prefikser:
    for cat_data in emner.values():
        for emne in cat_data["emner"]:
            nøkkelord.add(f"{prefiks} {emne}")
        for emne_spesiell in cat_data.get("emner_spesielle", []):
            nøkkelord.add(f"{prefiks} {emne_spesiell}")

for suffiks in suffikser:
    for cat_data in emner.values():
        for emne in cat_data["emner"][:15]:
            nøkkelord.add(f"{emne} {suffiks}")
        for emne_spesiell in cat_data.get("emner_spesielle", []):
            nøkkelord.add(f"{emne_spesiell} {suffiks}")

for spørsmål in spørsmål:
    for cat_data in emner.values():
        for emne in cat_data["emner"][:15]:
            nøkkelord.add(f"{spørsmål} {emne}")
        for emne_spesiell in cat_data.get("emner_spesielle", []):
            nøkkelord.add(f"{spørsmål} {emne_spesiell}")

verb = ["lær", "mestrer", "øv", "studer", "forstå", "anvend"]
for v in verb:
    for cat_data in emner.values():
        for emne in cat_data["emner"][:15]:
            nøkkelord.add(f"{v} {emne}")

for cat_data in emner.values():
    alle_emner = cat_data["emner"] + cat_data.get("emner_spesielle", [])
    if len(alle_emner) >= 2:
        for _ in range(min(30, len(alle_emner) * 3)):
            emne1, emne2 = random.sample(alle_emner, 2)
            nøkkelord.add(f"forskjell mellom {emne1} og {emne2}")
            nøkkelord.add(f"{emne1} vs {emne2}")
            nøkkelord.add(f"sammenligning {emne1} og {emne2}")

for cat_data in emner.values():
    for emne in cat_data["emner"][:10]:
        nøkkelord.add(f"vanlige feil i {emne}")
        nøkkelord.add(f"hvordan unngå feil i {emne}")
        nøkkelord.add(f"løsning på problemer med {emne}")

nivåer = ["nybegynner", "mellom", "avansert", "profesjonell", "intensiv"]
for nivå in nivåer:
    for cat_data in emner.values():
        for emne in cat_data["emner"][:12]:
            nøkkelord.add(f"{nivå} kurs i {emne}")
            nøkkelord.add(f"{emne} {nivå} nivå leksjoner")

for cat_data in emner.values():
    for emne in cat_data["emner"][:10]:
        nøkkelord.add(f"sertifisering i {emne}")
        nøkkelord.add(f"eksamen i {emne}")
        nøkkelord.add(f"bøker om {emne}")
        nøkkelord.add(f"videoer om {emne}")

for cat_data in emner.values():
    for emne in cat_data["emner"][:10]:
        nøkkelord.add(f"tips for {emne}")
        nøkkelord.add(f"råd for å forbedre seg i {emne}")

for i in range(1, 2000):
    cat_name = random.choice(list(emner.keys()))
    emne = random.choice(emner[cat_name]["emner"])
    nøkkelord.add(f"{emne} leksjon {i}")
    nøkkelord.add(f"{emne} kapittel {i}")
    nøkkelord.add(f"{emne} enhet {i}")

# ============================================
# BEGRENS
# ============================================
nøkkelord_liste = sorted(list(nøkkelord))
random.shuffle(nøkkelord_liste)

if len(nøkkelord_liste) < ANTALL_NØKKELORD:
    print(f"⚠ Kun {len(nøkkelord_liste)} nøkkelord generert. Gjentakelse noen for å nå {ANTALL_NØKKELORD}...")
    while len(nøkkelord_liste) < ANTALL_NØKKELORD:
        nøkkelord_liste.extend(nøkkelord_liste[:min(1000, ANTALL_NØKKELORD - len(nøkkelord_liste))])

endelige_nøkkelord = nøkkelord_liste[:ANTALL_NØKKELORD]
random.shuffle(endelige_nøkkelord)

# ============================================
# LAGRE
# ============================================
with open('keywords/no.json', 'w', encoding='utf-8') as f:
    json.dump(endelige_nøkkelord, f, indent=2, ensure_ascii=False)

# ============================================
# RAPPORT
# ============================================
print(f"\n✅ {len(endelige_nøkkelord)} norske nøkkelord generert")
print(f"📁 Lagret i: keywords/no.json")
print(f"\n📊 Forhåndsvisning (første 30 nøkkelord):")
for i, kw in enumerate(endelige_nøkkelord[:30]):
    print(f"   {i+1}. {kw}")
