import json
import random

# ============================================
# KONFIGURACIJA
# ============================================
RAKTINŽODŽIŲ_SKAIČIUS = 10000

# ============================================
# TEMOS LIETUVIŲ KALBA
# ============================================
temOS = {
    "matematika": {
        "temos": ["matematika", "kalkuliatorius", "algebra", "geometrija", "trigonometrija", 
                   "statistika", "tikimybė", "išvestinės", "integralai", "ribos", 
                   "funkcijos", "matricos", "vektoriai", "lygtys", "logaritmai", 
                   "trupmenos", "procentai", "šaknys", "laipsniai", "polinomai", 
                   "kompleksiniai skaičiai", "diferencialinės lygtys", "tiesinė algebra",
                   "sferinė trigonometrija", "vektorinis skaičiavimas", "topologija", "skaičių teorija"]
    },
    "fizika": {
        "temos": ["fizika", "mechanika", "termodinamika", "elektromagnetizmas", "optika", 
                   "akustika", "kinematika", "dinamika", "skysčiai", "kvantinė fizika", 
                   "reliatyvumo teorija", "energija", "darbas", "galia", "judėjimas", 
                   "jėgos", "gravitacija", "elektra", "magnetizmas", "bangos",
                   "astrofizika", "kosmologija", "branduolinė fizika", "molekulinė fizika"]
    },
    "chemija": {
        "temos": ["chemija", "organinė chemija", "neorganinė chemija", "analizinė chemija", 
                   "biochemija", "cheminės reakcijos", "balansavimas", "stechiometrija", 
                   "periodinė lentelė", "cheminiai ryšiai", "molekulės", "atomai", 
                   "cheminiai junginiai", "rūgštys", "bazės", "ph", "tirpalai", 
                   "dujos", "termochemija", "kvantinė chemija", "elektrochemija"]
    },
    "biologija": {
        "temos": ["biologija", "ląstelių biologija", "molekulinė biologija", "genetika", 
                   "anatomija", "fiziologija", "ekologija", "evoliucija", "botanika", 
                   "zoologija", "mikrobiologija", "dNR", "rNR", "baltymai", "fermentai", 
                   "metabolizmas", "ląstelės", "audiniai", "organai", "kūno sistemos",
                   "neurobiologija", "imunologija", "embriologija"]
    },
    "programavimas": {
        "temos": ["programavimas", "python", "javascript", "java", "c++", "c#", "php", 
                   "ruby", "swift", "kotlin", "go", "rust", "html", "css", "sql", 
                   "mongodb", "git", "react", "angular", "vue", "nodejs", "django",
                   "flask", "spring boot", "laravel", "typescript", "graphql"]
    },
    "dirbtinis_intelektas": {
        "temos_specialios": ["mašinų mokymasis", "gilusis mokymasis", "gpt", "llm"],
        "temos": ["dirbtinis intelektas", "neuroniniai tinklai", "natūralios kalbos apdorojimas", 
                   "kompiuterinis matymas", "chatbotai", "transformatoriai", "automatizacija",
                   "mašinų mokymasis", "gilusis mokymasis", "natūralios kalbos apdorojimas", "kompiuterinis matymas"]
    },
    "kibernetinis_saugumas": {
        "temos": ["kibernetinis saugumas", "etinis hackingas", "ugniasienės", "šifravimas", 
                   "informacijos saugumas", "prasiskverbimo testavimas", "kenksminga programinė įranga", "išpirkos programinė įranga", 
                   "phishingas", "socialinė inžinerija", "kriptografija", "tinklo saugumas",
                   "interneto saugumas", "mobilusis saugumas", "etinis hackingas"]
    },
    "gaminimas": {
        "temos": ["gaminimas", "paprasti receptai", "desertai", "kepimas", "konditerijos gaminiai", 
                   "meksikietiška virtuvė", "itališka virtuvė", "ispaniška virtuvė", "gėrimai", 
                   "kokteiliai", "kokteiliai", "vyno derinimas", "vynas", "amatinis alus",
                   "molekulinė gastronomija", "vegetariškas gaminimas", "vegoniškas gaminimas"]
    },
    "sportas": {
        "temos": ["sportas", "futbolas", "krepšinis", "tenisas", "plaukimas", "bėgimas", 
                   "fitnesas", "sporto salė", "joga", "pilatesas", "crossfit", "sportinė mityba",
                   "funkcinės treniruotės", "kalistenika", "boksas", "kovos menai"]
    },
    "verslas": {
        "temos": ["verslas", "verslumas", "startuoliai", "skaitmeninė rinkodara", "pardavimai", 
                   "asmeniniai finansai", "investicijos", "verslas internete", "elektroninė prekyba", 
                   "logistika", "lyderystė", "verslo valdymas", "žmogiškieji ištekliai",
                   "klientų aptarnavimas", "prekės ženklo kūrimas", "seo", "sem", "el. pašto rinkodara"]
    }
}

# ============================================
# PRIEDĖLIAI
# ============================================
priedėliai = [
    "kaip išmokti", "kaip įvaldyti", "pilnas vadovas", "pamoka", "kursas",
    "įvaldyti", "suprasti", "praktikuoti", "spręsti problemas", "pratimai",
    "įvadas į", "pagrindinės sąvokos", "vadovas", "teorija",
    "pavyzdžiai", "pagrindai", "patarimai mokymuisi", "ištekliai mokymuisi",
    "pamokos", "pamokos", "kaip tobulėti", "kaip naudoti"
]

# ============================================
# PriesAGOS
# ============================================
priesagos = [
    "pradedantysis", "vidutinis", "pažengęs", "profesionalus", "pilnas",
    "lengvas", "greitas", "pradedantiesiems", "nuo nulio", "žingsnis po žingsnio",
    "su pratimais", "internetu", "nemokamas", "sertifikuotas", "universiteto lygis",
    "vaikams", "suaugusiems", "intensyvus", "praktiškas", "teorinis"
]

# ============================================
# KLAUSIMAI
# ============================================
klausimai = [
    "kas tai", "kaip tai veikia", "kam tai skirta", "kur mokytis",
    "kada naudoti", "kodėl tai svarbu", "kokie privalumai",
    "kiek laiko užtrunka išmokti", "ko man reikia mokymuisi"
]

# ============================================
# RAKTINŽODŽIŲ GENERAVIMAS
# ============================================
raktiniai_žodžiai = set()

print("🔄 Generuojami lietuviški raktažodžiai...")

for priedėlis in priedėliai:
    for cat_data in temOS.values():
        for tema in cat_data["temos"]:
            raktiniai_žodžiai.add(f"{priedėlis} {tema}")
        for tema_speciali in cat_data.get("temos_specialios", []):
            raktiniai_žodžiai.add(f"{priedėlis} {tema_speciali}")

for priesaga in priesagos:
    for cat_data in temOS.values():
        for tema in cat_data["temos"][:15]:
            raktiniai_žodžiai.add(f"{tema} {priesaga}")
        for tema_speciali in cat_data.get("temos_specialios", []):
            raktiniai_žodžiai.add(f"{tema_speciali} {priesaga}")

for klausimas in klausimai:
    for cat_data in temOS.values():
        for tema in cat_data["temos"][:15]:
            raktiniai_žodžiai.add(f"{klausimas} {tema}")
        for tema_speciali in cat_data.get("temos_specialios", []):
            raktiniai_žodžiai.add(f"{klausimas} {tema_speciali}")

veiksmažodžiai = ["išmok", "įvaldyk", "praktikuok", "studijuok", "suprask", "taikyk"]
for veiksmažodis in veiksmažodžiai:
    for cat_data in temOS.values():
        for tema in cat_data["temos"][:15]:
            raktiniai_žodžiai.add(f"{veiksmažodis} {tema}")

for cat_data in temOS.values():
    visos_temos = cat_data["temos"] + cat_data.get("temos_specialios", [])
    if len(visos_temos) >= 2:
        for _ in range(min(30, len(visos_temos) * 3)):
            tema1, tema2 = random.sample(visos_temos, 2)
            raktiniai_žodžiai.add(f"skirtumas tarp {tema1} ir {tema2}")
            raktiniai_žodžiai.add(f"{tema1} prieš {tema2}")
            raktiniai_žodžiai.add(f"{tema1} ir {tema2} palyginimas")

for cat_data in temOS.values():
    for tema in cat_data["temos"][:10]:
        raktiniai_žodžiai.add(f"dažnos klaidos {tema}")
        raktiniai_žodžiai.add(f"kaip išvengti klaidų {tema}")
        raktiniai_žodžiai.add(f"{tema} problemų sprendimas")

lygiai = ["pradedantysis", "vidutinis", "pažengęs", "profesionalus", "intensyvus"]
for lygis in lygiai:
    for cat_data in temOS.values():
        for tema in cat_data["temos"][:12]:
            raktiniai_žodžiai.add(f"{lygis} {tema} kursas")
            raktiniai_žodžiai.add(f"{tema} {lygis} lygio pamokos")

for cat_data in temOS.values():
    for tema in cat_data["temos"][:10]:
        raktiniai_žodžiai.add(f"sertifikatas {tema}")
        raktiniai_žodžiai.add(f"egzaminas {tema}")
        raktiniai_žodžiai.add(f"knygos apie {tema}")
        raktiniai_žodžiai.add(f"vaizdo įrašai apie {tema}")

for cat_data in temOS.values():
    for tema in cat_data["temos"][:10]:
        raktiniai_žodžiai.add(f"patarimai {tema}")
        raktiniai_žodžiai.add(f"rekomendacijos tobulėti {tema}")

for i in range(1, 2000):
    cat_name = random.choice(list(temOS.keys()))
    tema = random.choice(temOS[cat_name]["temos"])
    raktiniai_žodžiai.add(f"{tema} pamoka {i}")
    raktiniai_žodžiai.add(f"{tema} skyrius {i}")
    raktiniai_žodžiai.add(f"{tema} vienetas {i}")

# ============================================
# APRIBOJIMAS
# ============================================
raktinių_žodžių_sąrašas = sorted(list(raktiniai_žodžiai))
random.shuffle(raktinių_žodžių_sąrašas)

if len(raktinių_žodžių_sąrašas) < RAKTINŽODŽIŲ_SKAIČIUS:
    print(f"⚠ Buvo sugeneruota tik {len(raktinių_žodžių_sąrašas)} raktažodžių. Kartojame keletą, kad pasiektume {RAKTINŽODŽIŲ_SKAIČIUS}...")
    while len(raktinių_žodžių_sąrašas) < RAKTINŽODŽIŲ_SKAIČIUS:
        raktinių_žodžių_sąrašas.extend(raktinių_žodžių_sąrašas[:min(1000, RAKTINŽODŽIŲ_SKAIČIUS - len(raktinių_žodžių_sąrašas))])

galutiniai_raktiniai_žodžiai = raktinių_žodžių_sąrašas[:RAKTINŽODŽIŲ_SKAIČIUS]
random.shuffle(galutiniai_raktiniai_žodžiai)

# ============================================
# IŠSAUGOJIMAS
# ============================================
with open('keywords/lt.json', 'w', encoding='utf-8') as f:
    json.dump(galutiniai_raktiniai_žodžiai, f, indent=2, ensure_ascii=False)

# ============================================
# ATASKAITA
# ============================================
print(f"\n✅ {len(galutiniai_raktiniai_žodžiai)} lietuviškų raktažodžių buvo sugeneruota")
print(f"📁 Išsaugota: keywords/lt.json")
print(f"\n📊 Peržiūra (pirmieji 30 raktažodžių):")
for i, kw in enumerate(galutiniai_raktiniai_žodžiai[:30]):
    print(f"   {i+1}. {kw}")
