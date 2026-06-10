import json
import random

# ============================================
# KONFIGURÁCIÓ
# ============================================
KULCSSZAVAK_SZÁMA = 10000

# ============================================
# TÉMÁK MAGYARUL
# ============================================
témák = {
    "matematika": {
        "témák": ["matematika", "kalkulus", "algebra", "geometria", "trigonometria", 
                   "statisztika", "valószínűségszámítás", "deriváltak", "integrálok", "határértékek", 
                   "függvények", "mátrixok", "vektorok", "egyenletek", "logaritmusok", 
                   "törtek", "százalékok", "gyökök", "hatványok", "polinomok", 
                   "komplex számok", "differenciálegyenletek", "lineáris algebra",
                   "gömbi trigonometria", "vektoranalízis", "topológia", "számelmélet"]
    },
    "fizika": {
        "témák": ["fizika", "mechanika", "termodinamika", "elektromágnesség", "optika", 
                   "akusztika", "kinematika", "dinamika", "folyadékok", "kvantumfizika", 
                   "relativitáselmélet", "energia", "munka", "teljesítmény", "mozgás", 
                   "erők", "gravitáció", "elektromosság", "mágnesség", "hullámok",
                   "asztrofizika", "kozmológia", "magfizika", "molekuláris fizika"]
    },
    "kémia": {
        "témák": ["kémia", "szerves kémia", "szervetlen kémia", "analitikai kémia", 
                   "biokémia", "kémiai reakciók", "egyensúlyozás", "sztöchiometria", 
                   "periódusos rendszer", "kémiai kötések", "molekulák", "atomok", 
                   "kémiai vegyületek", "savak", "bázisok", "ph", "oldatok", 
                   "gázok", "termokémia", "kvantumkémia", "elektrokémia"]
    },
    "biológia": {
        "témák": ["biológia", "sejtbiológia", "molekuláris biológia", "genetika", 
                   "anatómia", "fiziológia", "ökológia", "evolúció", "botanika", 
                   "zoológia", "mikrobiológia", "dns", "rns", "fehérjék", "enzimek", 
                   "anyagcsere", "sejtek", "szövetek", "szervek", "testrendszerek",
                   "idegtudomány", "immunológia", "embriológia"]
    },
    "programozás": {
        "témák": ["programozás", "python", "javascript", "java", "c++", "c#", "php", 
                   "ruby", "swift", "kotlin", "go", "rust", "html", "css", "sql", 
                   "mongodb", "git", "react", "angular", "vue", "nodejs", "django",
                   "flask", "spring boot", "laravel", "typescript", "graphql"]
    },
    "mesterséges_intelligencia": {
        "témák_különleges": ["gépi tanulás", "mély tanulás", "gpt", "llm"],
        "témák": ["mesterséges intelligencia", "neurális hálózatok", "természetes nyelvfeldolgozás", 
                   "számítógépes látás", "chatbotok", "transzformátorok", "automatizálás",
                   "gépi tanulás", "mély tanulás", "természetes nyelvfeldolgozás", "számítógépes látás"]
    },
    "kiberbiztonság": {
        "témák": ["kiberbiztonság", "etikus hackelés", "tűzfalak", "titkosítás", 
                   "információbiztonság", "behatolási tesztelés", "rosszindulatú szoftver", "zsarolóvírus", 
                   "adathalászat", "társadalmi manipuláció", "kriptográfia", "hálózati biztonság",
                   "webes biztonság", "mobil biztonság", "etikus hackelés"]
    },
    "főzés": {
        "témák": ["főzés", "egyszerű receptek", "desszertek", "sütés", "pékáruk", 
                   "mexikói konyha", "olasz konyha", "spanyol konyha", "italok", 
                   "koktélok", "koktélok", "bor párosítás", "bor", "kézműves sör",
                   "molekuláris gasztronómia", "vegetáriánus főzés", "vegán főzés"]
    },
    "sport": {
        "témák": ["sport", "futball", "kosárlabda", "tenisz", "úszás", "futás", 
                   "fitnesz", "edzőterem", "jóga", "pilates", "crossfit", "sporttáplálkozás",
                   "funkcionális edzés", "saját testsúlyos edzés", "boksz", "harcművészetek"]
    },
    "üzlet": {
        "témák": ["üzlet", "vállalkozás", "induló vállalkozások", "digitális marketing", "értékesítés", 
                   "személyes pénzügyek", "befektetések", "online üzlet", "e-kereskedelem", 
                   "logisztika", "vezetés", "üzletvezetés", "emberi erőforrások",
                   "ügyfélszolgálat", "márkaépítés", "seo", "sem", "email marketing"]
    }
}

# ============================================
# ELŐTAGOK
# ============================================
előtagok = [
    "hogyan tanulj", "hogyan sajátíts el", "teljes útmutató", "oktatóanyag", "tanfolyam",
    "sajátíts el", "értsd meg", "gyakorolj", "problémák megoldása", "gyakorlatok",
    "bevezetés", "alapfogalmak", "kézikönyv", "elmélet",
    "példák", "alapok", "tippek a tanuláshoz", "források a tanuláshoz",
    "leckék", "leckék", "hogyan fejlődj", "hogyan használd"
]

# ============================================
# UTÓTAGOK
# ============================================
utótagok = [
    "kezdő", "középhaladó", "haladó", "profi", "teljes",
    "könnyű", "gyors", "kezdőknek", "nulláról", "lépésről lépésre",
    "gyakorlatokkal", "online", "ingyenes", "tanúsított", "egyetemi szint",
    "gyerekeknek", "felnőtteknek", "intenzív", "gyakorlati", "elméleti"
]

# ============================================
# KÉRDÉSEK
# ============================================
kérdések = [
    "mi az", "hogyan működik", "mire való", "hol tanuljam",
    "mikor használjam", "miért fontos", "mik az előnyei",
    "mennyi ideig tart megtanulni", "mire van szükségem a tanuláshoz"
]

# ============================================
# KULCSSZAVAK GENERÁLÁSA
# ============================================
kulcsszavak = set()

print("🔄 Magyar kulcsszavak generálása...")

for előtag in előtagok:
    for cat_data in témák.values():
        for téma in cat_data["témák"]:
            kulcsszavak.add(f"{előtag} {téma}")
        for téma_különleges in cat_data.get("témák_különleges", []):
            kulcsszavak.add(f"{előtag} {téma_különleges}")

for utótag in utótagok:
    for cat_data in témák.values():
        for téma in cat_data["témák"][:15]:
            kulcsszavak.add(f"{téma} {utótag}")
        for téma_különleges in cat_data.get("témák_különleges", []):
            kulcsszavak.add(f"{téma_különleges} {utótag}")

for kérdés in kérdések:
    for cat_data in témák.values():
        for téma in cat_data["témák"][:15]:
            kulcsszavak.add(f"{kérdés} {téma}")
        for téma_különleges in cat_data.get("témák_különleges", []):
            kulcsszavak.add(f"{kérdés} {téma_különleges}")

igék = ["tanulj", "sajátíts el", "gyakorolj", "tanulmányozd", "értsd meg", "alkalmazd"]
for ige in igék:
    for cat_data in témák.values():
        for téma in cat_data["témák"][:15]:
            kulcsszavak.add(f"{ige} {téma}")

for cat_data in témák.values():
    összes_téma = cat_data["témák"] + cat_data.get("témák_különleges", [])
    if len(összes_téma) >= 2:
        for _ in range(min(30, len(összes_téma) * 3)):
            téma1, téma2 = random.sample(összes_téma, 2)
            kulcsszavak.add(f"különbség {téma1} és {téma2} között")
            kulcsszavak.add(f"{téma1} vs {téma2}")
            kulcsszavak.add(f"{téma1} és {téma2} összehasonlítása")

for cat_data in témák.values():
    for téma in cat_data["témák"][:10]:
        kulcsszavak.add(f"gyakori hibák a {téma} témakörben")
        kulcsszavak.add(f"hogyan kerüljük el a hibákat a {téma} témakörben")
        kulcsszavak.add(f"megoldás a {téma} problémákra")

szintek = ["kezdő", "középhaladó", "haladó", "profi", "intenzív"]
for szint in szintek:
    for cat_data in témák.values():
        for téma in cat_data["témák"][:12]:
            kulcsszavak.add(f"{szint} {téma} tanfolyam")
            kulcsszavak.add(f"{téma} {szint} szintű leckék")

for cat_data in témák.values():
    for téma in cat_data["témák"][:10]:
        kulcsszavak.add(f"tanúsítvány a {téma} témakörben")
        kulcsszavak.add(f"{téma} vizsga")
        kulcsszavak.add(f"{téma} könyvek")
        kulcsszavak.add(f"{téma} videók")

for cat_data in témák.values():
    for téma in cat_data["témák"][:10]:
        kulcsszavak.add(f"tippek a {téma} témakörhöz")
        kulcsszavak.add(f"tanácsok a {téma} fejlesztéséhez")

for i in range(1, 2000):
    cat_name = random.choice(list(témák.keys()))
    téma = random.choice(témák[cat_name]["témák"])
    kulcsszavak.add(f"{téma} lecke {i}")
    kulcsszavak.add(f"{téma} fejezet {i}")
    kulcsszavak.add(f"{téma} egység {i}")

# ============================================
# KORLÁTOZÁS
# ============================================
kulcsszó_lista = sorted(list(kulcsszavak))
random.shuffle(kulcsszó_lista)

if len(kulcsszó_lista) < KULCSSZAVAK_SZÁMA:
    print(f"⚠ Csak {len(kulcsszó_lista)} kulcsszó generálódott. Néhány ismétlése a {KULCSSZAVAK_SZÁMA} eléréséhez...")
    while len(kulcsszó_lista) < KULCSSZAVAK_SZÁMA:
        kulcsszó_lista.extend(kulcsszó_lista[:min(1000, KULCSSZAVAK_SZÁMA - len(kulcsszó_lista))])

végleges_kulcsszavak = kulcsszó_lista[:KULCSSZAVAK_SZÁMA]
random.shuffle(végleges_kulcsszavak)

# ============================================
# MENTÉS
# ============================================
with open('keywords/hu.json', 'w', encoding='utf-8') as f:
    json.dump(végleges_kulcsszavak, f, indent=2, ensure_ascii=False)

# ============================================
# JELENTÉS
# ============================================
print(f"\n✅ {len(végleges_kulcsszavak)} magyar kulcsszó generálódott")
print(f"📁 Mentve: keywords/hu.json")
print(f"\n📊 Előnézet (az első 30 kulcsszó):")
for i, kw in enumerate(végleges_kulcsszavak[:30]):
    print(f"   {i+1}. {kw}")
