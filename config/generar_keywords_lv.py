import json
import random

# ============================================
# KONFIGURĀCIJA
# ============================================
ATSLĒGVĀRDU_SKAITS = 10000

# ============================================
# TĒMAS LATVIEŠU VALODĀ
# ============================================
tēmas = {
    "matemātika": {
        "tēmas": ["matemātika", "kalkulus", "algebra", "ģeometrija", "trigonometrija", 
                   "statistika", "varbūtība", "atvasinājumi", "integrāļi", "robežas", 
                   "funkcijas", "matricas", "vektori", "vienādojumi", "logaritmi", 
                   "daļskaitļi", "procenti", "saknes", "pakāpes", "polinomi", 
                   "kompleksie skaitļi", "diferenciālvienādojumi", "lineārā algebra",
                   "sfēriskā trigonometrija", "vektoru analīze", "topoloģija", "skaitļu teorija"]
    },
    "fizika": {
        "tēmas": ["fizika", "mehānika", "termodinamika", "elektromagnētisms", "optika", 
                   "akustika", "kinemātika", "dinamika", "šķidrumi", "kvantu fizika", 
                   "relativitātes teorija", "enerģija", "darbs", "jauda", "kustība", 
                   "spēki", "gravitācija", "elektrība", "magnetisms", "viļņi",
                   "astrofizika", "kosmoloģija", "kodolfizika", "molekulārā fizika"]
    },
    "ķīmija": {
        "tēmas": ["ķīmija", "organiskā ķīmija", "neorganiskā ķīmija", "analītiskā ķīmija", 
                   "bioķīmija", "ķīmiskās reakcijas", "līdzsvarošana", "stehiometrija", 
                   "periodiskā tabula", "ķīmiskās saites", "molekulas", "atomi", 
                   "ķīmiskie savienojumi", "skābes", "bāzes", "ph", "šķīdumi", 
                   "gāzes", "termoķīmija", "kvantu ķīmija", "elektroķīmija"]
    },
    "bioloģija": {
        "tēmas": ["bioloģija", "šūnu bioloģija", "molekulārā bioloģija", "ģenētika", 
                   "anatōmija", "fizioloģija", "ekoloģija", "evolūcija", "botānika", 
                   "zooloģija", "mikrobioloģija", "dns", "rns", "proteīni", "enzīmi", 
                   "metabolisms", "šūnas", "audi", "orgāni", "ķermeņa sistēmas",
                   "neirozinātne", "imunoloģija", "embrioloģija"]
    },
    "programmēšana": {
        "tēmas": ["programmēšana", "python", "javascript", "java", "c++", "c#", "php", 
                   "ruby", "swift", "kotlin", "go", "rust", "html", "css", "sql", 
                   "mongodb", "git", "react", "angular", "vue", "nodejs", "django",
                   "flask", "spring boot", "laravel", "typescript", "graphql"]
    },
    "mākslīgais_intelekts": {
        "tēmas_īpašās": ["mašīnmācīšanās", "dziļā mācīšanās", "gpt", "llm"],
        "tēmas": ["mākslīgais intelekts", "neironu tīkli", "dabiskās valodas apstrāde", 
                   "datorredze", "čatboti", "transformatori", "automatizācija",
                   "mašīnmācīšanās", "dziļā mācīšanās", "dabiskās valodas apstrāde", "datorredze"]
    },
    "kiberdrošība": {
        "tēmas": ["kiberdrošība", "ētiska hakerēšana", "ugunsmūri", "šifrēšana", 
                   "informācijas drošība", "iespiešanās testēšana", "ļaunprogrammatūra", "izspiedējprogrammatūra", 
                   "pikšķerēšana", "sociālā inženierija", "kriptogrāfija", "tīkla drošība",
                   "tīmekļa drošība", "mobilā drošība", "ētiska hakerēšana"]
    },
    "gatavošana": {
        "tēmas": ["gatavošana", "vienkāršas receptes", "deserti", "cepšana", "mīklas izstrādājumi", 
                   "meksikāņu virtuve", "itāļu virtuve", "spāņu virtuve", "dzērieni", 
                   "kokteiļi", "kokteiļi", "vīna saderēšana", "vīns", "amatniecības alus",
                   "molekulārā gastronomija", "veģetāriešu gatavošana", "vegānu gatavošana"]
    },
    "sports": {
        "tēmas": ["sports", "futbols", "basketbols", "teniss", "peldēšana", "skriešana", 
                   "fitness", "sporta zāle", "joga", "pilates", "crossfit", "sporta uzturs",
                   "funkcionālie treniņi", "kalisstēnija", "bokss", "cīņas mākslas"]
    },
    "bizness": {
        "tēmas": ["bizness", "uzņēmējdarbība", "jaunuzņēmumi", "digitālais mārketings", "pārdošana", 
                   "personīgās finanses", "ieguldījumi", "tiešsaistes bizness", "e-komercija", 
                   "loģistika", "līderība", "biznesa vadība", "cilvēkresursi",
                   "klientu apkalpošana", "zīmola veidošana", "seo", "sem", "epasta mārketings"]
    }
}

# ============================================
# PRIEDĒKĻI
# ============================================
priedēkļi = [
    "kā iemācīties", "kā apgūt", "pilnīgs ceļvedis", "apmācība", "kurss",
    "apgūt", "saprast", "praktizēt", "atrisināt problēmas", "vingrinājumi",
    "ievads", "pamatjēdzieni", "rokasgrāmata", "teorija",
    "piemēri", "pamati", "padomi mācīšanai", "resursi mācībām",
    "nodarbības", "nodarbības", "kā uzlabot", "kā lietot"
]

# ============================================
# GALOTNES
# ============================================
galotnes = [
    "iesācējs", "vidējs", "padziļināts", "profesionāls", "pilnīgs",
    "viegli", "ātri", "iesācējiem", "no nulles", "soli pa solim",
    "ar vingrinājumiem", "tiešsaistē", "bezmaksas", "sertificēts", "universitātes līmenis",
    "bērniem", "pieaugušajiem", "intensīvs", "praktisks", "teorētisks"
]

# ============================================
# JAUTĀJUMI
# ============================================
jautājumi = [
    "kas ir", "kā tas darbojas", "kam tas paredzēts", "kur mācīties",
    "kad lietot", "kāpēc tas ir svarīgi", "kādas ir priekšrocības",
    "cik ilgi prasa mācīties", "kas man vajadzīgs mācībām"
]

# ============================================
# ATSLĒGVĀRDU ĢENERĒŠANA
# ============================================
atslēgvārdi = set()

print("🔄 Ģenerē latviešu atslēgvārdus...")

for priedēklis in priedēkļi:
    for cat_data in tēmas.values():
        for tēma in cat_data["tēmas"]:
            atslēgvārdi.add(f"{priedēklis} {tēma}")
        for tēma_īpašā in cat_data.get("tēmas_īpašās", []):
            atslēgvārdi.add(f"{priedēklis} {tēma_īpašā}")

for galotne in galotnes:
    for cat_data in tēmas.values():
        for tēma in cat_data["tēmas"][:15]:
            atslēgvārdi.add(f"{tēma} {galotne}")
        for tēma_īpašā in cat_data.get("tēmas_īpašās", []):
            atslēgvārdi.add(f"{tēma_īpašā} {galotne}")

for jautājums in jautājumi:
    for cat_data in tēmas.values():
        for tēma in cat_data["tēmas"][:15]:
            atslēgvārdi.add(f"{jautājums} {tēma}")
        for tēma_īpašā in cat_data.get("tēmas_īpašās", []):
            atslēgvārdi.add(f"{jautājums} {tēma_īpašā}")

darbības_vārdi = ["mācies", "apgūsti", "praktizē", "studē", "saproti", "pielieto"]
for darbības_vārds in darbības_vārdi:
    for cat_data in tēmas.values():
        for tēma in cat_data["tēmas"][:15]:
            atslēgvārdi.add(f"{darbības_vārds} {tēma}")

for cat_data in tēmas.values():
    visas_tēmas = cat_data["tēmas"] + cat_data.get("tēmas_īpašās", [])
    if len(visas_tēmas) >= 2:
        for _ in range(min(30, len(visas_tēmas) * 3)):
            tēma1, tēma2 = random.sample(visas_tēmas, 2)
            atslēgvārdi.add(f"atšķirība starp {tēma1} un {tēma2}")
            atslēgvārdi.add(f"{tēma1} pret {tēma2}")
            atslēgvārdi.add(f"{tēma1} un {tēma2} salīdzinājums")

for cat_data in tēmas.values():
    for tēma in cat_data["tēmas"][:10]:
        atslēgvārdi.add(f"biežākās kļūdas {tēma}")
        atslēgvārdi.add(f"kā izvairīties no kļūdām {tēma}")
        atslēgvārdi.add(f"{tēma} problēmu risinājumi")

līmeņi = ["iesācējs", "vidējs", "padziļināts", "profesionāls", "intensīvs"]
for līmenis in līmeņi:
    for cat_data in tēmas.values():
        for tēma in cat_data["tēmas"][:12]:
            atslēgvārdi.add(f"{līmenis} {tēma} kurss")
            atslēgvārdi.add(f"{tēma} {līmenis} līmeņa nodarbības")

for cat_data in tēmas.values():
    for tēma in cat_data["tēmas"][:10]:
        atslēgvārdi.add(f"sertifikāts {tēma}")
        atslēgvārdi.add(f"eksāmens {tēma}")
        atslēgvārdi.add(f"grāmatas par {tēma}")
        atslēgvārdi.add(f"video par {tēma}")

for cat_data in tēmas.values():
    for tēma in cat_data["tēmas"][:10]:
        atslēgvārdi.add(f"padomi {tēma}")
        atslēgvārdi.add(f"ieteikumi uzlabošanai {tēma}")

for i in range(1, 2000):
    cat_name = random.choice(list(tēmas.keys()))
    tēma = random.choice(tēmas[cat_name]["tēmas"])
    atslēgvārdi.add(f"{tēma} nodarbība {i}")
    atslēgvārdi.add(f"{tēma} nodaļa {i}")
    atslēgvārdi.add(f"{tēma} vienība {i}")

# ============================================
# IEROBEŽOŠANA
# ============================================
atslēgvārdu_saraksts = sorted(list(atslēgvārdi))
random.shuffle(atslēgvārdu_saraksts)

if len(atslēgvārdu_saraksts) < ATSLĒGVĀRDU_SKAITS:
    print(f"⚠ Tika ģenerēti tikai {len(atslēgvārdu_saraksts)} atslēgvārdi. Atkārtojam dažus, lai sasniegtu {ATSLĒGVĀRDU_SKAITS}...")
    while len(atslēgvārdu_saraksts) < ATSLĒGVĀRDU_SKAITS:
        atslēgvārdu_saraksts.extend(atslēgvārdu_saraksts[:min(1000, ATSLĒGVĀRDU_SKAITS - len(atslēgvārdu_saraksts))])

galīgie_atslēgvārdi = atslēgvārdu_saraksts[:ATSLĒGVĀRDU_SKAITS]
random.shuffle(galīgie_atslēgvārdi)

# ============================================
# SAGLABĀŠANA
# ============================================
with open('keywords/lv.json', 'w', encoding='utf-8') as f:
    json.dump(galīgie_atslēgvārdi, f, indent=2, ensure_ascii=False)

# ============================================
# ZIŅOJUMS
# ============================================
print(f"\n✅ {len(galīgie_atslēgvārdi)} latviešu atslēgvārdu tika ģenerēti")
print(f"📁 Saglabāts: keywords/lv.json")
print(f"\n📊 Priekšskatījums (pirmie 30 atslēgvārdi):")
for i, kw in enumerate(galīgie_atslēgvārdi[:30]):
    print(f"   {i+1}. {kw}")
