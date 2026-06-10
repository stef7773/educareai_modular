import json
import random

# ============================================
# KONFIGURACIJA
# ============================================
ŠTEVILO_KLJUČNIH_BESED = 10000

# ============================================
# TEME V SLOVENŠČINI
# ============================================
teme = {
    "matematika": {
        "teme": ["matematika", "kalkulus", "algebra", "geometrija", "trigonometrija", 
                   "statistika", "verjetnost", "odvodi", "integrali", "limite", 
                   "funkcije", "matrike", "vektorji", "enačbe", "logaritmi", 
                   "ulomki", "odstotki", "korenine", "potence", "polinomi", 
                   "kompleksna števila", "diferencialne enačbe", "linearna algebra",
                   "sferična trigonometrija", "vektorski račun", "topologija", "teorija števil"]
    },
    "fizika": {
        "teme": ["fizika", "mehanika", "termodinamika", "elektromagnetizem", "optika", 
                   "akustika", "kinematika", "dinamika", "tekočine", "kvantna fizika", 
                   "teorija relativnosti", "energija", "delo", "moč", "gibanje", 
                   "sile", "gravitacija", "elektrika", "magnetizem", "valovi",
                   "astrofizika", "kozmologija", "jedrska fizika", "molekularna fizika"]
    },
    "kemija": {
        "teme": ["kemija", "organska kemija", "anorganska kemija", "analizna kemija", 
                   "biokemija", "kemične reakcije", "uravnoteženje", "stehiometrija", 
                   "periodni sistem", "kemične vezi", "molekule", "atom", 
                   "kemične spojine", "kisline", "baze", "ph", "raztopine", 
                   "plini", "termokemija", "kvantna kemija", "elektrokemija"]
    },
    "biologija": {
        "teme": ["biologija", "celična biologija", "molekularna biologija", "genetika", 
                   "anatomija", "fiziologija", "ekologija", "evolucija", "botanika", 
                   "zoologija", "mikrobiologija", "dna", "rna", "proteini", "encimi", 
                   "metabolizem", "celice", "tkiva", "organi", "telesni sistemi",
                   "nevroznanost", "imunologija", "embriologija"]
    },
    "programiranje": {
        "teme": ["programiranje", "python", "javascript", "java", "c++", "c#", "php", 
                   "ruby", "swift", "kotlin", "go", "rust", "html", "css", "sql", 
                   "mongodb", "git", "react", "angular", "vue", "nodejs", "django",
                   "flask", "spring boot", "laravel", "typescript", "graphql"]
    },
    "umetna_inteligenca": {
        "teme_posebne": ["strokovno učenje", "globoko učenje", "gpt", "llm"],
        "teme": ["umetna inteligenca", "nevronske mreže", "obdelava naravnega jezika", 
                   "računalniški vid", "klepetalni roboti", "transformatorji", "avtomatizacija",
                   "strokovno učenje", "globoko učenje", "obdelava naravnega jezika", "računalniški vid"]
    },
    "kibernetska_varnost": {
        "teme": ["kibernetska varnost", "etično hekanje", "požarni zidovi", "šifriranje", 
                   "informacijska varnost", "preizkušanje prodora", "zlonamerna programska oprema", "izsiljevalska programska oprema", 
                   "phishing", "socialno inženirstvo", "kriptografija", "omrežna varnost",
                   "spletna varnost", "mobilna varnost", "etično hekanje"]
    },
    "kuhanje": {
        "teme": ["kuhanje", "preprosti recepti", "sladice", "peka", "pecivo", 
                   "mehiška kuhinja", "italijanska kuhinja", "španska kuhinja", "pijače", 
                   "koktajli", "koktajli", "združevanje vina", "vino", "craft pivo",
                   "molekularna gastronomija", "vegetarijansko kuhanje", "vegansko kuhanje"]
    },
    "šport": {
        "teme": ["šport", "nogomet", "košarka", "tenis", "plavanje", "tek", 
                   "fitness", "telovadnica", "joga", "pilates", "crossfit", "športna prehrana",
                   "funkcionalno usposabljanje", "kalistenika", "boks", "borilne veščine"]
    },
    "poslovanje": {
        "teme": ["poslovanje", "podjetništvo", "startupi", "digitalno trženje", "prodaja", 
                   "osebne finance", "naložbe", "spletno poslovanje", "e-trgovina", 
                   "logistika", "vodenje", "vodenje podjetja", "človeški viri",
                   "služba za stranke", "oblikovanje blagovne znamke", "seo", "sem", "trženje po e-pošti"]
    }
}

# ============================================
# PREDPON
# ============================================
predpone = [
    "kako se naučiti", "kako obvladati", "popoln vodnik", "vadnica", "tečaj",
    "obvladati", "razumeti", "vaditi", "reševati težave", "vaje",
    "uvod v", "osnovni koncepti", "priročnik", "teorija",
    "primeri", "osnove", "nasveti za učenje", "viri za učenje",
    "lekcije", "lekcije", "kako se izboljšati v", "kako uporabljati"
]

# ============================================
# PRIPON
# ============================================
pripone = [
    "začetnik", "srednji", "napredni", "profesionalni", "popoln",
    "enostaven", "hiter", "za začetnike", "iz nič", "korak za korakom",
    "z vajami", "spletno", "brezplačen", "certificiran", "univerzitetna raven",
    "za otroke", "za odrasle", "intenziven", "praktičen", "teoretičen"
]

# ============================================
# VPRAŠANJA
# ============================================
vprašanja = [
    "kaj je", "kako deluje", "za kaj se uporablja", "kje se naučiti",
    "kdaj uporabiti", "zakaj je pomembno", "kakšne so prednosti",
    "kako dolgo traja učenje", "kaj potrebujem za študij"
]

# ============================================
# GENERIRANJE KLJUČNIH BESED
# ============================================
ključne_besede = set()

print("🔄 Generiranje slovenskih ključnih besed...")

for predpona in predpone:
    for cat_data in teme.values():
        for tema in cat_data["teme"]:
            ključne_besede.add(f"{predpona} {tema}")
        for tema_posebna in cat_data.get("teme_posebne", []):
            ključne_besede.add(f"{predpona} {tema_posebna}")

for pripona in pripone:
    for cat_data in teme.values():
        for tema in cat_data["teme"][:15]:
            ključne_besede.add(f"{tema} {pripona}")
        for tema_posebna in cat_data.get("teme_posebne", []):
            ključne_besede.add(f"{tema_posebna} {pripona}")

for vprašanje in vprašanja:
    for cat_data in teme.values():
        for tema in cat_data["teme"][:15]:
            ključne_besede.add(f"{vprašanje} {tema}")
        for tema_posebna in cat_data.get("teme_posebne", []):
            ključne_besede.add(f"{vprašanje} {tema_posebna}")

glagoli = ["nauči se", "obvladaj", "vadi", "študiraj", "razumi", "uporabi"]
for glagol in glagoli:
    for cat_data in teme.values():
        for tema in cat_data["teme"][:15]:
            ključne_besede.add(f"{glagol} {tema}")

for cat_data in teme.values():
    vse_teme = cat_data["teme"] + cat_data.get("teme_posebne", [])
    if len(vse_teme) >= 2:
        for _ in range(min(30, len(vse_teme) * 3)):
            tema1, tema2 = random.sample(vse_teme, 2)
            ključne_besede.add(f"razlika med {tema1} in {tema2}")
            ključne_besede.add(f"{tema1} proti {tema2}")
            ključne_besede.add(f"primerjava {tema1} in {tema2}")

for cat_data in teme.values():
    for tema in cat_data["teme"][:10]:
        ključne_besede.add(f"pogoste napake v {tema}")
        ključne_besede.add(f"kako se izogniti napakam v {tema}")
        ključne_besede.add(f"rešitev težav z {tema}")

ravni = ["začetnik", "srednji", "napredni", "profesionalni", "intenziven"]
for raven in ravni:
    for cat_data in teme.values():
        for tema in cat_data["teme"][:12]:
            ključne_besede.add(f"{raven} tečaj {tema}")
            ključne_besede.add(f"{tema} {raven} raven lekcije")

for cat_data in teme.values():
    for tema in cat_data["teme"][:10]:
        ključne_besede.add(f"certifikacija v {tema}")
        ključne_besede.add(f"izpit iz {tema}")
        ključne_besede.add(f"knjige o {tema}")
        ključne_besede.add(f"videi o {tema}")

for cat_data in teme.values():
    for tema in cat_data["teme"][:10]:
        ključne_besede.add(f"nasveti za {tema}")
        ključne_besede.add(f"priporočila za izboljšanje v {tema}")

for i in range(1, 2000):
    cat_name = random.choice(list(teme.keys()))
    tema = random.choice(teme[cat_name]["teme"])
    ključne_besede.add(f"{tema} lekcija {i}")
    ključne_besede.add(f"{tema} poglavje {i}")
    ključne_besede.add(f"{tema} enota {i}")

# ============================================
# OMEJITEV
# ============================================
seznam_ključnih_besed = sorted(list(ključne_besede))
random.shuffle(seznam_ključnih_besed)

if len(seznam_ključnih_besed) < ŠTEVILO_KLJUČNIH_BESED:
    print(f"⚠ Samo {len(seznam_ključnih_besed)} ključnih besed je bilo generiranih. Ponavljamo nekaj, da dosežemo {ŠTEVILO_KLJUČNIH_BESED}...")
    while len(seznam_ključnih_besed) < ŠTEVILO_KLJUČNIH_BESED:
        seznam_ključnih_besed.extend(seznam_ključnih_besed[:min(1000, ŠTEVILO_KLJUČNIH_BESED - len(seznam_ključnih_besed))])

končne_ključne_besede = seznam_ključnih_besed[:ŠTEVILO_KLJUČNIH_BESED]
random.shuffle(končne_ključne_besede)

# ============================================
# SHRANJEVANJE
# ============================================
with open('keywords/sl.json', 'w', encoding='utf-8') as f:
    json.dump(končne_ključne_besede, f, indent=2, ensure_ascii=False)

# ============================================
# POROČILO
# ============================================
print(f"\n✅ {len(končne_ključne_besede)} slovenskih ključnih besed je bilo generiranih")
print(f"📁 Shranjeno v: keywords/sl.json")
print(f"\n📊 Predogled (prvih 30 ključnih besed):")
for i, kw in enumerate(končne_ključne_besede[:30]):
    print(f"   {i+1}. {kw}")
