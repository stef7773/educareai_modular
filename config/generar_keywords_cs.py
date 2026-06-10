import json
import random

# ============================================
# KONFIGURACE
# ============================================
POCET_KLICOVYCH_SLOV = 10000

# ============================================
# TÉMATA V ČEŠTINĚ
# ============================================
témata = {
    "matematika": {
        "témata": ["matematika", "kalkulus", "algebra", "geometrie", "trigonometrie", 
                   "statistika", "pravděpodobnost", "derivace", "integrály", "limity", 
                   "funkce", "matice", "vektory", "rovnice", "logaritmy", 
                   "zlomky", "procenta", "odmocniny", "mocniny", "polynomy", 
                   "komplexní čísla", "diferenciální rovnice", "lineární algebra",
                   "sférická trigonometrie", "vektorový počet", "topologie", "teorie čísel"]
    },
    "fyzika": {
        "témata": ["fyzika", "mechanika", "termodynamika", "elektromagnetismus", "optika", 
                   "akustika", "kinematika", "dynamika", "tekutiny", "kvantová fyzika", 
                   "teorie relativity", "energie", "práce", "výkon", "pohyb", 
                   "síly", "gravitace", "elektřina", "magnetismus", "vlny",
                   "astrofyzika", "kosmologie", "jaderná fyzika", "molekulární fyzika"]
    },
    "chemie": {
        "témata": ["chemie", "organická chemie", "anorganická chemie", "analytická chemie", 
                   "biochemie", "chemické reakce", "vyrovnávání", "stechiometrie", 
                   "periodická tabulka", "chemické vazby", "molekuly", "atomy", 
                   "chemické sloučeniny", "kyseliny", "zásady", "ph", "roztoky", 
                   "plyny", "termochemie", "kvantová chemie", "elektrochemie"]
    },
    "biologie": {
        "témata": ["biologie", "buněčná biologie", "molekulární biologie", "genetika", 
                   "anatomie", "fyziologie", "ekologie", "evoluce", "botanika", 
                   "zoologie", "mikrobiologie", "dna", "rna", "bílkoviny", "enzymy", 
                   "metabolismus", "buňky", "tkáně", "orgány", "tělesné systémy",
                   "neurověda", "imunologie", "embryologie"]
    },
    "programování": {
        "témata": ["programování", "python", "javascript", "java", "c++", "c#", "php", 
                   "ruby", "swift", "kotlin", "go", "rust", "html", "css", "sql", 
                   "mongodb", "git", "react", "angular", "vue", "nodejs", "django",
                   "flask", "spring boot", "laravel", "typescript", "graphql"]
    },
    "umělá_inteligence": {
        "témata_speciální": ["strojové učení", "hluboké učení", "gpt", "llm"],
        "témata": ["umělá inteligence", "neuronové sítě", "zpracování přirozeného jazyka", 
                   "počítačové vidění", "chatboti", "transformátory", "automatizace",
                   "strojové učení", "hluboké učení", "zpracování přirozeného jazyka", "počítačové vidění"]
    },
    "kybernetická_bezpečnost": {
        "témata": ["kybernetická bezpečnost", "etické hackování", "firewally", "šifrování", 
                   "informační bezpečnost", "penetrační testování", "malware", "ransomware", 
                   "phishing", "sociální inženýrství", "kryptografie", "bezpečnost sítě",
                   "webová bezpečnost", "mobilní bezpečnost", "etické hackování"]
    },
    "vaření": {
        "témata": ["vaření", "snadné recepty", "dezerty", "pečení", "pečivo", 
                   "mexická kuchyně", "italská kuchyně", "španělská kuchyně", "nápoje", 
                   "koktejly", "koktejly", "párování vína", "víno", "řemeslné pivo",
                   "molekulární gastronomie", "vegetariánské vaření", "veganské vaření"]
    },
    "sport": {
        "témata": ["sport", "fotbal", "basketbal", "tenis", "plavání", "běh", 
                   "fitness", "posilovna", "jóga", "pilates", "crossfit", "sportovní výživa",
                   "funkční trénink", "kalistenika", "box", "bojová umění"]
    },
    "podnikání": {
        "témata": ["podnikání", "podnikavost", "startupy", "digitální marketing", "prodej", 
                   "osobní finance", "investice", "online podnikání", "e-commerce", 
                   "logistika", "vedení", "řízení podniku", "lidské zdroje",
                   "zákaznický servis", "budování značky", "seo", "sem", "email marketing"]
    }
}

# ============================================
# PŘEDPONY
# ============================================
předpony = [
    "jak se naučit", "jak ovládnout", "kompletní průvodce", "tutoriál", "kurz",
    "ovládnout", "porozumět", "cvičit", "řešit problémy", "cvičení",
    "úvod do", "základní pojmy", "příručka", "teorie",
    "příklady", "základy", "tipy jak se naučit", "zdroje ke studiu",
    "lekce", "lekce", "jak se zlepšit v", "jak používat"
]

# ============================================
# PŘÍPONY
# ============================================
přípony = [
    "začátečník", "středně pokročilý", "pokročilý", "profesionální", "kompletní",
    "snadný", "rychlý", "pro začátečníky", "od nuly", "krok za krokem",
    "s cvičeními", "online", "zdarma", "certifikovaný", "univerzitní úroveň",
    "pro děti", "pro dospělé", "intenzivní", "praktický", "teoretický"
]

# ============================================
# OTÁZKY
# ============================================
otázky = [
    "co je", "jak to funguje", "k čemu to je", "kde se naučit",
    "kdy použít", "proč je to důležité", "jaké jsou výhody",
    "jak dlouho trvá se to naučit", "co potřebuji ke studiu"
]

# ============================================
# GENEROVÁNÍ KLÍČOVÝCH SLOV
# ============================================
klíčová_slova = set()

print("🔄 Generuji česká klíčová slova...")

for předpona in předpony:
    for cat_data in témata.values():
        for téma in cat_data["témata"]:
            klíčová_slova.add(f"{předpona} {téma}")
        for téma_speciální in cat_data.get("témata_speciální", []):
            klíčová_slova.add(f"{předpona} {téma_speciální}")

for přípona in přípony:
    for cat_data in témata.values():
        for téma in cat_data["témata"][:15]:
            klíčová_slova.add(f"{téma} {přípona}")
        for téma_speciální in cat_data.get("témata_speciální", []):
            klíčová_slova.add(f"{téma_speciální} {přípona}")

for otázka in otázky:
    for cat_data in témata.values():
        for téma in cat_data["témata"][:15]:
            klíčová_slova.add(f"{otázka} {téma}")
        for téma_speciální in cat_data.get("témata_speciální", []):
            klíčová_slova.add(f"{otázka} {téma_speciální}")

slovesa = ["nauč se", "ovládni", "cvič", "studuj", "pochop", "aplikuj"]
for sloveso in slovesa:
    for cat_data in témata.values():
        for téma in cat_data["témata"][:15]:
            klíčová_slova.add(f"{sloveso} {téma}")

for cat_data in témata.values():
    všechna_témata = cat_data["témata"] + cat_data.get("témata_speciální", [])
    if len(všechna_témata) >= 2:
        for _ in range(min(30, len(všechna_témata) * 3)):
            téma1, téma2 = random.sample(všechna_témata, 2)
            klíčová_slova.add(f"rozdíl mezi {téma1} a {téma2}")
            klíčová_slova.add(f"{téma1} vs {téma2}")
            klíčová_slova.add(f"srovnání {téma1} a {téma2}")

for cat_data in témata.values():
    for téma in cat_data["témata"][:10]:
        klíčová_slova.add(f"časté chyby v {téma}")
        klíčová_slova.add(f"jak se vyhnout chybám v {téma}")
        klíčová_slova.add(f"řešení problémů s {téma}")

úrovně = ["začátečník", "středně pokročilý", "pokročilý", "profesionální", "intenzivní"]
for úroveň in úrovně:
    for cat_data in témata.values():
        for téma in cat_data["témata"][:12]:
            klíčová_slova.add(f"{úroveň} kurz {téma}")
            klíčová_slova.add(f"{téma} {úroveň} úroveň lekce")

for cat_data in témata.values():
    for téma in cat_data["témata"][:10]:
        klíčová_slova.add(f"certifikace v {téma}")
        klíčová_slova.add(f"zkouška z {téma}")
        klíčová_slova.add(f"knihy o {téma}")
        klíčová_slova.add(f"videa o {téma}")

for cat_data in témata.values():
    for téma in cat_data["témata"][:10]:
        klíčová_slova.add(f"tipy pro {téma}")
        klíčová_slova.add(f"rady jak se zlepšit v {téma}")

for i in range(1, 2000):
    cat_name = random.choice(list(témata.keys()))
    téma = random.choice(témata[cat_name]["témata"])
    klíčová_slova.add(f"{téma} lekce {i}")
    klíčová_slova.add(f"{téma} kapitola {i}")
    klíčová_slova.add(f"{téma} jednotka {i}")

# ============================================
# OMEZENÍ
# ============================================
seznam_slov = sorted(list(klíčová_slova))
random.shuffle(seznam_slov)

if len(seznam_slov) < POCET_KLICOVYCH_SLOV:
    print(f"⚠ Vygenerováno pouze {len(seznam_slov)} klíčových slov. Opakuji některá pro dosažení {POCET_KLICOVYCH_SLOV}...")
    while len(seznam_slov) < POCET_KLICOVYCH_SLOV:
        seznam_slov.extend(seznam_slov[:min(1000, POCET_KLICOVYCH_SLOV - len(seznam_slov))])

konečná_slova = seznam_slov[:POCET_KLICOVYCH_SLOV]
random.shuffle(konečná_slova)

# ============================================
# ULOŽENÍ
# ============================================
with open('keywords/cs.json', 'w', encoding='utf-8') as f:
    json.dump(konečná_slova, f, indent=2, ensure_ascii=False)

# ============================================
# ZPRÁVA
# ============================================
print(f"\n✅ {len(konečná_slova)} českých klíčových slov vygenerováno")
print(f"📁 Uloženo v: keywords/cs.json")
print(f"\n📊 Náhled (prvních 30 klíčových slov):")
for i, kw in enumerate(konečná_slova[:30]):
    print(f"   {i+1}. {kw}")
