import json
import random

# ============================================
# KONFİQURASİYA
# ============================================
AÇAR_SÖZLƏRİN_SAYI = 10000

# ============================================
# AZƏRBAYCAN DİLİNDƏ MÖVZULAR
# ============================================
mövzular = {
    "riyaziyyat": {
        "mövzular": ["riyaziyyat", "kalkulus", "cebr", "həndəsə", "triqonometriya", 
                   "statistika", "ehtimal", "törəmələr", "inteqrallar", "limitlər", 
                   "funksiyalar", "matrislər", "vektorlar", "tənliklər", "loqarifmlər", 
                   "kəsrlər", "faizlər", "köklər", "qüvvətlər", "polinomlar", 
                   "kompleks ədədlər", "diferensial tənliklər", "xətti cəbr",
                   "sferik triqonometriya", "vektor hesabı", "topologiya", "ədəd nəzəriyyəsi"]
    },
    "fizika": {
        "mövzular": ["fizika", "mexanika", "termodinamika", "elektromaqnetizm", "optika", 
                   "akustika", "kinematika", "dinamika", "mayelər", "kvant fizikası", 
                   "nisbilik nəzəriyyəsi", "enerji", "iş", "güc", "hərəkət", 
                   "qüvvələr", "cazibə qüvvəsi", "elektrik", "maqnetizm", "dalğalar",
                   "astrofizika", "kosmologiya", "nüvə fizikası", "molekulyar fizika"]
    },
    "kimya": {
        "mövzular": ["kimya", "üzvi kimya", "qeyri-üzvi kimya", "analitik kimya", 
                   "biokimya", "kimyəvi reaksiyalar", "balanslaşdırma", "stexiometriya", 
                   "dövri cədvəl", "kimyəvi bağlar", "molekullar", "atomlar", 
                   "kimyəvi birləşmələr", "turşular", "əsaslar", "ph", "məhlullar", 
                   "qazlar", "termokimya", "kvant kimyası", "elektrokimya"]
    },
    "biologiya": {
        "mövzular": ["biologiya", "hüceyrə biologiyası", "molekulyar biologiya", "genetika", 
                   "anatomiya", "fiziologiya", "ekologiya", "təkamül", "botanika", 
                   "zoologiya", "mikrobiologiya", "dna", "rna", "zülallar", "fermentlər", 
                   "maddələr mübadiləsi", "hüceyrələr", "toxumalar", "orqanlar", "bədən sistemləri",
                   "neyroelm", "immunologiya", "embriologiya"]
    },
    "proqramlaşdırma": {
        "mövzular": ["proqramlaşdırma", "python", "javascript", "java", "c++", "c#", "php", 
                   "ruby", "swift", "kotlin", "go", "rust", "html", "css", "sql", 
                   "mongodb", "git", "react", "angular", "vue", "nodejs", "django",
                   "flask", "spring boot", "laravel", "typescript", "graphql"]
    },
    "süni_intellekt": {
        "mövzular_xüsusi": ["maşın öyrənməsi", "dərin öyrənmə", "gpt", "llm"],
        "mövzular": ["süni intellekt", "neyron şəbəkələri", "təbii dilin işlənməsi", 
                   "kompüter görməsi", "çatbotlar", "transformatorlar", "avtomatlaşdırma",
                   "maşın öyrənməsi", "dərin öyrənmə", "təbii dilin işlənməsi", "kompüter görməsi"]
    },
    "kibertəhlükəsizlik": {
        "mövzular": ["kibertəhlükəsizlik", "etik hakerlik", "yanğın divarları", "şifrələmə", 
                   "informasiya təhlükəsizliyi", "nüfuz testi", "zərərli proqram", "fidyə proqramı", 
                   "fişinq", "sosial mühəndislik", "kriptoqrafiya", "şəbəkə təhlükəsizliyi",
                   "veb təhlükəsizliyi", "mobil təhlükəsizlik", "etik hakerlik"]
    },
    "yemək_bişirmə": {
        "mövzular": ["yemək bişirmə", "sadə reseptlər", "desertlər", "bişirmə", "xəmir məmulatları", 
                   "meksika mətbəxi", "italiya mətbəxi", "ispaniya mətbəxi", "içkilər", 
                   "kokteyllər", "kokteyllər", "şərab uyğunlaşdırılması", "şərab", "sənət pivəsi",
                   "molekulyar qastronomiya", "vegetarian yemək", "vegan yemək"]
    },
    "idman": {
        "mövzular": ["idman", "futbol", "basketbol", "tenis", "üzmə", "qaçış", 
                   "fitnes", "idman zalı", "yoqa", "pilates", "krossfit", "idman qidalanması",
                   "funksional məşq", "kalistenika", "boks", "döyüş sənətləri"]
    },
    "biznes": {
        "mövzular": ["biznes", "sahibkarlıq", "startaplar", "rəqəmsal marketinq", "satış", 
                   "şəxsi maliyyə", "investisiyalar", "onlayn biznes", "elektron ticarət", 
                   "logistika", "liderlik", "biznesin idarə edilməsi", "insan resursları",
                   "müştəri xidməti", "brendinq", "seo", "sem", "e-poçt marketinqi"]
    }
}

# ============================================
# PREFİKSLƏR
# ============================================
prefikslər = [
    "necə öyrənmək", "necə mənimsəmək", "tam bələdçi", "dərs", "kurs",
    "mənimsəmək", "anlamaq", "təcrübə etmək", "problemləri həll etmək", "tapşırıqlar",
    "giriş", "əsas anlayışlar", "təlimat", "nəzəriyyə",
    "nümunələr", "əsaslar", "öyrənmək üçün məsləhətlər", "təhsil üçün resurslar",
    "dərslər", "dərslər", "necə təkmilləşdirmək", "necə istifadə etmək"
]

# ============================================
# SUFİKSLƏR
# ============================================
sufikslər = [
    "başlanğıc", "orta", "qabaqcıl", "peşəkar", "tam",
    "asan", "sürətli", "yeni başlayanlar üçün", "sıfırdan", "addım-addım",
    "tapşırıqlarla", "onlayn", "pulsuz", "sertifikatlı", "universitet səviyyəsi",
    "uşaqlar üçün", "böyüklər üçün", "intensiv", "praktik", "nəzəri"
]

# ============================================
# SUALLAR
# ============================================
suallar = [
    "nədir", "necə işləyir", "nə üçündür", "harada öyrənmək",
    "nə vaxt istifadə etmək", "niyə vacibdir", "faydaları nələrdir",
    "öyrənmək nə qədər vaxt aparır", "təhsil üçün nə lazımdır"
]

# ============================================
# AÇAR SÖZLƏRİN YARADILMASI
# ============================================
açar_sözlər = set()

print("🔄 Azərbaycan dilində açar sözlər yaradılır...")

for prefiks in prefikslər:
    for cat_data in mövzular.values():
        for mövzu in cat_data["mövzular"]:
            açar_sözlər.add(f"{prefiks} {mövzu}")
        for mövzu_xüsusi in cat_data.get("mövzular_xüsusi", []):
            açar_sözlər.add(f"{prefiks} {mövzu_xüsusi}")

for sufiks in sufikslər:
    for cat_data in mövzular.values():
        for mövzu in cat_data["mövzular"][:15]:
            açar_sözlər.add(f"{mövzu} {sufiks}")
        for mövzu_xüsusi in cat_data.get("mövzular_xüsusi", []):
            açar_sözlər.add(f"{mövzu_xüsusi} {sufiks}")

for sual in suallar:
    for cat_data in mövzular.values():
        for mövzu in cat_data["mövzular"][:15]:
            açar_sözlər.add(f"{sual} {mövzu}")
        for mövzu_xüsusi in cat_data.get("mövzular_xüsusi", []):
            açar_sözlər.add(f"{sual} {mövzu_xüsusi}")

fellər = ["öyrən", "mənimsə", "təcrübə et", "oxu", "anla", "tətbiq et"]
for fel in fellər:
    for cat_data in mövzular.values():
        for mövzu in cat_data["mövzular"][:15]:
            açar_sözlər.add(f"{fel} {mövzu}")

for cat_data in mövzular.values():
    bütün_mövzular = cat_data["mövzular"] + cat_data.get("mövzular_xüsusi", [])
    if len(bütün_mövzular) >= 2:
        for _ in range(min(30, len(bütün_mövzular) * 3)):
            mövzu1, mövzu2 = random.sample(bütün_mövzular, 2)
            açar_sözlər.add(f"{mövzu1} və {mövzu2} arasındakı fərq")
            açar_sözlər.add(f"{mövzu1} vs {mövzu2}")
            açar_sözlər.add(f"{mövzu1} və {mövzu2} müqayisəsi")

for cat_data in mövzular.values():
    for mövzu in cat_data["mövzular"][:10]:
        açar_sözlər.add(f"{mövzu} -da ümumi səhvlər")
        açar_sözlər.add(f"{mövzu} -da səhvlərdən necə qaçınmaq")
        açar_sözlər.add(f"{mövzu} problemlərinin həlli")

səviyyələr = ["başlanğıc", "orta", "qabaqcıl", "peşəkar", "intensiv"]
for səviyyə in səviyyələr:
    for cat_data in mövzular.values():
        for mövzu in cat_data["mövzular"][:12]:
            açar_sözlər.add(f"{səviyyə} {mövzu} kursu")
            açar_sözlər.add(f"{mövzu} {səviyyə} səviyyə dərsləri")

for cat_data in mövzular.values():
    for mövzu in cat_data["mövzular"][:10]:
        açar_sözlər.add(f"{mövzu} sertifikatı")
        açar_sözlər.add(f"{mövzu} imtahanı")
        açar_sözlər.add(f"{mövzu} kitabları")
        açar_sözlər.add(f"{mövzu} videoları")

for cat_data in mövzular.values():
    for mövzu in cat_data["mövzular"][:10]:
        açar_sözlər.add(f"{mövzu} üçün məsləhətlər")
        açar_sözlər.add(f"{mövzu} -da təkmilləşmək üçün tövsiyələr")

for i in range(1, 2000):
    cat_name = random.choice(list(mövzular.keys()))
    mövzu = random.choice(mövzular[cat_name]["mövzular"])
    açar_sözlər.add(f"{mövzu} dərs {i}")
    açar_sözlər.add(f"{mövzu} fəsil {i}")
    açar_sözlər.add(f"{mövzu} vahid {i}")

# ============================================
# MƏHDUDİYYƏT
# ============================================
açar_sözlərin_siyahısı = sorted(list(açar_sözlər))
random.shuffle(açar_sözlərin_siyahısı)

if len(açar_sözlərin_siyahısı) < AÇAR_SÖZLƏRİN_SAYI:
    print(f"⚠ Yalnız {len(açar_sözlərin_siyahısı)} açar söz yaradıldı. {AÇAR_SÖZLƏRİN_SAYI} -ə çatmaq üçün bəzilərini təkrarlayırıq...")
    while len(açar_sözlərin_siyahısı) < AÇAR_SÖZLƏRİN_SAYI:
        açar_sözlərin_siyahısı.extend(açar_sözlərin_siyahısı[:min(1000, AÇAR_SÖZLƏRİN_SAYI - len(açar_sözlərin_siyahısı))])

son_açar_sözlər = açar_sözlərin_siyahısı[:AÇAR_SÖZLƏRİN_SAYI]
random.shuffle(son_açar_sözlər)

# ============================================
# YADDA SAXLAMA
# ============================================
with open('keywords/az.json', 'w', encoding='utf-8') as f:
    json.dump(son_açar_sözlər, f, indent=2, ensure_ascii=False)

# ============================================
# HESABAT
# ============================================
print(f"\n✅ {len(son_açar_sözlər)} azərbaycan dilində açar söz yaradıldı")
print(f"📁 Yadda saxlanıldı: keywords/az.json")
print(f"\n📊 Önizləmə (ilk 30 açar söz):")
for i, kw in enumerate(son_açar_sözlər[:30]):
    print(f"   {i+1}. {kw}")
