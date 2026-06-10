import json
import random

# ============================================
# KONFIGURATION
# ============================================
ANTAL_NYCKELORD = 10000

# ============================================
# ÄMNEN PÅ SVENSKA
# ============================================
amnen = {
    "matematik": {
        "amnen": ["matematik", "kalkyl", "algebra", "geometri", "trigonometri", 
                   "statistik", "sannolikhet", "derivator", "integraler", "gränsvärden", 
                   "funktioner", "matriser", "vektorer", "ekvationer", "logaritmer", 
                   "bråk", "procent", "rötter", "potenser", "polynom", 
                   "komplexa tal", "differentialekvationer", "linjär algebra",
                   "sfärisk trigonometri", "vektoranalys", "topologi", "talteori"]
    },
    "fysik": {
        "amnen": ["fysik", "mekanik", "termodynamik", "elektromagnetism", "optik", 
                   "akustik", "kinematik", "dynamik", "vätskor", "kvantfysik", 
                   "relativitetsteori", "energi", "arbete", "effekt", "rörelse", 
                   "krafter", "gravitation", "elektricitet", "magnetism", "vågor",
                   "astrofysik", "kosmologi", "kärnfysik", "molekylärfysik"]
    },
    "kemi": {
        "amnen": ["kemi", "organisk kemi", "oorganisk kemi", "analytisk kemi", 
                   "biokemi", "kemiska reaktioner", "balansering", "stökiometri", 
                   "periodiska systemet", "kemiska bindningar", "molekyler", "atomer", 
                   "kemiska föreningar", "syror", "baser", "ph", "lösningar", 
                   "gaser", "termokemi", "kvantkemi", "elektrokemi"]
    },
    "biologi": {
        "amnen": ["biologi", "cellbiologi", "molekylärbiologi", "genetik", 
                   "anatomi", "fysiologi", "ekologi", "evolution", "botanik", 
                   "zoologi", "mikrobiologi", "dna", "rna", "proteiner", "enzymer", 
                   "metabolism", "celler", "vävnader", "organ", "kroppssystem",
                   "neurovetenskap", "immunologi", "embryologi"]
    },
    "programmering": {
        "amnen": ["programmering", "python", "javascript", "java", "c++", "c#", "php", 
                   "ruby", "swift", "kotlin", "go", "rust", "html", "css", "sql", 
                   "mongodb", "git", "react", "angular", "vue", "nodejs", "django",
                   "flask", "spring boot", "laravel", "typescript", "graphql"]
    },
    "artificiell_intelligens": {
        "amnen_special": ["maskininlärning", "djupinlärning", "gpt", "llm"],
        "amnen": ["artificiell intelligens", "neuronnät", "naturlig språkbehandling", 
                   "datorseende", "chattbotar", "transformatorer", "automation",
                   "maskininlärning", "djupinlärning", "naturlig språkbehandling", "datorseende"]
    },
    "cybersäkerhet": {
        "amnen": ["cybersäkerhet", "etisk hackning", "brandväggar", "kryptering", 
                   "informationssäkerhet", "penetrationstestning", "skadlig programvara", "utpressningsprogram", 
                   "nätfiske", "social manipulering", "kryptografi", "nätverkssäkerhet",
                   "webbsäkerhet", "mobil säkerhet", "etisk hackning"]
    },
    "matlagning": {
        "amnen": ["matlagning", "enkla recept", "efterrätter", "bakning", "bakverk", 
                   "mexikansk mat", "italiensk mat", "spansk mat", "drycker", 
                   "cocktails", "cocktails", "vinparning", "vin", "hantverksöl",
                   "molekylär gastronomi", "vegetarisk matlagning", "vegansk matlagning"]
    },
    "sport": {
        "amnen": ["sport", "fotboll", "basketboll", "tennis", "simning", "löpning", 
                   "fitness", "gym", "yoga", "pilates", "crossfit", "sportnäring",
                   "funktionell träning", "kroppsviktsträning", "boxning", "kampsport"]
    },
    "företag": {
        "amnen": ["företag", "entreprenörskap", "startups", "digital marknadsföring", "försäljning", 
                   "personlig ekonomi", "investeringar", "onlineföretag", "e-handel", 
                   "logistik", "ledarskap", "företagsledning", "personalresurser",
                   "kundservice", "varumärkesbyggande", "seo", "sem", "e-postmarknadsföring"]
    }
}

# ============================================
# PREFIX
# ============================================
prefix = [
    "hur man lär sig", "hur man bemästrar", "fullständig guide till", "handledning om", "kurs i",
    "bemästra", "förstå", "öva", "lösa problem med", "övningar i",
    "introduktion till", "grundläggande koncept i", "manual för", "teori om",
    "exempel på", "grunder i", "tips för att lära sig", "resurser för att studera",
    "lektioner i", "lektioner i", "hur man förbättrar sig i", "hur man använder"
]

# ============================================
# SUFFIX
# ============================================
suffix = [
    "nybörjare", "medelnivå", "avancerad", "professionell", "komplett",
    "enkel", "snabb", "för nybörjare", "från grunden", "steg för steg",
    "med övningar", "online", "gratis", "certifierad", "universitetsnivå",
    "för barn", "för vuxna", "intensiv", "praktisk", "teoretisk"
]

# ============================================
# FRÅGOR
# ============================================
fragor = [
    "vad är", "hur fungerar", "vad används det till", "var lär man sig",
    "när ska man använda", "varför är det viktigt", "vilka är fördelarna med",
    "hur lång tid tar det att lära sig", "vad behöver jag för att studera"
]

# ============================================
# GENERERA NYCKELORD
# ============================================
nyckelord = set()

print("🔄 Genererar svenska nyckelord...")

# 1. Kombinationer med prefix
for pre in prefix:
    for cat_data in amnen.values():
        for amne in cat_data["amnen"]:
            nyckelord.add(f"{pre} {amne}")
        for amne_special in cat_data.get("amnen_special", []):
            nyckelord.add(f"{pre} {amne_special}")

# 2. Kombinationer med suffix
for suf in suffix:
    for cat_data in amnen.values():
        for amne in cat_data["amnen"][:15]:
            nyckelord.add(f"{amne} {suf}")
        for amne_special in cat_data.get("amnen_special", []):
            nyckelord.add(f"{amne_special} {suf}")

# 3. Frågor
for fraga in fragor:
    for cat_data in amnen.values():
        for amne in cat_data["amnen"][:15]:
            nyckelord.add(f"{fraga} {amne}")
        for amne_special in cat_data.get("amnen_special", []):
            nyckelord.add(f"{fraga} {amne_special}")

# 4. Verb + ämne
verb = ["lär", "bemästra", "öva", "studera", "förstå", "tillämpa"]
for v in verb:
    for cat_data in amnen.values():
        for amne in cat_data["amnen"][:15]:
            nyckelord.add(f"{v} {amne}")

# 5. Jämförelser
for cat_data in amnen.values():
    alla_amnen = cat_data["amnen"] + cat_data.get("amnen_special", [])
    if len(alla_amnen) >= 2:
        for _ in range(min(30, len(alla_amnen) * 3)):
            amne1, amne2 = random.sample(alla_amnen, 2)
            nyckelord.add(f"skillnad mellan {amne1} och {amne2}")
            nyckelord.add(f"{amne1} vs {amne2}")
            nyckelord.add(f"jämförelse {amne1} och {amne2}")

# 6. Vanliga misstag
for cat_data in amnen.values():
    for amne in cat_data["amnen"][:10]:
        nyckelord.add(f"vanliga misstag i {amne}")
        nyckelord.add(f"hur man undviker misstag i {amne}")
        nyckelord.add(f"lösning på problem med {amne}")

# 7. Kurser och nivåer
nivaer = ["nybörjare", "medelnivå", "avancerad", "professionell", "intensiv"]
for niva in nivaer:
    for cat_data in amnen.values():
        for amne in cat_data["amnen"][:12]:
            nyckelord.add(f"{niva} kurs i {amne}")
            nyckelord.add(f"{amne} {niva} nivå lektioner")

# 8. Certifieringar och resurser
for cat_data in amnen.values():
    for amne in cat_data["amnen"][:10]:
        nyckelord.add(f"certifiering i {amne}")
        nyckelord.add(f"examen i {amne}")
        nyckelord.add(f"böcker om {amne}")
        nyckelord.add(f"videor om {amne}")

# 9. Tips
for cat_data in amnen.values():
    for amne in cat_data["amnen"][:10]:
        nyckelord.add(f"tips för {amne}")
        nyckelord.add(f"råd för att förbättra sig i {amne}")

# 10. Numeriska varianter
for i in range(1, 2000):
    cat_name = random.choice(list(amnen.keys()))
    amne = random.choice(amnen[cat_name]["amnen"])
    nyckelord.add(f"{amne} lektion {i}")
    nyckelord.add(f"{amne} kapitel {i}")
    nyckelord.add(f"{amne} enhet {i}")

# ============================================
# BEGRÄNSA
# ============================================
nyckelord_lista = sorted(list(nyckelord))
random.shuffle(nyckelord_lista)

if len(nyckelord_lista) < ANTAL_NYCKELORD:
    print(f"⚠ Endast {len(nyckelord_lista)} nyckelord genererades. Upprepar några för att nå {ANTAL_NYCKELORD}...")
    while len(nyckelord_lista) < ANTAL_NYCKELORD:
        nyckelord_lista.extend(nyckelord_lista[:min(1000, ANTAL_NYCKELORD - len(nyckelord_lista))])

slutliga_nyckelord = nyckelord_lista[:ANTAL_NYCKELORD]
random.shuffle(slutliga_nyckelord)

# ============================================
# SPARA
# ============================================
with open('keywords/sv.json', 'w', encoding='utf-8') as f:
    json.dump(slutliga_nyckelord, f, indent=2, ensure_ascii=False)

# ============================================
# RAPPORT
# ============================================
print(f"\n✅ {len(slutliga_nyckelord)} svenska nyckelord genererades")
print(f"📁 Sparades i: keywords/sv.json")
print(f"\n📊 Förhandsvisning (första 30 nyckelorden):")
for i, kw in enumerate(slutliga_nyckelord[:30]):
    print(f"   {i+1}. {kw}")

