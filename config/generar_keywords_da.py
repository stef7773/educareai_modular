import json
import random

# ============================================
# KONFIGURATION
# ============================================
ANTAL_NØGLEORD = 10000

# ============================================
# EMNER PÅ DANSK
# ============================================
emner = {
    "matematik": {
        "emner": ["matematik", "calculus", "algebra", "geometri", "trigonometri", 
                   "statistik", "sandsynlighed", "afledede", "integraler", "grænser", 
                   "funktioner", "matricer", "vektorer", "ligninger", "logaritmer", 
                   "brøker", "procent", "rødder", "potenser", "polynomier", 
                   "komplekse tal", "differentialligninger", "lineær algebra",
                   "sfærisk trigonometri", "vektorregning", "topologi", "talteori"]
    },
    "fysik": {
        "emner": ["fysik", "mekanik", "termodynamik", "elektromagnetisme", "optik", 
                   "akustik", "kinematik", "dynamik", "væsker", "kvantefysik", 
                   "relativitetsteori", "energi", "arbejde", "effekt", "bevægelse", 
                   "kræfter", "tyngdekraft", "elektricitet", "magnetisme", "bølger",
                   "astrofysik", "kosmologi", "kernefysik", "molekylærfysik"]
    },
    "kemi": {
        "emner": ["kemi", "organisk kemi", "uorganisk kemi", "analytisk kemi", 
                   "biokemi", "kemiske reaktioner", "balance", "stoikiometri", 
                   "periodiske system", "kemiske bindinger", "molekyler", "atomer", 
                   "kemiske forbindelser", "syrer", "baser", "ph", "opløsninger", 
                   "gasser", "termokemi", "kvantekemi", "elektrokemi"]
    },
    "biologi": {
        "emner": ["biologi", "cellebiologi", "molekylærbiologi", "genetik", 
                   "anatomi", "fysiologi", "økologi", "evolution", "botanik", 
                   "zoologi", "mikrobiologi", "dna", "rna", "proteiner", "enzymer", 
                   "metabolisme", "celler", "væv", "organer", "kropssystemer",
                   "neurovidenskab", "immunologi", "embryologi"]
    },
    "programmering": {
        "emner": ["programmering", "python", "javascript", "java", "c++", "c#", "php", 
                   "ruby", "swift", "kotlin", "go", "rust", "html", "css", "sql", 
                   "mongodb", "git", "react", "angular", "vue", "nodejs", "django",
                   "flask", "spring boot", "laravel", "typescript", "graphql"]
    },
    "kunstig_intelligens": {
        "emner_specielle": ["maskinlæring", "dyb læring", "gpt", "llm"],
        "emner": ["kunstig intelligens", "neurale netværk", "naturlig sprogbehandling", 
                   "computersyn", "chatbots", "transformatorer", "automatisering",
                   "maskinlæring", "dyb læring", "naturlig sprogbehandling", "computersyn"]
    },
    "cybersikkerhed": {
        "emner": ["cybersikkerhed", "etisk hacking", "firewalls", "kryptering", 
                   "informationssikkerhed", "penetrationstest", "malware", "ransomware", 
                   "phishing", "social manipulation", "kryptografi", "netværkssikkerhed",
                   "websikkerhed", "mobil sikkerhed", "etisk hacking"]
    },
    "madlavning": {
        "emner": ["madlavning", "nemme opskrifter", "desserter", "bagning", "bagværk", 
                   "mexicansk mad", "italiensk mad", "spansk mad", "drikkevarer", 
                   "cocktails", "cocktails", "vinparring", "vin", "håndværksøl",
                   "molekylær gastronomi", "vegetarisk madlavning", "vegansk madlavning"]
    },
    "sport": {
        "emner": ["sport", "fodbold", "basketball", "tennis", "svømning", "løb", 
                   "fitness", "træningscenter", "yoga", "pilates", "crossfit", "sportsernæring",
                   "funktionel træning", "kropsvægtstræning", "boksning", "kampsport"]
    },
    "forretning": {
        "emner": ["forretning", "iværksætteri", "startups", "digital markedsføring", "salg", 
                   "personlig økonomi", "investeringer", "online forretning", "e-handel", 
                   "logistik", "lederskab", "virksomhedsledelse", "human resources",
                   "kundeservice", "branding", "seo", "sem", "e-mail markedsføring"]
    }
}

# ============================================
# PRÆFIK SER
# ============================================
præfikser = [
    "hvordan man lærer", "hvordan man mestrer", "komplet guide til", "tutorial om", "kursus i",
    "mestre", "forstå", "øve", "løse problemer med", "øvelser i",
    "introduktion til", "grundlæggende koncepter i", "manual til", "teori om",
    "eksempler på", "grundlæggende om", "tips til at lære", "ressourcer til at studere",
    "lektioner i", "lektioner i", "hvordan man forbedrer sig i", "hvordan man bruger"
]

# ============================================
# SUFFIKSER
# ============================================
suffikser = [
    "begynder", "mellemniveau", "avanceret", "professionel", "komplet",
    "let", "hurtig", "for begyndere", "fra bunden", "trin for trin",
    "med øvelser", "online", "gratis", "certificeret", "universitetsniveau",
    "for børn", "for voksne", "intensiv", "praktisk", "teoretisk"
]

# ============================================
# SPØRGSMÅL
# ============================================
spørgsmål = [
    "hvad er", "hvordan fungerer", "hvad bruges det til", "hvor lærer man",
    "hvornår skal man bruge", "hvorfor er det vigtigt", "hvad er fordelene ved",
    "hvor lang tid tager det at lære", "hvad har jeg brug for at studere"
]

# ============================================
# GENERER NØGLEORD
# ============================================
nøgleord = set()

print("🔄 Genererer danske nøgleord...")

for præfiks in præfikser:
    for cat_data in emner.values():
        for emne in cat_data["emner"]:
            nøgleord.add(f"{præfiks} {emne}")
        for emne_speciel in cat_data.get("emner_specielle", []):
            nøgleord.add(f"{præfiks} {emne_speciel}")

for suffiks in suffikser:
    for cat_data in emner.values():
        for emne in cat_data["emner"][:15]:
            nøgleord.add(f"{emne} {suffiks}")
        for emne_speciel in cat_data.get("emner_specielle", []):
            nøgleord.add(f"{emne_speciel} {suffiks}")

for spørgsmål in spørgsmål:
    for cat_data in emner.values():
        for emne in cat_data["emner"][:15]:
            nøgleord.add(f"{spørgsmål} {emne}")
        for emne_speciel in cat_data.get("emner_specielle", []):
            nøgleord.add(f"{spørgsmål} {emne_speciel}")

verber = ["lær", "mestrer", "øv", "studér", "forstå", "anvend"]
for verbum in verber:
    for cat_data in emner.values():
        for emne in cat_data["emner"][:15]:
            nøgleord.add(f"{verbum} {emne}")

for cat_data in emner.values():
    alle_emner = cat_data["emner"] + cat_data.get("emner_specielle", [])
    if len(alle_emner) >= 2:
        for _ in range(min(30, len(alle_emner) * 3)):
            emne1, emne2 = random.sample(alle_emner, 2)
            nøgleord.add(f"forskel mellem {emne1} og {emne2}")
            nøgleord.add(f"{emne1} vs {emne2}")
            nøgleord.add(f"sammenligning {emne1} og {emne2}")

for cat_data in emner.values():
    for emne in cat_data["emner"][:10]:
        nøgleord.add(f"almindelige fejl i {emne}")
        nøgleord.add(f"hvordan man undgår fejl i {emne}")
        nøgleord.add(f"løsning på problemer med {emne}")

niveauer = ["begynder", "mellem", "avanceret", "professionel", "intensiv"]
for niveau in niveauer:
    for cat_data in emner.values():
        for emne in cat_data["emner"][:12]:
            nøgleord.add(f"{niveau} kursus i {emne}")
            nøgleord.add(f"{emne} {niveau} niveau lektioner")

for cat_data in emner.values():
    for emne in cat_data["emner"][:10]:
        nøgleord.add(f"certificering i {emne}")
        nøgleord.add(f"eksamen i {emne}")
        nøgleord.add(f"bøger om {emne}")
        nøgleord.add(f"videoer om {emne}")

for cat_data in emner.values():
    for emne in cat_data["emner"][:10]:
        nøgleord.add(f"tips til {emne}")
        nøgleord.add(f"råd til at forbedre sig i {emne}")

for i in range(1, 2000):
    cat_name = random.choice(list(emner.keys()))
    emne = random.choice(emner[cat_name]["emner"])
    nøgleord.add(f"{emne} lektion {i}")
    nøgleord.add(f"{emne} kapitel {i}")
    nøgleord.add(f"{emne} enhed {i}")

# ============================================
# BEGRÆNS
# ============================================
nøgleord_liste = sorted(list(nøgleord))
random.shuffle(nøgleord_liste)

if len(nøgleord_liste) < ANTAL_NØGLEORD:
    print(f"⚠ Kun {len(nøgleord_liste)} nøgleord genereret. Gentager nogle for at nå {ANTAL_NØGLEORD}...")
    while len(nøgleord_liste) < ANTAL_NØGLEORD:
        nøgleord_liste.extend(nøgleord_liste[:min(1000, ANTAL_NØGLEORD - len(nøgleord_liste))])

endelige_nøgleord = nøgleord_liste[:ANTAL_NØGLEORD]
random.shuffle(endelige_nøgleord)

# ============================================
# GEM
# ============================================
with open('keywords/da.json', 'w', encoding='utf-8') as f:
    json.dump(endelige_nøgleord, f, indent=2, ensure_ascii=False)

# ============================================
# RAPPORT
# ============================================
print(f"\n✅ {len(endelige_nøgleord)} danske nøgleord genereret")
print(f"📁 Gemt i: keywords/da.json")
print(f"\n📊 Forhåndsvisning (første 30 nøgleord):")
for i, kw in enumerate(endelige_nøgleord[:30]):
    print(f"   {i+1}. {kw}")
