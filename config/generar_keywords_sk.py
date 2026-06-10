import json
import random

# ============================================
# KONFIGURÁCIA
# ============================================
POČET_KĽÚČOVÝCH_SLOV = 10000

# ============================================
# TÉMY V SLOVENČINE
# ============================================
témy = {
    "matematika": {
        "témy": ["matematika", "kalkulus", "algebra", "geometria", "trigonometria", 
                   "štatistika", "pravdepodobnosť", "deriváty", "integrály", "limity", 
                   "funkcie", "matice", "vektory", "rovnice", "logaritmy", 
                   "zlomky", "percentá", "odmocniny", "mocniny", "polynómy", 
                   "komplexné čísla", "diferenciálne rovnice", "lineárna algebra",
                   "sférická trigonometria", "vektorový počet", "topológia", "teória čísel"]
    },
    "fyzika": {
        "témy": ["fyzika", "mechanika", "termodynamika", "elektromagnetizmus", "optika", 
                   "akustika", "kinematika", "dynamika", "tekutiny", "kvantová fyzika", 
                   "teória relativity", "energia", "práca", "výkon", "pohyb", 
                   "sily", "gravitácia", "elektrina", "magnetizmus", "vlny",
                   "astrofyzika", "kozmológia", "jadrová fyzika", "molekulárna fyzika"]
    },
    "chémia": {
        "témy": ["chémia", "organická chémia", "anorganická chémia", "analytická chémia", 
                   "biochémia", "chemické reakcie", "vyrovnávanie", "stechiometria", 
                   "periodická tabuľka", "chemické väzby", "molekuly", "atómy", 
                   "chemické zlúčeniny", "kyseliny", "zásady", "ph", "roztoky", 
                   "plyny", "termochémia", "kvantová chémia", "elektrochémia"]
    },
    "biológia": {
        "témy": ["biológia", "bunková biológia", "molekulárna biológia", "genetika", 
                   "anatória", "fyziológia", "ekológia", "evolúcia", "botanika", 
                   "zoológia", "mikrobiológia", "dna", "rna", "proteíny", "enzýmy", 
                   "metabolizmus", "bunky", "tkanivá", "orgány", "telesné systémy",
                   "neuroveda", "imunológia", "embryológia"]
    },
    "programovanie": {
        "témy": ["programovanie", "python", "javascript", "java", "c++", "c#", "php", 
                   "ruby", "swift", "kotlin", "go", "rust", "html", "css", "sql", 
                   "mongodb", "git", "react", "angular", "vue", "nodejs", "django",
                   "flask", "spring boot", "laravel", "typescript", "graphql"]
    },
    "umelá_inteligencia": {
        "témy_špeciálne": ["strojové učenie", "hlboké učenie", "gpt", "llm"],
        "témy": ["umelá inteligencia", "neuronové siete", "spracovanie prirodzeného jazyka", 
                   "počítačové videnie", "chatboty", "transformátory", "automatizácia",
                   "strojové učenie", "hlboké učenie", "spracovanie prirodzeného jazyka", "počítačové videnie"]
    },
    "kybernetická_bezpečnosť": {
        "témy": ["kybernetická bezpečnosť", "etické hackovanie", "firewally", "šifrovanie", 
                   "informačná bezpečnosť", "penetračné testovanie", "malvér", "ransomvér", 
                   "phishing", "sociálne inžinierstvo", "kryptografia", "sieťová bezpečnosť",
                   "webová bezpečnosť", "mobilná bezpečnosť", "etické hackovanie"]
    },
    "varenie": {
        "témy": ["varenie", "jednoduché recepty", "dezerty", "pečenie", "pečivo", 
                   "mexická kuchyňa", "talianska kuchyňa", "španielska kuchyňa", "nápoje", 
                   "koktaily", "koktaily", "párovanie vína", "víno", "remeselné pivo",
                   "molekulárna gastronómia", "vegetariánske varenie", "vegánske varenie"]
    },
    "šport": {
        "témy": ["šport", "futbal", "basketbal", "tenis", "plávanie", "beh", 
                   "fitness", "posilňovňa", "joga", "pilates", "crossfit", "športová výživa",
                   "funkčný tréning", "kalistenika", "box", "bojové umenia"]
    },
    "podnikanie": {
        "témy": ["podnikanie", "podnikavosť", "startupy", "digitálny marketing", "predaj", 
                   "osobné financie", "investície", "online podnikanie", "e-commerce", 
                   "logistika", "vodcovstvo", "riadenie podniku", "ľudské zdroje",
                   "zákaznícky servis", "budovanie značky", "seo", "sem", "email marketing"]
    }
}

# ============================================
# PREDPONY
# ============================================
predpony = [
    "ako sa naučiť", "ako ovládnuť", "kompletný sprievodca", "tutoriál", "kurz",
    "ovládnuť", "pochopiť", "cvičiť", "riešiť problémy", "cvičenia",
    "úvod do", "základné pojmy", "príručka", "teória",
    "príklady", "základy", "tipy na učenie", "zdroje na štúdium",
    "lekcie", "lekcie", "ako sa zlepšiť v", "ako používať"
]

# ============================================
# PRÍPONY
# ============================================
prípony = [
    "začiatočník", "stredne pokročilý", "pokročilý", "profesionálny", "kompletný",
    "jednoduchý", "rýchly", "pre začiatočníkov", "od nuly", "krok za krokom",
    "s cvičeniami", "online", "zadarmo", "certifikovaný", "univerzitná úroveň",
    "pre deti", "pre dospelých", "intenzívny", "praktický", "teoretický"
]

# ============================================
# OTÁZKY
# ============================================
otázky = [
    "čo je", "ako funguje", "na čo slúži", "kde sa naučiť",
    "kedy použiť", "prečo je dôležité", "aké sú výhody",
    "ako dlho trvá sa to naučiť", "čo potrebujem na štúdium"
]

# ============================================
# GENEROVANIE KĽÚČOVÝCH SLOV
# ============================================
kľúčové_slová = set()

print("🔄 Generovanie slovenských kľúčových slov...")

for predpona in predpony:
    for cat_data in témy.values():
        for téma in cat_data["témy"]:
            kľúčové_slová.add(f"{predpona} {téma}")
        for téma_špeciálna in cat_data.get("témy_špeciálne", []):
            kľúčové_slová.add(f"{predpona} {téma_špeciálna}")

for prípona in prípony:
    for cat_data in témy.values():
        for téma in cat_data["témy"][:15]:
            kľúčové_slová.add(f"{téma} {prípona}")
        for téma_špeciálna in cat_data.get("témy_špeciálne", []):
            kľúčové_slová.add(f"{téma_špeciálna} {prípona}")

for otázka in otázky:
    for cat_data in témy.values():
        for téma in cat_data["témy"][:15]:
            kľúčové_slová.add(f"{otázka} {téma}")
        for téma_špeciálna in cat_data.get("témy_špeciálne", []):
            kľúčové_slová.add(f"{otázka} {téma_špeciálna}")

slovesá = ["nauč sa", "ovládni", "cvič", "študuj", "pochop", "aplikuj"]
for sloveso in slovesá:
    for cat_data in témy.values():
        for téma in cat_data["témy"][:15]:
            kľúčové_slová.add(f"{sloveso} {téma}")

for cat_data in témy.values():
    všetky_témy = cat_data["témy"] + cat_data.get("témy_špeciálne", [])
    if len(všetky_témy) >= 2:
        for _ in range(min(30, len(všetky_témy) * 3)):
            téma1, téma2 = random.sample(všetky_témy, 2)
            kľúčové_slová.add(f"rozdiel medzi {téma1} a {téma2}")
            kľúčové_slová.add(f"{téma1} vs {téma2}")
            kľúčové_slová.add(f"porovnanie {téma1} a {téma2}")

for cat_data in témy.values():
    for téma in cat_data["témy"][:10]:
        kľúčové_slová.add(f"časté chyby v {téma}")
        kľúčové_slová.add(f"ako sa vyhnúť chybám v {téma}")
        kľúčové_slová.add(f"riešenie problémov s {téma}")

úrovne = ["začiatočník", "stredne pokročilý", "pokročilý", "profesionálny", "intenzívny"]
for úroveň in úrovne:
    for cat_data in témy.values():
        for téma in cat_data["témy"][:12]:
            kľúčové_slová.add(f"{úroveň} kurz {téma}")
            kľúčové_slová.add(f"{téma} {úroveň} úroveň lekcie")

for cat_data in témy.values():
    for téma in cat_data["témy"][:10]:
        kľúčové_slová.add(f"certifikácia v {téma}")
        kľúčové_slová.add(f"skúška z {téma}")
        kľúčové_slová.add(f"knihy o {téma}")
        kľúčové_slová.add(f"videá o {téma}")

for cat_data in témy.values():
    for téma in cat_data["témy"][:10]:
        kľúčové_slová.add(f"tipy pre {téma}")
        kľúčové_slová.add(f"rady ako sa zlepšiť v {téma}")

for i in range(1, 2000):
    cat_name = random.choice(list(témy.keys()))
    téma = random.choice(témy[cat_name]["témy"])
    kľúčové_slová.add(f"{téma} lekcia {i}")
    kľúčové_slová.add(f"{téma} kapitola {i}")
    kľúčové_slová.add(f"{téma} jednotka {i}")

# ============================================
# OBMEDZENIE
# ============================================
zoznam_kľúčových_slov = sorted(list(kľúčové_slová))
random.shuffle(zoznam_kľúčových_slov)

if len(zoznam_kľúčových_slov) < POČET_KĽÚČOVÝCH_SLOV:
    print(f"⚠ Vygenerovalo sa iba {len(zoznam_kľúčových_slov)} kľúčových slov. Opakujeme niektoré na dosiahnutie {POČET_KĽÚČOVÝCH_SLOV}...")
    while len(zoznam_kľúčových_slov) < POČET_KĽÚČOVÝCH_SLOV:
        zoznam_kľúčových_slov.extend(zoznam_kľúčových_slov[:min(1000, POČET_KĽÚČOVÝCH_SLOV - len(zoznam_kľúčových_slov))])

konečné_kľúčové_slová = zoznam_kľúčových_slov[:POČET_KĽÚČOVÝCH_SLOV]
random.shuffle(konečné_kľúčové_slová)

# ============================================
# ULOŽENIE
# ============================================
with open('keywords/sk.json', 'w', encoding='utf-8') as f:
    json.dump(konečné_kľúčové_slová, f, indent=2, ensure_ascii=False)

# ============================================
# SPRÁVA
# ============================================
print(f"\n✅ {len(konečné_kľúčové_slová)} slovenských kľúčových slov bolo vygenerovaných")
print(f"📁 Uložené v: keywords/sk.json")
print(f"\n📊 Náhľad (prvých 30 kľúčových slov):")
for i, kw in enumerate(konečné_kľúčové_slová[:30]):
    print(f"   {i+1}. {kw}")
