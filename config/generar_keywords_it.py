import json
import random

# ============================================
# CONFIGURAZIONE
# ============================================
QUANTITA_KEYWORDS = 10000

# ============================================
# ARGOMENTI IN ITALIANO
# ============================================
argomenti = {
    "matematica": {
        "argomenti": ["matematica", "calcolo", "algebra", "geometria", "trigonometria", 
                   "statistica", "probabilita", "derivate", "integrali", "limiti", 
                   "funzioni", "matrici", "vettori", "equazioni", "logaritmi", 
                   "frazioni", "percentuali", "radici", "potenze", "polinomi", 
                   "numeri complessi", "equazioni differenziali", "algebra lineare",
                   "trigonometria sferica", "calcolo vettoriale", "topologia", "teoria dei numeri"]
    },
    "fisica": {
        "argomenti": ["fisica", "meccanica", "termodinamica", "elettromagnetismo", "ottica", 
                   "acustica", "cinematica", "dinamica", "fluidi", "quantistica", 
                   "relativita", "energia", "lavoro", "potenza", "moto", 
                   "forze", "gravita", "elettricita", "magnetismo", "onde",
                   "astrofisica", "cosmologia", "fisica nucleare", "fisica molecolare"]
    },
    "chimica": {
        "argomenti": ["chimica", "chimica organica", "chimica inorganica", "chimica analitica", 
                   "biochimica", "reazioni chimiche", "bilanciamento", "stechiometria", 
                   "tavola periodica", "legami chimici", "molecole", "atomi", 
                   "composti chimici", "acidi", "basi", "ph", "soluzioni", 
                   "gas", "termochimica", "chimica quantistica", "elettrochimica"]
    },
    "biologia": {
        "argomenti": ["biologia", "biologia cellulare", "biologia molecolare", "genetica", 
                   "anatomia", "fisiologia", "ecologia", "evoluzione", "botanica", 
                   "zoologia", "microbiologia", "dna", "rna", "proteine", "enzimi", 
                   "metabolismo", "cellule", "tessuti", "organi", "sistemi del corpo",
                   "neuroscienze", "immunologia", "embriologia"]
    },
    "programmazione": {
        "argomenti": ["programmazione", "python", "javascript", "java", "c++", "c#", "php", 
                   "ruby", "swift", "kotlin", "go", "rust", "html", "css", "sql", 
                   "mongodb", "git", "react", "angular", "vue", "nodejs", "django",
                   "flask", "spring boot", "laravel", "typescript", "graphql"]
    },
    "intelligenza_artificiale": {
        "argomenti_speciali": ["machine learning", "deep learning", "gpt", "llm"],
        "argomenti": ["intelligenza artificiale", "reti neurali", "elaborazione del linguaggio naturale", 
                   "visione artificiale", "chatbot", "trasformatori", "automazione",
                   "apprendimento automatico", "apprendimento profondo", "pnl", "visione artificiale"]
    },
    "cybersicurezza": {
        "argomenti": ["cybersicurezza", "hacking etico", "firewall", "crittografia", 
                   "sicurezza informatica", "penetration test", "malware", "ransomware", 
                   "phishing", "ingegneria sociale", "crittografia", "sicurezza di rete",
                   "sicurezza web", "sicurezza mobile", "hacking etico"]
    },
    "cucina": {
        "argomenti": ["cucina", "ricette facili", "dolci", "pasticceria", "forno", 
                   "cibo messicano", "cibo italiano", "cibo spagnolo", "bevande", 
                   "cocktail", "cocktail", "abbinamento", "vino", "birra artigianale",
                   "gastronomia molecolare", "cucina vegetariana", "cucina vegana"]
    },
    "sport": {
        "argomenti": ["sport", "calcio", "basket", "tennis", "nuoto", "corsa", 
                   "fitness", "palestra", "yoga", "pilates", "crossfit", "nutrizione sportiva",
                   "allenamento funzionale", "calisthenics", "boxe", "arti marziali"]
    },
    "business": {
        "argomenti": ["business", "imprenditoria", "startup", "marketing digitale", "vendite", 
                   "finanza personale", "investimenti", "business online", "ecommerce", 
                   "logistica", "leadership", "gestione aziendale", "risorse umane",
                   "servizio clienti", "branding", "seo", "sem", "email marketing"]
    }
}

# ============================================
# PREFISSI
# ============================================
prefissi = [
    "come imparare", "come padroneggiare", "guida completa a", "tutorial su", "corso di",
    "padroneggiare", "capire", "praticare", "risolvere problemi di", "esercizi di",
    "introduzione a", "concetti base di", "manuale di", "teoria di",
    "esempi di", "fondamenti di", "consigli per imparare", "risorse per studiare",
    "lezioni di", "lezioni di", "come migliorare in", "come usare"
]

# ============================================
# SUFFISSI
# ============================================
suffissi = [
    "base", "intermedio", "avanzato", "professionale", "completo",
    "facile", "veloce", "per principianti", "da zero", "passo dopo passo",
    "con esercizi", "online", "gratis", "certificato", "universitario",
    "per bambini", "per adulti", "intensivo", "pratico", "teorico"
]

# ============================================
# DOMANDE
# ============================================
domande = [
    "cos e", "come funziona", "a cosa serve", "dove imparare",
    "quando usare", "perche e importante", "quali sono i benefici di",
    "quanto tempo ci vuole per imparare", "cosa serve per studiare"
]

# ============================================
# GENERAZIONE KEYWORDS
# ============================================
keywords = set()

print("🔄 Generazione keywords in italiano...")

# 1. Combinazioni con prefissi
for prefisso in prefissi:
    for cat_data in argomenti.values():
        for arg in cat_data["argomenti"]:
            keywords.add(f"{prefisso} {arg}")
        for arg_spec in cat_data.get("argomenti_speciali", []):
            keywords.add(f"{prefisso} {arg_spec}")

# 2. Combinazioni con suffissi
for suffisso in suffissi:
    for cat_data in argomenti.values():
        for arg in cat_data["argomenti"][:15]:
            keywords.add(f"{arg} {suffisso}")
        for arg_spec in cat_data.get("argomenti_speciali", []):
            keywords.add(f"{arg_spec} {suffisso}")

# 3. Domande
for domanda in domande:
    for cat_data in argomenti.values():
        for arg in cat_data["argomenti"][:15]:
            keywords.add(f"{domanda} {arg}")
        for arg_spec in cat_data.get("argomenti_speciali", []):
            keywords.add(f"{domanda} {arg_spec}")

# 4. Verbi + argomento
verbi = ["imparare", "padroneggiare", "praticare", "studiare", "capire", "applicare"]
for verbo in verbi:
    for cat_data in argomenti.values():
        for arg in cat_data["argomenti"][:15]:
            keywords.add(f"{verbo} {arg}")

# 5. Confronti
for cat_data in argomenti.values():
    tutti_argomenti = cat_data["argomenti"] + cat_data.get("argomenti_speciali", [])
    if len(tutti_argomenti) >= 2:
        for _ in range(min(30, len(tutti_argomenti) * 3)):
            arg1, arg2 = random.sample(tutti_argomenti, 2)
            keywords.add(f"differenza tra {arg1} e {arg2}")
            keywords.add(f"{arg1} vs {arg2}")
            keywords.add(f"confronto {arg1} vs {arg2}")

# 6. Errori comuni
for cat_data in argomenti.values():
    for arg in cat_data["argomenti"][:10]:
        keywords.add(f"errori comuni in {arg}")
        keywords.add(f"come evitare errori in {arg}")
        keywords.add(f"soluzione a problemi di {arg}")

# 7. Corsi e livelli
livelli = ["base", "intermedio", "avanzato", "professionale", "intensivo"]
for livello in livelli:
    for cat_data in argomenti.values():
        for arg in cat_data["argomenti"][:12]:
            keywords.add(f"corso {livello} di {arg}")
            keywords.add(f"lezioni di {arg} livello {livello}")

# 8. Certificazioni e risorse
for cat_data in argomenti.values():
    for arg in cat_data["argomenti"][:10]:
        keywords.add(f"certificazione in {arg}")
        keywords.add(f"esame di {arg}")
        keywords.add(f"libri di {arg}")
        keywords.add(f"video di {arg}")

# 9. Consigli
for cat_data in argomenti.values():
    for arg in cat_data["argomenti"][:10]:
        keywords.add(f"consigli per {arg}")
        keywords.add(f"suggerimenti per migliorare in {arg}")

# 10. Variazioni numeriche
for i in range(1, 2000):
    cat_name = random.choice(list(argomenti.keys()))
    arg = random.choice(argomenti[cat_name]["argomenti"])
    keywords.add(f"lezione {i} di {arg}")
    keywords.add(f"capitolo {i} di {arg}")
    keywords.add(f"unita {i} di {arg}")

# ============================================
# LIMITARE
# ============================================
keywords_lista = sorted(list(keywords))
random.shuffle(keywords_lista)

if len(keywords_lista) < QUANTITA_KEYWORDS:
    print(f"⚠ Solo {len(keywords_lista)} keywords generate. Ripetendo alcune per raggiungere {QUANTITA_KEYWORDS}...")
    while len(keywords_lista) < QUANTITA_KEYWORDS:
        keywords_lista.extend(keywords_lista[:min(1000, QUANTITA_KEYWORDS - len(keywords_lista))])

keywords_final = keywords_lista[:QUANTITA_KEYWORDS]
random.shuffle(keywords_final)

# ============================================
# SALVARE
# ============================================
with open('keywords/it.json', 'w', encoding='utf-8') as f:
    json.dump(keywords_final, f, indent=2, ensure_ascii=False)

# ============================================
# REPORT
# ============================================
print(f"\n✅ {len(keywords_final)} keywords generate in italiano")
print(f"📁 Salvato in: keywords/it.json")
print(f"\n📊 Anteprima (prime 30 keywords):")
for i, kw in enumerate(keywords_final[:30]):
    print(f"   {i+1}. {kw}")
