import json
import random

# ============================================
# KONFIGURATION
# ============================================
ANZAHL_KEYWORDS = 10000

# ============================================
# THEMEN AUF DEUTSCH
# ============================================
themen = {
    "mathematik": {
        "themen": ["mathematik", "analysis", "algebra", "geometrie", "trigonometrie", 
                   "statistik", "wahrscheinlichkeit", "ableitungen", "integrale", "grenzwerte", 
                   "funktionen", "matrizen", "vektoren", "gleichungen", "logarithmen", 
                   "bruche", "prozente", "wurzeln", "potenzen", "polynome", 
                   "komplexe zahlen", "differentialgleichungen", "lineare algebra",
                   "spharische trigonometrie", "vektoranalysis", "topologie", "zahlentheorie"]
    },
    "physik": {
        "themen": ["physik", "mechanik", "thermodynamik", "elektromagnetismus", "optik", 
                   "akustik", "kinematik", "dynamik", "flussigkeiten", "quantenphysik", 
                   "relativitatstheorie", "energie", "arbeit", "leistung", "bewegung", 
                   "krafte", "gravitation", "elektrizitat", "magnetismus", "wellen",
                   "astrophysik", "kosmologie", "kernphysik", "molekularphysik"]
    },
    "chemie": {
        "themen": ["chemie", "organische chemie", "anorganische chemie", "analytische chemie", 
                   "biochemie", "chemische reaktionen", "stchiometrie", 
                   "periodensystem", "chemische bindungen", "molekule", "atome", 
                   "chemische verbindungen", "sauren", "basen", "ph wert", "losungen", 
                   "gase", "thermochemie", "quantenchemie", "elektrochemie"]
    },
    "biologie": {
        "themen": ["biologie", "zellbiologie", "molekularbiologie", "genetik", 
                   "anatomie", "physiologie", "okologie", "evolution", "botanik", 
                   "zoologie", "mikrobiologie", "dns", "rns", "proteine", "enzyme", 
                   "stoffwechsel", "zellen", "gewebe", "organe", "korpersysteme",
                   "neurowissenschaft", "immunologie", "embryologie"]
    },
    "programmierung": {
        "themen": ["programmierung", "python", "javascript", "java", "c++", "c#", "php", 
                   "ruby", "swift", "kotlin", "go", "rust", "html", "css", "sql", 
                   "mongodb", "git", "react", "angular", "vue", "nodejs", "django",
                   "flask", "spring boot", "laravel", "typescript", "graphql"]
    },
    "kunstliche_intelligenz": {
        "themen_spezial": ["maschinelles lernen", "deep learning", "gpt", "llm"],
        "themen": ["kunstliche intelligenz", "neuronale netze", "naturliche sprachverarbeitung", 
                   "computersehen", "chatbots", "transformatoren", "automatisierung",
                   "maschinelles lernen", "deep learning", "nlp", "computersehen"]
    },
    "cybersicherheit": {
        "themen": ["cybersicherheit", "ethisches hacking", "firewalls", "verschlusselung", 
                   "informationssicherheit", "penetrationstest", "malware", "ransomware", 
                   "phishing", "social engineering", "kryptographie", "netzwerksicherheit",
                   "websicherheit", "mobile sicherheit", "ethisches hacking"]
    },
    "kuchen": {
        "themen": ["kuchen", "einfache rezepte", "desserts", "backen", "geback", 
                   "mexikanisches essen", "italienisches essen", "spanisches essen", "getranke", 
                   "cocktails", "cocktails", "weinbegleitung", "wein", "craft beer",
                   "molekulare gastronomie", "vegetarische kuche", "vegane kuche"]
    },
    "sport": {
        "themen": ["sport", "fussball", "basketball", "tennis", "schwimmen", "laufen", 
                   "fitness", "fitnessstudio", "yoga", "pilates", "crossfit", "sportlernahrung",
                   "funktionelles training", "kalisthenie", "boxen", "kampfkunste"]
    },
    "wirtschaft": {
        "themen": ["wirtschaft", "unternehmertum", "startups", "digitales marketing", "verkauf", 
                   "personliche finanzen", "investitionen", "online geschaft", "ecommerce", 
                   "logistik", "fuhrung", "unternehmensfuhrung", "personalwesen",
                   "kundenservice", "markenbildung", "seo", "sem", "email marketing"]
    }
}

# ============================================
# PRÄFIXE
# ============================================
praefixe = [
    "wie lernt man", "wie meistert man", "vollstandiger leitfaden zu", "tutorial zu", "kurs zu",
    "meistern", "verstehen", "ubung", "probleme losen von", "ubungen zu",
    "einfuhrung in", "grundlagen von", "handbuch von", "theorie von",
    "beispiele von", "grundlagen von", "tipps zum lernen", "ressourcen zum studieren",
    "kurse zu", "lektionen zu", "wie verbessert man sich in", "wie verwendet man"
]

# ============================================
# SUFFIXE
# ============================================
suffixe = [
    "anfanger", "mittelstufe", "fortgeschritten", "profi", "komplett",
    "einfach", "schnell", "fur anfanger", "von grund auf", "schritt fur schritt",
    "mit ubungen", "online", "kostenlos", "zertifiziert", "universitatsniveau",
    "fur kinder", "fur erwachsene", "intensiv", "praktisch", "theoretisch"
]

# ============================================
# FRAGEN
# ============================================
fragen = [
    "was ist", "wie funktioniert", "wozu dient", "wo lernen",
    "wann verwenden", "warum ist wichtig", "was sind die vorteile von",
    "wie lange dauert es zu lernen", "was brauche ich zum studieren"
]

# ============================================
# GENERIERUNG DER KEYWORDS
# ============================================
keywords = set()

print("🔄 Generiere deutsche Keywords...")

# 1. Kombinationen mit Präfixen
for praefix in praefixe:
    for cat_data in themen.values():
        for thema in cat_data["themen"]:
            keywords.add(f"{praefix} {thema}")
        for thema_spec in cat_data.get("themen_spezial", []):
            keywords.add(f"{praefix} {thema_spec}")

# 2. Kombinationen mit Suffixen
for suffix in suffixe:
    for cat_data in themen.values():
        for thema in cat_data["themen"][:15]:
            keywords.add(f"{thema} {suffix}")
        for thema_spec in cat_data.get("themen_spezial", []):
            keywords.add(f"{thema_spec} {suffix}")

# 3. Fragen
for frage in fragen:
    for cat_data in themen.values():
        for thema in cat_data["themen"][:15]:
            keywords.add(f"{frage} {thema}")
        for thema_spec in cat_data.get("themen_spezial", []):
            keywords.add(f"{frage} {thema_spec}")

# 4. Verben + Thema
verben = ["lernen", "meistern", "uben", "studieren", "verstehen", "anwenden"]
for verb in verben:
    for cat_data in themen.values():
        for thema in cat_data["themen"][:15]:
            keywords.add(f"{verb} {thema}")

# 5. Vergleiche
for cat_data in themen.values():
    alle_themen = cat_data["themen"] + cat_data.get("themen_spezial", [])
    if len(alle_themen) >= 2:
        for _ in range(min(30, len(alle_themen) * 3)):
            thema1, thema2 = random.sample(alle_themen, 2)
            keywords.add(f"unterschied zwischen {thema1} und {thema2}")
            keywords.add(f"{thema1} vs {thema2}")
            keywords.add(f"vergleich {thema1} vs {thema2}")

# 6. Häufige Fehler
for cat_data in themen.values():
    for thema in cat_data["themen"][:10]:
        keywords.add(f"haufige fehler in {thema}")
        keywords.add(f"wie vermeidet man fehler in {thema}")
        keywords.add(f"losungen fur probleme mit {thema}")

# 7. Kurse und Niveaus
niveaus = ["anfanger", "mittelstufe", "fortgeschritten", "profi", "intensiv"]
for niveau in niveaus:
    for cat_data in themen.values():
        for thema in cat_data["themen"][:12]:
            keywords.add(f"{niveau} kurs in {thema}")
            keywords.add(f"{thema} kurse {niveau} niveau")

# 8. Zertifizierungen und Ressourcen
for cat_data in themen.values():
    for thema in cat_data["themen"][:10]:
        keywords.add(f"zertifizierung in {thema}")
        keywords.add(f"{thema} prufung")
        keywords.add(f"{thema} bucher")
        keywords.add(f"{thema} videos")

# 9. Tipps
for cat_data in themen.values():
    for thema in cat_data["themen"][:10]:
        keywords.add(f"tipps fur {thema}")
        keywords.add(f"ratschlage um sich zu verbessern in {thema}")

# 10. Numerische Variationen
for i in range(1, 2000):
    cat_name = random.choice(list(themen.keys()))
    thema = random.choice(themen[cat_name]["themen"])
    keywords.add(f"lektion {i} von {thema}")
    keywords.add(f"kapitel {i} von {thema}")
    keywords.add(f"einheit {i} von {thema}")

# ============================================
# BEGRENZUNG
# ============================================
keywords_liste = sorted(list(keywords))
random.shuffle(keywords_liste)

if len(keywords_liste) < ANZAHL_KEYWORDS:
    print(f"⚠ Nur {len(keywords_liste)} Keywords generiert. Wiederhole einige, um {ANZAHL_KEYWORDS} zu erreichen...")
    while len(keywords_liste) < ANZAHL_KEYWORDS:
        keywords_liste.extend(keywords_liste[:min(1000, ANZAHL_KEYWORDS - len(keywords_liste))])

keywords_final = keywords_liste[:ANZAHL_KEYWORDS]
random.shuffle(keywords_final)

# ============================================
# SPEICHERN
# ============================================
with open('keywords/de.json', 'w', encoding='utf-8') as f:
    json.dump(keywords_final, f, indent=2, ensure_ascii=False)

# ============================================
# BERICHT
# ============================================
print(f"\n✅ {len(keywords_final)} Keywords auf Deutsch generiert")
print(f"📁 Gespeichert in: keywords/de.json")
print(f"\n📊 Vorschau (erste 30 Keywords):")
for i, kw in enumerate(keywords_final[:30]):
    print(f"   {i+1}. {kw}")
