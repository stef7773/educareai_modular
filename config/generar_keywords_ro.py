import json
import random

# ============================================
# CONFIGURARE
# ============================================
NUMĂR_CUVINTE_CHEIE = 10000

# ============================================
# SUBIECTE ÎN ROMÂNĂ
# ============================================
subiecte = {
    "matematică": {
        "subiecte": ["matematică", "calcul", "algebră", "geometrie", "trigonometrie", 
                   "statistică", "probabilitate", "derivate", "integrale", "limite", 
                   "funcții", "matrici", "vectori", "ecuații", "logaritmi", 
                   "fracții", "procente", "rădăcini", "puteri", "polinoame", 
                   "numere complexe", "ecuații diferențiale", "algebră liniară",
                   "trigonometrie sferică", "calcul vectorial", "topologie", "teoria numerelor"]
    },
    "fizică": {
        "subiecte": ["fizică", "mecanică", "termodinamică", "electromagnetism", "optică", 
                   "acustică", "cinematică", "dinamică", "fluide", "fizică cuantică", 
                   "teoria relativității", "energie", "lucru", "putere", "mișcare", 
                   "forțe", "gravitație", "electricitate", "magnetism", "unde",
                   "astrofizică", "cosmologie", "fizică nucleară", "fizică moleculară"]
    },
    "chimie": {
        "subiecte": ["chimie", "chimie organică", "chimie anorganică", "chimie analitică", 
                   "biochimie", "reacții chimice", "echilibrare", "stoechiometrie", 
                   "tabel periodic", "legături chimice", "molecule", "atomi", 
                   "compuși chimici", "acizi", "baze", "ph", "soluții", 
                   "gaze", "termochimie", "chimie cuantică", "electrochimie"]
    },
    "biologie": {
        "subiecte": ["biologie", "biologie celulară", "biologie moleculară", "genetică", 
                   "anatomie", "fiziologie", "ecologie", "evoluție", "botanică", 
                   "zoologie", "microbiologie", "adn", "arn", "proteine", "enzime", 
                   "metabolism", "celule", "țesuturi", "organe", "sisteme corporale",
                   "neuroștiință", "imunologie", "embriologie"]
    },
    "programare": {
        "subiecte": ["programare", "python", "javascript", "java", "c++", "c#", "php", 
                   "ruby", "swift", "kotlin", "go", "rust", "html", "css", "sql", 
                   "mongodb", "git", "react", "angular", "vue", "nodejs", "django",
                   "flask", "spring boot", "laravel", "typescript", "graphql"]
    },
    "inteligență_artificială": {
        "subiecte_speciale": ["învățare automată", "învățare profundă", "gpt", "llm"],
        "subiecte": ["inteligență artificială", "rețele neuronale", "procesarea limbajului natural", 
                   "viziune artificială", "chatboți", "transformatoare", "automatizare",
                   "învățare automată", "învățare profundă", "procesarea limbajului natural", "viziune artificială"]
    },
    "securitate_cibernetică": {
        "subiecte": ["securitate cibernetică", "hacking etic", "firewall-uri", "criptare", 
                   "securitatea informațiilor", "testare de penetrare", "programe malware", "programe ransomware", 
                   "phishing", "inginerie socială", "criptografie", "securitatea rețelei",
                   "securitate web", "securitate mobilă", "hacking etic"]
    },
    "gătit": {
        "subiecte": ["gătit", "rețete simple", "deserturi", "coacere", "produse de patiserie", 
                   "mâncare mexicană", "mâncare italiană", "mâncare spaniolă", "băuturi", 
                   "cocktailuri", "cocktailuri", "asociere vin", "vin", "bere artizanală",
                   "gastronomie moleculară", "gătit vegetarian", "gătit vegan"]
    },
    "sport": {
        "subiecte": ["sport", "fotbal", "baschet", "tenis", "înot", "alergare", 
                   "fitness", "sală de sport", "yoga", "pilates", "crossfit", "nutriție sportivă",
                   "antrenament funcțional", "calisthenics", "box", "arte marțiale"]
    },
    "afaceri": {
        "subiecte": ["afaceri", "antreprenoriat", "startup-uri", "marketing digital", "vânzări", 
                   "finanțe personale", "investiții", "afaceri online", "comerț electronic", 
                   "logistică", "leadership", "managementul afacerilor", "resurse umane",
                   "servicii clienți", "construirea mărcii", "seo", "sem", "marketing prin email"]
    }
}

# ============================================
# PREFIXE
# ============================================
prefixe = [
    "cum să înveți", "cum să stăpânești", "ghid complet", "tutorial", "curs",
    "stăpânește", "înțelege", "exersează", "rezolvă probleme", "exerciții",
    "introducere în", "concepte de bază", "manual", "teorie",
    "exemple", "fundamente", "sfaturi pentru învățare", "resurse pentru studiu",
    "lecții", "lecții", "cum să te îmbunătățești în", "cum să folosești"
]

# ============================================
# SUFIXE
# ============================================
sufixe = [
    "începător", "intermediar", "avansat", "profesionist", "complet",
    "ușor", "rapid", "pentru începători", "de la zero", "pas cu pas",
    "cu exerciții", "online", "gratuit", "certificat", "nivel universitar",
    "pentru copii", "pentru adulți", "intensiv", "practic", "teoretic"
]

# ============================================
# ÎNTREBĂRI
# ============================================
întrebări = [
    "ce este", "cum funcționează", "la ce servește", "unde să înveți",
    "când să folosești", "de ce este important", "care sunt beneficiile",
    "cât timp durează să înveți", "de ce am nevoie pentru a studia"
]

# ============================================
# GENERARE CUVINTE CHEIE
# ============================================
cuvinte_cheie = set()

print("🔄 Generare cuvinte cheie în limba română...")

for prefix in prefixe:
    for cat_data in subiecte.values():
        for subiect in cat_data["subiecte"]:
            cuvinte_cheie.add(f"{prefix} {subiect}")
        for subiect_special in cat_data.get("subiecte_speciale", []):
            cuvinte_cheie.add(f"{prefix} {subiect_special}")

for sufix in sufixe:
    for cat_data in subiecte.values():
        for subiect in cat_data["subiecte"][:15]:
            cuvinte_cheie.add(f"{subiect} {sufix}")
        for subiect_special in cat_data.get("subiecte_speciale", []):
            cuvinte_cheie.add(f"{subiect_special} {sufix}")

for întrebare in întrebări:
    for cat_data in subiecte.values():
        for subiect in cat_data["subiecte"][:15]:
            cuvinte_cheie.add(f"{întrebare} {subiect}")
        for subiect_special in cat_data.get("subiecte_speciale", []):
            cuvinte_cheie.add(f"{întrebare} {subiect_special}")

verbe = ["învață", "stăpânește", "exersează", "studiază", "înțelege", "aplică"]
for verb in verbe:
    for cat_data in subiecte.values():
        for subiect in cat_data["subiecte"][:15]:
            cuvinte_cheie.add(f"{verb} {subiect}")

for cat_data in subiecte.values():
    toate_subiectele = cat_data["subiecte"] + cat_data.get("subiecte_speciale", [])
    if len(toate_subiectele) >= 2:
        for _ in range(min(30, len(toate_subiectele) * 3)):
            subiect1, subiect2 = random.sample(toate_subiectele, 2)
            cuvinte_cheie.add(f"diferența dintre {subiect1} și {subiect2}")
            cuvinte_cheie.add(f"{subiect1} vs {subiect2}")
            cuvinte_cheie.add(f"comparație {subiect1} și {subiect2}")

for cat_data in subiecte.values():
    for subiect in cat_data["subiecte"][:10]:
        cuvinte_cheie.add(f"greșeli comune în {subiect}")
        cuvinte_cheie.add(f"cum să eviți greșelile în {subiect}")
        cuvinte_cheie.add(f"soluție la problemele cu {subiect}")

niveluri = ["începător", "intermediar", "avansat", "profesionist", "intensiv"]
for nivel in niveluri:
    for cat_data in subiecte.values():
        for subiect in cat_data["subiecte"][:12]:
            cuvinte_cheie.add(f"curs {nivel} de {subiect}")
            cuvinte_cheie.add(f"lecții {subiect} nivel {nivel}")

for cat_data in subiecte.values():
    for subiect in cat_data["subiecte"][:10]:
        cuvinte_cheie.add(f"certificare în {subiect}")
        cuvinte_cheie.add(f"examen {subiect}")
        cuvinte_cheie.add(f"cărți despre {subiect}")
        cuvinte_cheie.add(f"videoclipuri despre {subiect}")

for cat_data in subiecte.values():
    for subiect in cat_data["subiecte"][:10]:
        cuvinte_cheie.add(f"sfaturi pentru {subiect}")
        cuvinte_cheie.add(f"recomandări pentru a te îmbunătăți în {subiect}")

for i in range(1, 2000):
    cat_name = random.choice(list(subiecte.keys()))
    subiect = random.choice(subiecte[cat_name]["subiecte"])
    cuvinte_cheie.add(f"{subiect} lecția {i}")
    cuvinte_cheie.add(f"{subiect} capitolul {i}")
    cuvinte_cheie.add(f"{subiect} unitatea {i}")

# ============================================
# LIMITARE
# ============================================
lista_cuvinte = sorted(list(cuvinte_cheie))
random.shuffle(lista_cuvinte)

if len(lista_cuvinte) < NUMĂR_CUVINTE_CHEIE:
    print(f"⚠ S-au generat doar {len(lista_cuvinte)} cuvinte cheie. Se repetă câteva pentru a ajunge la {NUMĂR_CUVINTE_CHEIE}...")
    while len(lista_cuvinte) < NUMĂR_CUVINTE_CHEIE:
        lista_cuvinte.extend(lista_cuvinte[:min(1000, NUMĂR_CUVINTE_CHEIE - len(lista_cuvinte))])

cuvinte_finale = lista_cuvinte[:NUMĂR_CUVINTE_CHEIE]
random.shuffle(cuvinte_finale)

# ============================================
# SALVARE
# ============================================
with open('keywords/ro.json', 'w', encoding='utf-8') as f:
    json.dump(cuvinte_finale, f, indent=2, ensure_ascii=False)

# ============================================
# RAPORT
# ============================================
print(f"\n✅ {len(cuvinte_finale)} cuvinte cheie în limba română generate")
print(f"📁 Salvate în: keywords/ro.json")
print(f"\n📊 Previzualizare (primele 30 de cuvinte cheie):")
for i, kw in enumerate(cuvinte_finale[:30]):
    print(f"   {i+1}. {kw}")
