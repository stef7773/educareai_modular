import json
import random

# ============================================
# KONFIGURATSIOON
# ============================================
MÄRKSÕNADE_ARV = 10000

# ============================================
# TEEMAD EESTI KEELES
# ============================================
teemad = {
    "matemaatika": {
        "teemad": ["matemaatika", "matemaatiline analüüs", "algebra", "geomeetria", "trigonomeetria", 
                   "statistika", "tõenäosus", "tuletised", "integraalid", "piirväärtused", 
                   "funktsioonid", "maatriksid", "vektorid", "võrrandid", "logaritmid", 
                   "murrud", "protsendid", "juured", "astmed", "polünoomid", 
                   "kompleksarvud", "diferentsiaalvõrrandid", "lineaaralgebra",
                   "sfääriline trigonomeetria", "vektoranalüüs", "topoloogia", "arvuteooria"]
    },
    "füüsika": {
        "teemad": ["füüsika", "mehaanika", "termodünaamika", "elektromagnetism", "optika", 
                   "akustika", "kinemaatika", "dünaamika", "vedelikud", "kvantfüüsika", 
                   "relatiivsusteooria", "energia", "töö", "võimsus", "liikumine", 
                   "jõud", "gravitatsioon", "elekter", "magnetism", "lained",
                   "astrofüüsika", "kosmoloogia", "tuumafüüsika", "molekulaarfüüsika"]
    },
    "keemia": {
        "teemad": ["keemia", "orgaaniline keemia", "anorgaaniline keemia", "analüütiline keemia", 
                   "biokeemia", "keemilised reaktsioonid", "tasakaalustamine", "stöhhiomeetria", 
                   "perioodilisustabel", "keemilised sidemed", "molekulid", "aatomid", 
                   "keemilised ühendid", "happed", "alused", "ph", "lahused", 
                   "gaasid", "termokeemia", "kvantkeemia", "elektrokeemia"]
    },
    "bioloogia": {
        "teemad": ["bioloogia", "rakubioloogia", "molekulaarbioloogia", "geneetika", 
                   "anatoomia", "füsioloogia", "ökoloogia", "evolutsioon", "botaanika", 
                   "zooloogia", "mikrobioloogia", "dna", "rna", "valgud", "ensüümid", 
                   "ainevahetus", "rakud", "koed", "elundid", "kehasüsteemid",
                   "neuroteadus", "immunoloogia", "embrüoloogia"]
    },
    "programmeerimine": {
        "teemad": ["programmeerimine", "python", "javascript", "java", "c++", "c#", "php", 
                   "ruby", "swift", "kotlin", "go", "rust", "html", "css", "sql", 
                   "mongodb", "git", "react", "angular", "vue", "nodejs", "django",
                   "flask", "spring boot", "laravel", "typescript", "graphql"]
    },
    "tehisintellekt": {
        "teemad_erilised": ["masinõpe", "süvaõpe", "gpt", "llm"],
        "teemad": ["tehisintellekt", "närvivõrgud", "loomuliku keele töötlus", 
                   "arvutinägemine", "vestlusrobotid", "transformaatorid", "automatiseerimine",
                   "masinõpe", "süvaõpe", "loomuliku keele töötlus", "arvutinägemine"]
    },
    "küberjulgeolek": {
        "teemad": ["küberjulgeolek", "eetiline häkkimine", "tulemüürid", "krüpteerimine", 
                   "infoturve", "sissetungitestimine", "pahavara", "lunavaraprogramm", 
                   "andmepüük", "sotsiaalne inseneriteadus", "krüptograafia", "võrguturve",
                   "veebiturve", "mobiiliturve", "eetiline häkkimine"]
    },
    "toiduvalmistamine": {
        "teemad": ["toiduvalmistamine", "lihtsad retseptid", "magustoidud", "küpsetamine", "pagaritooted", 
                   "mehhiko köök", "itaalia köök", "hispaania köök", "joogid", 
                   "kokteilid", "kokteilid", "veini sobitamine", "vein", "käsitööõlu",
                   "molekulaargastronoomia", "taimetoit", "vegantoit"]
    },
    "sport": {
        "teemad": ["sport", "jalgpall", "korvpall", "tennis", "ujumine", "jooksmine", 
                   "fitness", "jõusaal", "jooga", "pilates", "crossfit", "sporditoitumine",
                   "funktsionaalne treening", "kalisteenika", "poks", "võitluskunstid"]
    },
    "äri": {
        "teemad": ["äri", "ettevõtlus", "startupid", "digitaalne turundus", "müük", 
                   "isiklikud rahandus", "investeeringud", "veebiäri", "e-kaubandus", 
                   "logistika", "juhtimine", "ärijuhtimine", "inimressursid",
                   "klienditeenindus", "bränding", "seo", "sem", "e-posti turundus"]
    }
}

# ============================================
# EESLIITED
# ============================================
eesliited = [
    "kuidas õppida", "kuidas omandada", "täielik juhend", "õpetus", "kursus",
    "omandada", "mõista", "harjutada", "lahendada probleeme", "harjutused",
    "sissejuhatus", "põhimõisted", "käsiraamat", "teooria",
    "näited", "põhialused", "nõuanded õppimiseks", "ressursid õppimiseks",
    "tunnid", "tunnid", "kuidas paraneda", "kuidas kasutada"
]

# ============================================
# JÄRELIITED
# ============================================
järelliited = [
    "algaja", "kesktase", "edasijõudnud", "professionaalne", "täielik",
    "lihtne", "kiire", "algajatele", "nullist", "samm-sammult",
    "harjutustega", "veebis", "tasuta", "sertifitseeritud", "ülikooli tase",
    "lastele", "täiskasvanutele", "intensiivne", "praktiline", "teoreetiline"
]

# ============================================
# KÜSIMUSED
# ============================================
küsimused = [
    "mis on", "kuidas see töötab", "milleks see on", "kus õppida",
    "millal kasutada", "miks see on oluline", "millised on eelised",
    "kui kaua aega kulub õppimiseks", "mida ma vajan õppimiseks"
]

# ============================================
# MÄRKSÕNADE LOOMINE
# ============================================
märksõnad = set()

print("🔄 Eesti märksõnade loomine...")

for eesliide in eesliited:
    for cat_data in teemad.values():
        for teema in cat_data["teemad"]:
            märksõnad.add(f"{eesliide} {teema}")
        for teema_eriline in cat_data.get("teemad_erilised", []):
            märksõnad.add(f"{eesliide} {teema_eriline}")

for järelliide in järelliited:
    for cat_data in teemad.values():
        for teema in cat_data["teemad"][:15]:
            märksõnad.add(f"{teema} {järelliide}")
        for teema_eriline in cat_data.get("teemad_erilised", []):
            märksõnad.add(f"{teema_eriline} {järelliide}")

for küsimus in küsimused:
    for cat_data in teemad.values():
        for teema in cat_data["teemad"][:15]:
            märksõnad.add(f"{küsimus} {teema}")
        for teema_eriline in cat_data.get("teemad_erilised", []):
            märksõnad.add(f"{küsimus} {teema_eriline}")

tegusõnad = ["õpi", "omanda", "harjuta", "õpeta", "mõista", "rakenda"]
for tegusõna in tegusõnad:
    for cat_data in teemad.values():
        for teema in cat_data["teemad"][:15]:
            märksõnad.add(f"{tegusõna} {teema}")

for cat_data in teemad.values():
    kõik_teemad = cat_data["teemad"] + cat_data.get("teemad_erilised", [])
    if len(kõik_teemad) >= 2:
        for _ in range(min(30, len(kõik_teemad) * 3)):
            teema1, teema2 = random.sample(kõik_teemad, 2)
            märksõnad.add(f"erinevus {teema1} ja {teema2} vahel")
            märksõnad.add(f"{teema1} vs {teema2}")
            märksõnad.add(f"{teema1} ja {teema2} võrdlus")

for cat_data in teemad.values():
    for teema in cat_data["teemad"][:10]:
        märksõnad.add(f"sagedased vead {teema}")
        märksõnad.add(f"kuidas vältida vigu {teema}")
        märksõnad.add(f"{teema} probleemide lahendused")

tasemed = ["algaja", "kesktase", "edasijõudnud", "professionaalne", "intensiivne"]
for tase in tasemed:
    for cat_data in teemad.values():
        for teema in cat_data["teemad"][:12]:
            märksõnad.add(f"{tase} {teema} kursus")
            märksõnad.add(f"{teema} {tase} taseme tunnid")

for cat_data in teemad.values():
    for teema in cat_data["teemad"][:10]:
        märksõnad.add(f"sertifikaat {teema}")
        märksõnad.add(f"eksam {teema}")
        märksõnad.add(f"raamatud {teema} kohta")
        märksõnad.add(f"videod {teema} kohta")

for cat_data in teemad.values():
    for teema in cat_data["teemad"][:10]:
        märksõnad.add(f"nõuanded {teema} jaoks")
        märksõnad.add(f"soovitused {teema} parandamiseks")

for i in range(1, 2000):
    cat_name = random.choice(list(teemad.keys()))
    teema = random.choice(teemad[cat_name]["teemad"])
    märksõnad.add(f"{teema} tund {i}")
    märksõnad.add(f"{teema} peatükk {i}")
    märksõnad.add(f"{teema} üksus {i}")

# ============================================
# PIIRAMINE
# ============================================
märksõnade_nimekiri = sorted(list(märksõnad))
random.shuffle(märksõnade_nimekiri)

if len(märksõnade_nimekiri) < MÄRKSÕNADE_ARV:
    print(f"⚠ Loodi ainult {len(märksõnade_nimekiri)} märksõna. Korratakse mõnda, et jõuda {MÄRKSÕNADE_ARV}...")
    while len(märksõnade_nimekiri) < MÄRKSÕNADE_ARV:
        märksõnade_nimekiri.extend(märksõnade_nimekiri[:min(1000, MÄRKSÕNADE_ARV - len(märksõnade_nimekiri))])

lõplikud_märksõnad = märksõnade_nimekiri[:MÄRKSÕNADE_ARV]
random.shuffle(lõplikud_märksõnad)

# ============================================
# SALVESTAMINE
# ============================================
with open('keywords/et.json', 'w', encoding='utf-8') as f:
    json.dump(lõplikud_märksõnad, f, indent=2, ensure_ascii=False)

# ============================================
# ARUANNE
# ============================================
print(f"\n✅ Loodi {len(lõplikud_märksõnad)} eesti märksõna")
print(f"📁 Salvestatud: keywords/et.json")
print(f"\n📊 Eelvaade (esimesed 30 märksõna):")
for i, kw in enumerate(lõplikud_märksõnad[:30]):
    print(f"   {i+1}. {kw}")
