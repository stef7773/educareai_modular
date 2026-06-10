import json
import random

# ============================================
# CONFIGURATIE
# ============================================
AANTAL_KEYWORDS = 10000

# ============================================
# ONDERWERPEN IN HET NEDERLANDS
# ============================================
onderwerpen = {
    "wiskunde": {
        "onderwerpen": ["wiskunde", "calculus", "algebra", "meetkunde", "trigonometrie", 
                   "statistiek", "kansrekening", "afgeleiden", "integralen", "limieten", 
                   "functies", "matrices", "vectoren", "vergelijkingen", "logaritmen", 
                   "breuken", "percentages", "wortels", "machten", "polynomen", 
                   "complexe getallen", "differentiaalvergelijkingen", "lineaire algebra",
                   "sferische trigonometrie", "vectorrekening", "topologie", "getaltheorie"]
    },
    "natuurkunde": {
        "onderwerpen": ["natuurkunde", "mechanica", "thermodynamica", "elektromagnetisme", "optica", 
                   "akoestiek", "kinematica", "dynamica", "vloeistoffen", "kwantum", 
                   "relativiteit", "energie", "arbeid", "vermogen", "beweging", 
                   "krachten", "zwaartekracht", "elektriciteit", "magnetisme", "golven",
                   "astrofysica", "kosmologie", "kernfysica", "moleculaire fysica"]
    },
    "scheikunde": {
        "onderwerpen": ["scheikunde", "organische chemie", "anorganische chemie", "analytische chemie", 
                   "biochemie", "chemische reacties", "balanceren", "stoichiometrie", 
                   "periodiek systeem", "chemische bindingen", "moleculen", "atomen", 
                   "chemische verbindingen", "zuren", "basen", "ph", "oplossingen", 
                   "gassen", "thermochemie", "kwantumchemie", "elektrochemie"]
    },
    "biologie": {
        "onderwerpen": ["biologie", "celbiologie", "moleculaire biologie", "genetica", 
                   "anatomie", "fysiologie", "ecologie", "evolutie", "plantkunde", 
                   "dierkunde", "microbiologie", "dna", "rna", "eiwitten", "enzymen", 
                   "metabolisme", "cellen", "weefsels", "organen", "lichaamssystemen",
                   "neurowetenschap", "immunologie", "embryologie"]
    },
    "programmeren": {
        "onderwerpen": ["programmeren", "python", "javascript", "java", "c++", "c#", "php", 
                   "ruby", "swift", "kotlin", "go", "rust", "html", "css", "sql", 
                   "mongodb", "git", "react", "angular", "vue", "nodejs", "django",
                   "flask", "spring boot", "laravel", "typescript", "graphql"]
    },
    "kunstmatige_intelligentie": {
        "onderwerpen_speciaal": ["machine learning", "deep learning", "gpt", "llm"],
        "onderwerpen": ["kunstmatige intelligentie", "neurale netwerken", "natuurlijke taalverwerking", 
                   "computervisie", "chatbots", "transformers", "automatisering",
                   "machine learning", "deep learning", "nlp", "computervisie"]
    },
    "cyberbeveiliging": {
        "onderwerpen": ["cyberbeveiliging", "ethisch hacken", "firewalls", "encryptie", 
                   "informatiebeveiliging", "penetratietesten", "malware", "ransomware", 
                   "phishing", "sociale manipulatie", "cryptografie", "netwerkbeveiliging",
                   "webbeveiliging", "mobiele beveiliging", "ethisch hacken"]
    },
    "koken": {
        "onderwerpen": ["koken", "gemakkelijke recepten", "desserts", "banketbakken", "gebak", 
                   "mexicaans eten", "italiaans eten", "spaans eten", "dranken", 
                   "cocktails", "cocktails", "wijnspijs", "wijn", "ambachtelijk bier",
                   "moleculaire gastronomie", "vegetarisch koken", "veganistisch koken"]
    },
    "sport": {
        "onderwerpen": ["sport", "voetbal", "basketbal", "tennis", "zwemmen", "hardlopen", 
                   "fitness", "sportschool", "yoga", "pilates", "crossfit", "sportvoeding",
                   "functionele training", "calisthenics", "boksen", "vechtsporten"]
    },
    "bedrijf": {
        "onderwerpen": ["bedrijf", "ondernemerschap", "startups", "digitale marketing", "verkoop", 
                   "persoonlijke financien", "investeringen", "online bedrijf", "ecommerce", 
                   "logistiek", "leiderschap", "bedrijfsmanagement", "human resources",
                   "klantenservice", "branding", "seo", "sem", "email marketing"]
    }
}

# ============================================
# VOORVOEGSELS
# ============================================
voorvoegsels = [
    "hoe te leren", "hoe te beheersen", "volledige gids voor", "tutorial over", "cursus over",
    "beheersen", "begrijpen", "oefenen", "problemen oplossen van", "oefeningen over",
    "inleiding tot", "basisconcepten van", "handboek van", "theorie van",
    "voorbeelden van", "grondbeginselen van", "tips om te leren", "bronnen om te studeren",
    "lessen over", "lessen over", "hoe te verbeteren in", "hoe te gebruiken"
]

# ============================================
# ACHTERVOEGSELS
# ============================================
achtervoegsels = [
    "basis", "gemiddeld", "gevorderd", "professioneel", "compleet",
    "gemakkelijk", "snel", "voor beginners", "vanaf nul", "stap voor stap",
    "met oefeningen", "online", "gratis", "gecertificeerd", "universitair",
    "voor kinderen", "voor volwassenen", "intensief", "praktisch", "theoretisch"
]

# ============================================
# VRAGEN
# ============================================
vragen = [
    "wat is", "hoe werkt het", "waar dient het voor", "waar te leren",
    "wanneer te gebruiken", "waarom is het belangrijk", "wat zijn de voordelen van",
    "hoe lang duurt het om te leren", "wat heb ik nodig om te studeren"
]

# ============================================
# GENERATIE VAN KEYWORDS
# ============================================
keywords = set()

print("🔄 Genereer Nederlandse keywords...")

# 1. Combinaties met voorvoegsels
for voorvoegsel in voorvoegsels:
    for cat_data in onderwerpen.values():
        for onderwerp in cat_data["onderwerpen"]:
            keywords.add(f"{voorvoegsel} {onderwerp}")
        for onderwerp_spec in cat_data.get("onderwerpen_speciaal", []):
            keywords.add(f"{voorvoegsel} {onderwerp_spec}")

# 2. Combinaties met achtervoegsels
for achtervoegsel in achtervoegsels:
    for cat_data in onderwerpen.values():
        for onderwerp in cat_data["onderwerpen"][:15]:
            keywords.add(f"{onderwerp} {achtervoegsel}")
        for onderwerp_spec in cat_data.get("onderwerpen_speciaal", []):
            keywords.add(f"{onderwerp_spec} {achtervoegsel}")

# 3. Vragen
for vraag in vragen:
    for cat_data in onderwerpen.values():
        for onderwerp in cat_data["onderwerpen"][:15]:
            keywords.add(f"{vraag} {onderwerp}")
        for onderwerp_spec in cat_data.get("onderwerpen_speciaal", []):
            keywords.add(f"{vraag} {onderwerp_spec}")

# 4. Werkwoorden + onderwerp
werkwoorden = ["leren", "beheersen", "oefenen", "studeren", "begrijpen", "toepassen"]
for werkwoord in werkwoorden:
    for cat_data in onderwerpen.values():
        for onderwerp in cat_data["onderwerpen"][:15]:
            keywords.add(f"{werkwoord} {onderwerp}")

# 5. Vergelijkingen
for cat_data in onderwerpen.values():
    alle_onderwerpen = cat_data["onderwerpen"] + cat_data.get("onderwerpen_speciaal", [])
    if len(alle_onderwerpen) >= 2:
        for _ in range(min(30, len(alle_onderwerpen) * 3)):
            onderwerp1, onderwerp2 = random.sample(alle_onderwerpen, 2)
            keywords.add(f"verschil tussen {onderwerp1} en {onderwerp2}")
            keywords.add(f"{onderwerp1} vs {onderwerp2}")
            keywords.add(f"vergelijking {onderwerp1} vs {onderwerp2}")

# 6. Veelgemaakte fouten
for cat_data in onderwerpen.values():
    for onderwerp in cat_data["onderwerpen"][:10]:
        keywords.add(f"veelgemaakte fouten in {onderwerp}")
        keywords.add(f"hoe fouten te vermijden in {onderwerp}")
        keywords.add(f"oplossing voor problemen met {onderwerp}")

# 7. Cursussen en niveaus
niveaus = ["basis", "gemiddeld", "gevorderd", "professioneel", "intensief"]
for niveau in niveaus:
    for cat_data in onderwerpen.values():
        for onderwerp in cat_data["onderwerpen"][:12]:
            keywords.add(f"{niveau} cursus in {onderwerp}")
            keywords.add(f"lessen {onderwerp} {niveau} niveau")

# 8. Certificeringen en bronnen
for cat_data in onderwerpen.values():
    for onderwerp in cat_data["onderwerpen"][:10]:
        keywords.add(f"certificering in {onderwerp}")
        keywords.add(f"examen over {onderwerp}")
        keywords.add(f"boeken over {onderwerp}")
        keywords.add(f"videos over {onderwerp}")

# 9. Tips
for cat_data in onderwerpen.values():
    for onderwerp in cat_data["onderwerpen"][:10]:
        keywords.add(f"tips voor {onderwerp}")
        keywords.add(f"advies om te verbeteren in {onderwerp}")

# 10. Numerieke variaties
for i in range(1, 2000):
    cat_name = random.choice(list(onderwerpen.keys()))
    onderwerp = random.choice(onderwerpen[cat_name]["onderwerpen"])
    keywords.add(f"les {i} van {onderwerp}")
    keywords.add(f"hoofdstuk {i} van {onderwerp}")
    keywords.add(f"eenheid {i} van {onderwerp}")

# ============================================
# BEPERKEN
# ============================================
keywords_lijst = sorted(list(keywords))
random.shuffle(keywords_lijst)

if len(keywords_lijst) < AANTAL_KEYWORDS:
    print(f"⚠ Slechts {len(keywords_lijst)} keywords gegenereerd. Herhaal enkele om {AANTAL_KEYWORDS} te bereiken...")
    while len(keywords_lijst) < AANTAL_KEYWORDS:
        keywords_lijst.extend(keywords_lijst[:min(1000, AANTAL_KEYWORDS - len(keywords_lijst))])

keywords_finaal = keywords_lijst[:AANTAL_KEYWORDS]
random.shuffle(keywords_finaal)

# ============================================
# OPSLAAN
# ============================================
with open('keywords/nl.json', 'w', encoding='utf-8') as f:
    json.dump(keywords_finaal, f, indent=2, ensure_ascii=False)

# ============================================
# RAPPORT
# ============================================
print(f"\n✅ {len(keywords_finaal)} keywords gegenereerd in het Nederlands")
print(f"📁 Opgeslagen in: keywords/nl.json")
print(f"\n📊 Voorbeeld (eerste 30 keywords):")
for i, kw in enumerate(keywords_finaal[:30]):
    print(f"   {i+1}. {kw}")
