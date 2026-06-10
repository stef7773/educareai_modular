import json
import random

# ============================================
# KONFIGURACIJA
# ============================================
BROJ_KLJUČNIH_RIJEČI = 10000

# ============================================
# TEME NA HRVATSKOM
# ============================================
teme = {
    "matematika": {
        "teme": ["matematika", "kalkulus", "algebra", "geometrija", "trigonometrija", 
                   "statistika", "vjerojatnost", "derivacije", "integrali", "limesi", 
                   "funkcije", "matrice", "vektori", "jednadžbe", "logaritmi", 
                   "razlomci", "postoci", "korijeni", "potencije", "polinomi", 
                   "kompleksni brojevi", "diferencijalne jednadžbe", "linearna algebra",
                   "sferna trigonometrija", "vektorski kalkulus", "topologija", "teorija brojeva"]
    },
    "fizika": {
        "teme": ["fizika", "mehanika", "termodinamika", "elektromagnetizam", "optika", 
                   "akustika", "kinematika", "dinamika", "tekućine", "kvantna fizika", 
                   "teorija relativnosti", "energija", "rad", "snaga", "gibanje", 
                   "sile", "gravitacija", "elektricitet", "magnetizam", "valovi",
                   "astrofizika", "kozmologija", "nuklearna fizika", "molekularna fizika"]
    },
    "kemija": {
        "teme": ["kemija", "organska kemija", "anorganska kemija", "analitička kemija", 
                   "biokemija", "kemijske reakcije", "balansiranje", "stehiometrija", 
                   "periodni sustav", "kemijske veze", "molekule", "atomi", 
                   "kemijski spojevi", "kiseline", "baze", "ph", "otopine", 
                   "plinovi", "termokemija", "kvantna kemija", "elektrokemija"]
    },
    "biologija": {
        "teme": ["biologija", "stanična biologija", "molekularna biologija", "genetika", 
                   "anatomija", "fiziologija", "ekologija", "evolucija", "botanika", 
                   "zoologija", "mikrobiologija", "dna", "rna", "proteini", "enzimi", 
                   "metabolizam", "stanice", "tkiva", "organi", "tjelesni sustavi",
                   "neuroznanost", "imunologija", "embriologija"]
    },
    "programiranje": {
        "teme": ["programiranje", "python", "javascript", "java", "c++", "c#", "php", 
                   "ruby", "swift", "kotlin", "go", "rust", "html", "css", "sql", 
                   "mongodb", "git", "react", "angular", "vue", "nodejs", "django",
                   "flask", "spring boot", "laravel", "typescript", "graphql"]
    },
    "umjetna_inteligencija": {
        "teme_posebne": ["strojeno učenje", "duboko učenje", "gpt", "llm"],
        "teme": ["umjetna inteligencija", "neuronske mreže", "obrada prirodnog jezika", 
                   "računalni vid", "chatbotovi", "transformatori", "automatizacija",
                   "strojeno učenje", "duboko učenje", "obrada prirodnog jezika", "računalni vid"]
    },
    "cybersigurnost": {
        "teme": ["cybersigurnost", "etičko hakiranje", "vatreni zidovi", "šifriranje", 
                   "informacijska sigurnost", "penetracijsko testiranje", "zlonamjerni softver", "softver za ucjenu", 
                   "phishing", "socijalni inženjering", "kriptografija", "mrežna sigurnost",
                   "web sigurnost", "mobilna sigurnost", "etičko hakiranje"]
    },
    "kuhanje": {
        "teme": ["kuhanje", "jednostavni recepti", "deserti", "pečenje", "peciva", 
                   "meksička kuhinja", "talijanska kuhinja", "španjolska kuhinja", "pića", 
                   "kokteli", "kokteli", "sparivanje vina", "vino", "craft pivo",
                   "molekularna gastronomija", "vegetarijansko kuhanje", "vegansko kuhanje"]
    },
    "sport": {
        "teme": ["sport", "nogomet", "košarka", "tenis", "plivanje", "trčanje", 
                   "fitness", "teretana", "joga", "pilates", "crossfit", "sportska prehrana",
                   "funkcionalni trening", "kalistenika", "boks", "borilačke vještine"]
    },
    "poslovanje": {
        "teme": ["poslovanje", "poduzetništvo", "startupi", "digitalni marketing", "prodaja", 
                   "osobne financije", "ulaganja", "online poslovanje", "e-trgovina", 
                   "logistika", "vodstvo", "upravljanje poslovanjem", "ljudski resursi",
                   "korisnička služba", "brendiranje", "seo", "sem", "email marketing"]
    }
}

# ============================================
# PREFIKSI
# ============================================
prefiksi = [
    "kako naučiti", "kako ovladati", "potpuni vodič", "tutorial", "tečaj",
    "ovladati", "razumjeti", "vježbati", "rješavati probleme", "vježbe",
    "uvod u", "osnovni koncepti", "priručnik", "teorija",
    "primjeri", "osnove", "savjeti za učenje", "resursi za učenje",
    "lekcije", "lekcije", "kako se poboljšati u", "kako koristiti"
]

# ============================================
# SUFIKSI
# ============================================
sufiksi = [
    "početnik", "srednji", "napredni", "profesionalni", "potpuni",
    "lak", "brz", "za početnike", "od nule", "korak po korak",
    "s vježbama", "online", "besplatan", "certificiran", "sveučilišna razina",
    "za djecu", "za odrasle", "intenzivan", "praktičan", "teorijski"
]

# ============================================
# PITANJA
# ============================================
pitanja = [
    "što je", "kako funkcionira", "za što služi", "gdje naučiti",
    "kada koristiti", "zašto je važno", "koje su prednosti",
    "koliko vremena je potrebno za učenje", "što mi treba za učenje"
]

# ============================================
# GENERIRANJE KLJUČNIH RIJEČI
# ============================================
ključne_riječi = set()

print("🔄 Generiranje hrvatskih ključnih riječi...")

for prefiks in prefiksi:
    for cat_data in teme.values():
        for tema in cat_data["teme"]:
            ključne_riječi.add(f"{prefiks} {tema}")
        for tema_posebna in cat_data.get("teme_posebne", []):
            ključne_riječi.add(f"{prefiks} {tema_posebna}")

for sufiks in sufiksi:
    for cat_data in teme.values():
        for tema in cat_data["teme"][:15]:
            ključne_riječi.add(f"{tema} {sufiks}")
        for tema_posebna in cat_data.get("teme_posebne", []):
            ključne_riječi.add(f"{tema_posebna} {sufiks}")

for pitanje in pitanja:
    for cat_data in teme.values():
        for tema in cat_data["teme"][:15]:
            ključne_riječi.add(f"{pitanje} {tema}")
        for tema_posebna in cat_data.get("teme_posebne", []):
            ključne_riječi.add(f"{pitanje} {tema_posebna}")

glagoli = ["nauči", "ovladaj", "vježbaj", "studiraj", "razumi", "primijeni"]
for glagol in glagoli:
    for cat_data in teme.values():
        for tema in cat_data["teme"][:15]:
            ključne_riječi.add(f"{glagol} {tema}")

for cat_data in teme.values():
    sve_teme = cat_data["teme"] + cat_data.get("teme_posebne", [])
    if len(sve_teme) >= 2:
        for _ in range(min(30, len(sve_teme) * 3)):
            tema1, tema2 = random.sample(sve_teme, 2)
            ključne_riječi.add(f"razlika između {tema1} i {tema2}")
            ključne_riječi.add(f"{tema1} protiv {tema2}")
            ključne_riječi.add(f"usporedba {tema1} i {tema2}")

for cat_data in teme.values():
    for tema in cat_data["teme"][:10]:
        ključne_riječi.add(f"česte pogreške u {tema}")
        ključne_riječi.add(f"kako izbjeći pogreške u {tema}")
        ključne_riječi.add(f"rješenje problema s {tema}")

razine = ["početnik", "srednji", "napredni", "profesionalni", "intenzivan"]
for razina in razine:
    for cat_data in teme.values():
        for tema in cat_data["teme"][:12]:
            ključne_riječi.add(f"{razina} tečaj {tema}")
            ključne_riječi.add(f"{tema} {razina} razina lekcije")

for cat_data in teme.values():
    for tema in cat_data["teme"][:10]:
        ključne_riječi.add(f"certifikacija u {tema}")
        ključne_riječi.add(f"ispit iz {tema}")
        ključne_riječi.add(f"knjige o {tema}")
        ključne_riječi.add(f"videozapisi o {tema}")

for cat_data in teme.values():
    for tema in cat_data["teme"][:10]:
        ključne_riječi.add(f"savjeti za {tema}")
        ključne_riječi.add(f"preporuke za poboljšanje u {tema}")

for i in range(1, 2000):
    cat_name = random.choice(list(teme.keys()))
    tema = random.choice(teme[cat_name]["teme"])
    ključne_riječi.add(f"{tema} lekcija {i}")
    ključne_riječi.add(f"{tema} poglavlje {i}")
    ključne_riječi.add(f"{tema} jedinica {i}")

# ============================================
# OGRANIČENJE
# ============================================
popis_ključnih_riječi = sorted(list(ključne_riječi))
random.shuffle(popis_ključnih_riječi)

if len(popis_ključnih_riječi) < BROJ_KLJUČNIH_RIJEČI:
    print(f"⚠ Samo {len(popis_ključnih_riječi)} ključnih riječi je generirano. Ponavljamo neke da bismo dosegli {BROJ_KLJUČNIH_RIJEČI}...")
    while len(popis_ključnih_riječi) < BROJ_KLJUČNIH_RIJEČI:
        popis_ključnih_riječi.extend(popis_ključnih_riječi[:min(1000, BROJ_KLJUČNIH_RIJEČI - len(popis_ključnih_riječi))])

konačne_ključne_riječi = popis_ključnih_riječi[:BROJ_KLJUČNIH_RIJEČI]
random.shuffle(konačne_ključne_riječi)

# ============================================
# SPREMANJE
# ============================================
with open('keywords/hr.json', 'w', encoding='utf-8') as f:
    json.dump(konačne_ključne_riječi, f, indent=2, ensure_ascii=False)

# ============================================
# IZVJEŠTAJ
# ============================================
print(f"\n✅ {len(konačne_ključne_riječi)} hrvatskih ključnih riječi je generirano")
print(f"📁 Spremljeno u: keywords/hr.json")
print(f"\n📊 Pregled (prvih 30 ključnih riječi):")
for i, kw in enumerate(konačne_ključne_riječi[:30]):
    print(f"   {i+1}. {kw}")
