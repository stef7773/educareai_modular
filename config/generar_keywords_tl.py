import json
import random

# ============================================
# KONPIGURASYON
# ============================================
BILANG_NG_MGA_SUSI = 10000

# ============================================
# MGA PAKSA SA TAGALOG
# ============================================
mga_paksa = {
    "matematika": {
        "mga_paksa": ["matematika", "kalkulo", "algebra", "heometriya", "trigonometriya", 
                   "estadistika", "probabilidad", "deribatibo", "integral", "limit", 
                   "punksyon", "matris", "vector", "ekwasyon", "logaritmo", 
                   "praksyon", "porsyento", "ugat", "kapangyarihan", "polynomial", 
                   "komplex na numero", "diferensyal na ekwasyon", "linear algebra",
                   "spherical trigonometry", "vector kalkulo", "topolohiya", "teorya ng numero"]
    },
    "pisika": {
        "mga_paksa": ["pisika", "mekanika", "termodinamika", "elektromagnetismo", "optika", 
                   "akustika", "kinematika", "dinamika", "likido", "quantum pisika", 
                   "teorya ng relativity", "enerhiya", "trabaho", "kapangyarihan", "galaw", 
                   "puwersa", "gravidad", "kuryente", "magnetismo", "alon",
                   "astropisika", "kosmohiya", "nuclear pisika", "molekular pisika"]
    },
    "kimika": {
        "mga_paksa": ["kimika", "organic kimika", "inorganic kimika", "analitikal na kimika", 
                   "biokimika", "reaksyong kemikal", "pagbalanse", "stokiyometriya", 
                   "periodic table", "kemikal na bon", "molekula", "atomo", 
                   "kemikal na kompuwesto", "asido", "base", "ph", "solusyon", 
                   "gas", "termokimika", "quantum kimika", "elektrokimika"]
    },
    "biyolohiya": {
        "mga_paksa": ["biyolohiya", "cell biyolohiya", "molekular biyolohiya", "henetika", 
                   "anatomiya", "pisyolohiya", "ekolohiya", "ebolusyon", "botanika", 
                   "soolohiya", "mikrobiyolohiya", "dna", "rna", "protina", "enzima", 
                   "metabolismo", "cell", "tisyu", "organ", "sistema ng katawan",
                   "neurosiyensya", "immunolohiya", "embriyolohiya"]
    },
    "programming": {
        "mga_paksa": ["programming", "python", "javascript", "java", "c++", "c#", "php", 
                   "ruby", "swift", "kotlin", "go", "rust", "html", "css", "sql", 
                   "mongodb", "git", "react", "angular", "vue", "nodejs", "django",
                   "flask", "spring boot", "laravel", "typescript", "graphql"]
    },
    "artipisyal_na_katalinuhan": {
        "mga_paksa_espesyal": ["machine learning", "deep learning", "gpt", "llm"],
        "mga_paksa": ["artipisyal na katalinuhan", "neural network", "natural na pagproseso ng wika", 
                   "computer vision", "chatbot", "transpormer", "automation",
                   "machine learning", "deep learning", "natural na pagproseso ng wika", "computer vision"]
    },
    "cybersecurity": {
        "mga_paksa": ["cybersecurity", "ethical hacking", "firewall", "encryption", 
                   "seguridad ng impormasyon", "penetration testing", "malware", "ransomware", 
                   "phishing", "social engineering", "kriptograpiya", "seguridad ng network",
                   "seguridad ng web", "seguridad ng mobile", "ethical hacking"]
    },
    "pagluluto": {
        "mga_paksa": ["pagluluto", "madaling recipe", "panghimagas", "paghurno", "pastry", 
                   "meksikano na pagkain", "italyano na pagkain", "espanyol na pagkain", "inumin", 
                   "cocktail", "cocktail", "pagtutugma ng alak", "alak", "craft beer",
                   "molecular gastronomy", "vegetarian na pagluluto", "vegan na pagluluto"]
    },
    "palakasan": {
        "mga_paksa": ["palakasan", "futbol", "basketball", "tenis", "paglalangoy", "pagtakbo", 
                   "fitness", "gym", "yoga", "pilates", "crossfit", "nutrisyon sa palakasan",
                   "functional na pagsasanay", "calisthenics", "boksing", "martial arts"]
    },
    "negosyo": {
        "mga_paksa": ["negosyo", "pagnenegosyo", "startup", "digital marketing", "pagbebenta", 
                   "personal na pananalapi", "investment", "online na negosyo", "ecommerce", 
                   "logistics", "pamumuno", "pamamahala ng negosyo", "human resources",
                   "serbisyo sa customer", "pagba-brand", "seo", "sem", "email marketing"]
    }
}

# ============================================
# MGA UNLAPI
# ============================================
mga_unlapi = [
    "paano matuto", "paano makabisado", "kumpletong gabay sa", "tutorial sa", "kurso sa",
    "kabisaduhin", "maunawaan", "magsanay", "lutasin ang mga problema ng", "mga ehersisyo sa",
    "panimula sa", "mga pangunahing konsepto ng", "manwal ng", "teorya ng",
    "mga halimbawa ng", "mga batayan ng", "mga tip sa pag-aaral", "mga mapagkukunan para sa pag-aaral",
    "mga aralin sa", "mga aralin sa", "paano bumuti sa", "paano gamitin"
]

# ============================================
# MGA HULAPI
# ============================================
mga_hulapi = [
    "baguhan", "intermediate", "advance", "propesyonal", "kumpleto",
    "madali", "mabilis", "para sa mga baguhan", "mula sa wala", "hakbang sa hakbang",
    "may mga ehersisyo", "online", "libre", "sertipikado", "antas ng unibersidad",
    "para sa mga bata", "para sa mga matatanda", "intensive", "praktikal", "teoretikal"
]

# ============================================
# MGA TANONG
# ============================================
mga_tanong = [
    "ano ang", "paano ito gumagana", "para saan", "saan matututo",
    "kailan gagamitin", "bakit ito mahalaga", "ano ang mga benepisyo ng",
    "gaano katagal bago matuto", "ano ang kailangan ko para mag-aral"
]

# ============================================
# BUUIN ANG MGA SUSI
# ============================================
mga_susi = set()

print("🔄 Binubuo ang mga tagalog na keyword...")

for unlapi in mga_unlapi:
    for cat_data in mga_paksa.values():
        for paksa in cat_data["mga_paksa"]:
            mga_susi.add(f"{unlapi} {paksa}")
        for paksa_espesyal in cat_data.get("mga_paksa_espesyal", []):
            mga_susi.add(f"{unlapi} {paksa_espesyal}")

for hulapi in mga_hulapi:
    for cat_data in mga_paksa.values():
        for paksa in cat_data["mga_paksa"][:15]:
            mga_susi.add(f"{paksa} {hulapi}")
        for paksa_espesyal in cat_data.get("mga_paksa_espesyal", []):
            mga_susi.add(f"{paksa_espesyal} {hulapi}")

for tanong in mga_tanong:
    for cat_data in mga_paksa.values():
        for paksa in cat_data["mga_paksa"][:15]:
            mga_susi.add(f"{tanong} {paksa}")
        for paksa_espesyal in cat_data.get("mga_paksa_espesyal", []):
            mga_susi.add(f"{tanong} {paksa_espesyal}")

mga_pandiwa = ["matuto", "kabisaduhin", "magsanay", "mag-aral", "maunawaan", "ilapat"]
for pandiwa in mga_pandiwa:
    for cat_data in mga_paksa.values():
        for paksa in cat_data["mga_paksa"][:15]:
            mga_susi.add(f"{pandiwa} {paksa}")

for cat_data in mga_paksa.values():
    lahat_ng_paksa = cat_data["mga_paksa"] + cat_data.get("mga_paksa_espesyal", [])
    if len(lahat_ng_paksa) >= 2:
        for _ in range(min(30, len(lahat_ng_paksa) * 3)):
            paksa1, paksa2 = random.sample(lahat_ng_paksa, 2)
            mga_susi.add(f"pagkakaiba sa pagitan ng {paksa1} at {paksa2}")
            mga_susi.add(f"{paksa1} laban sa {paksa2}")
            mga_susi.add(f"paghahambing ng {paksa1} at {paksa2}")

for cat_data in mga_paksa.values():
    for paksa in cat_data["mga_paksa"][:10]:
        mga_susi.add(f"karaniwang pagkakamali sa {paksa}")
        mga_susi.add(f"paano maiwasan ang mga pagkakamali sa {paksa}")
        mga_susi.add(f"solusyon sa mga problema ng {paksa}")

mga_antas = ["baguhan", "intermediate", "advance", "propesyonal", "intensive"]
for antas in mga_antas:
    for cat_data in mga_paksa.values():
        for paksa in cat_data["mga_paksa"][:12]:
            mga_susi.add(f"{antas} na kurso sa {paksa}")
            mga_susi.add(f"{paksa} {antas} na antas ng mga aralin")

for cat_data in mga_paksa.values():
    for paksa in cat_data["mga_paksa"][:10]:
        mga_susi.add(f"sertipikasyon sa {paksa}")
        mga_susi.add(f"pagsusulit sa {paksa}")
        mga_susi.add(f"mga libro tungkol sa {paksa}")
        mga_susi.add(f"mga video tungkol sa {paksa}")

for cat_data in mga_paksa.values():
    for paksa in cat_data["mga_paksa"][:10]:
        mga_susi.add(f"mga tip para sa {paksa}")
        mga_susi.add(f"payo upang mapabuti sa {paksa}")

for i in range(1, 2000):
    cat_name = random.choice(list(mga_paksa.keys()))
    paksa = random.choice(mga_paksa[cat_name]["mga_paksa"])
    mga_susi.add(f"{paksa} aralin {i}")
    mga_susi.add(f"{paksa} kabanata {i}")
    mga_susi.add(f"{paksa} unit {i}")

# ============================================
# LIMITAHAN
# ============================================
listahan_ng_mga_susi = sorted(list(mga_susi))
random.shuffle(listahan_ng_mga_susi)

if len(listahan_ng_mga_susi) < BILANG_NG_MGA_SUSI:
    print(f"⚠ {len(listahan_ng_mga_susi)} lamang na keyword ang nabuo. Inuulit ang ilan upang maabot ang {BILANG_NG_MGA_SUSI}...")
    while len(listahan_ng_mga_susi) < BILANG_NG_MGA_SUSI:
        listahan_ng_mga_susi.extend(listahan_ng_mga_susi[:min(1000, BILANG_NG_MGA_SUSI - len(listahan_ng_mga_susi))])

panghuling_mga_susi = listahan_ng_mga_susi[:BILANG_NG_MGA_SUSI]
random.shuffle(panghuling_mga_susi)

# ============================================
# SAVE
# ============================================
with open('keywords/tl.json', 'w', encoding='utf-8') as f:
    json.dump(panghuling_mga_susi, f, indent=2, ensure_ascii=False)

# ============================================
# ULAT
# ============================================
print(f"\n✅ {len(panghuling_mga_susi)} mga keyword sa tagalog ang nabuo")
print(f"📁 Na-save sa: keywords/tl.json")
print(f"\n📊 Preview (unang 30 keyword):")
for i, kw in enumerate(panghuling_mga_susi[:30]):
    print(f"   {i+1}. {kw}")
