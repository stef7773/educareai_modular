import json
import random

# ============================================
# KONFIGURASI
# ============================================
BILANGAN_KATA_KUNCI = 10000

# ============================================
# TOPIK DALAM BAHASA MELAYU
# ============================================
topik = {
    "matematik": {
        "topik": ["matematik", "kalkulus", "algebra", "geometri", "trigonometri", 
                   "statistik", "kebarangkalian", "terbitan", "kamiran", "had", 
                   "fungsi", "matriks", "vektor", "persamaan", "logaritma", 
                   "pecahan", "peratusan", "punca kuasa", "kuasa", "polinomial", 
                   "nombor kompleks", "persamaan pembezaan", "algebra linear",
                   "trigonometri sfera", "kalkulus vektor", "topologi", "teori nombor"]
    },
    "fizik": {
        "topik": ["fizik", "mekanik", "termodinamik", "elektromagnetisme", "optik", 
                   "akustik", "kinematik", "dinamik", "cecair", "fizik kuantum", 
                   "teori relativiti", "tenaga", "kerja", "kuasa", "gerakan", 
                   "daya", "graviti", "elektrik", "kemagnetan", "gelombang",
                   "astrofizik", "kosmologi", "fizik nuklear", "fizik molekul"]
    },
    "kimia": {
        "topik": ["kimia", "kimia organik", "kimia tak organik", "kimia analitik", 
                   "biokimia", "tindak balas kimia", "penyeimbangan", "stoikiometri", 
                   "jadual berkala", "ikatan kimia", "molekul", "atom", 
                   "sebatian kimia", "asid", "bes", "ph", "larutan", 
                   "gas", "termokimia", "kimia kuantum", "elektrokimia"]
    },
    "biologi": {
        "topik": ["biologi", "biologi sel", "biologi molekul", "genetik", 
                   "anatomi", "fisiologi", "ekologi", "evolusi", "botani", 
                   "zoologi", "mikrobiologi", "dna", "rna", "protein", "enzim", 
                   "metabolisme", "sel", "tisu", "organ", "sistem badan",
                   "sains saraf", "imunologi", "embriologi"]
    },
    "pengaturcaraan": {
        "topik": ["pengaturcaraan", "python", "javascript", "java", "c++", "c#", "php", 
                   "ruby", "swift", "kotlin", "go", "rust", "html", "css", "sql", 
                   "mongodb", "git", "react", "angular", "vue", "nodejs", "django",
                   "flask", "spring boot", "laravel", "typescript", "graphql"]
    },
    "kecerdasan_buatan": {
        "topik_khas": ["pembelajaran mesin", "pembelajaran mendalam", "gpt", "llm"],
        "topik": ["kecerdasan buatan", "rangkaian saraf", "pemprosesan bahasa semula jadi", 
                   "penglihatan komputer", "chatbot", "transformer", "automasi",
                   "pembelajaran mesin", "pembelajaran mendalam", "pemprosesan bahasa semula jadi", "penglihatan komputer"]
    },
    "keselamatan_siber": {
        "topik": ["keselamatan siber", "penggodaman etika", "tembok api", "penyulitan", 
                   "keselamatan maklumat", "ujian penembusan", "perisian hasad", "perisian tebusan", 
                   "phishing", "kejuruteraan sosial", "kriptografi", "keselamatan rangkaian",
                   "keselamatan web", "keselamatan mudah alih", "penggodaman etika"]
    },
    "memasak": {
        "topik": ["memasak", "resipi mudah", "pencuci mulut", "pembakaran", "pastri", 
                   "masakan meksiko", "masakan itali", "masakan sepanyol", "minuman", 
                   "koktel", "koktel", "padanan wain", "wain", "bir kraf",
                   "gastronomi molekul", "masakan vegetarian", "masakan vegan"]
    },
    "sukan": {
        "topik": ["sukan", "bola sepak", "bola keranjang", "tenis", "renang", "larian", 
                   "kecergasan", "gim", "yoga", "pilates", "crossfit", "pemakanan sukan",
                   "latihan fungsi", "kalistenik", "tinju", "seni mempertahankan diri"]
    },
    "perniagaan": {
        "topik": ["perniagaan", "keusahawanan", "startup", "pemasaran digital", "jualan", 
                   "kewangan peribadi", "pelaburan", "perniagaan dalam talian", "e-dagang", 
                   "logistik", "kepimpinan", "pengurusan perniagaan", "sumber manusia",
                   "perkhidmatan pelanggan", "penjenamaan", "seo", "sem", "pemasaran e-mel"]
    }
}

# ============================================
# AWALAN
# ============================================
awalan = [
    "cara belajar", "cara menguasai", "panduan lengkap", "tutorial", "kursus",
    "kuasai", "fahami", "amalkan", "selesaikan masalah", "latihan",
    "pengenalan kepada", "konsep asas", "manual", "teori",
    "contoh", "asas", "tips belajar", "sumber untuk belajar",
    "pelajaran", "pelajaran", "cara menambah baik dalam", "cara menggunakan"
]

# ============================================
# AKHIRAN
# ============================================
akhiran = [
    "pemula", "pertengahan", "lanjutan", "profesional", "lengkap",
    "mudah", "cepat", "untuk pemula", "dari sifar", "langkah demi langkah",
    "dengan latihan", "dalam talian", "percuma", "diperakui", "peringkat universiti",
    "untuk kanak-kanak", "untuk dewasa", "intensif", "praktikal", "teori"
]

# ============================================
# SOALAN
# ============================================
soalan = [
    "apa itu", "bagaimana ia berfungsi", "untuk apa", "di mana belajar",
    "bila menggunakan", "kenapa penting", "apa faedahnya",
    "berapa lama masa untuk belajar", "apa yang saya perlukan untuk belajar"
]

# ============================================
# HASILKAN KATA KUNCI
# ============================================
kata_kunci = set()

print("🔄 Menghasilkan kata kunci bahasa Melayu...")

for awal in awalan:
    for cat_data in topik.values():
        for top in cat_data["topik"]:
            kata_kunci.add(f"{awal} {top}")
        for top_khas in cat_data.get("topik_khas", []):
            kata_kunci.add(f"{awal} {top_khas}")

for akh in akhiran:
    for cat_data in topik.values():
        for top in cat_data["topik"][:15]:
            kata_kunci.add(f"{top} {akh}")
        for top_khas in cat_data.get("topik_khas", []):
            kata_kunci.add(f"{top_khas} {akh}")

for soalan in soalan:
    for cat_data in topik.values():
        for top in cat_data["topik"][:15]:
            kata_kunci.add(f"{soalan} {top}")
        for top_khas in cat_data.get("topik_khas", []):
            kata_kunci.add(f"{soalan} {top_khas}")

kata_kerja = ["belajar", "kuasai", "amalkan", "kaji", "fahami", "guna"]
for kerja in kata_kerja:
    for cat_data in topik.values():
        for top in cat_data["topik"][:15]:
            kata_kunci.add(f"{kerja} {top}")

for cat_data in topik.values():
    semua_topik = cat_data["topik"] + cat_data.get("topik_khas", [])
    if len(semua_topik) >= 2:
        for _ in range(min(30, len(semua_topik) * 3)):
            top1, top2 = random.sample(semua_topik, 2)
            kata_kunci.add(f"perbezaan antara {top1} dan {top2}")
            kata_kunci.add(f"{top1} vs {top2}")
            kata_kunci.add(f"perbandingan {top1} dan {top2}")

for cat_data in topik.values():
    for top in cat_data["topik"][:10]:
        kata_kunci.add(f"kesilapan biasa dalam {top}")
        kata_kunci.add(f"cara mengelakkan kesilapan dalam {top}")
        kata_kunci.add(f"penyelesaian kepada masalah {top}")

peringkat = ["pemula", "pertengahan", "lanjutan", "profesional", "intensif"]
for per in peringkat:
    for cat_data in topik.values():
        for top in cat_data["topik"][:12]:
            kata_kunci.add(f"kursus {per} {top}")
            kata_kunci.add(f"pelajaran {top} peringkat {per}")

for cat_data in topik.values():
    for top in cat_data["topik"][:10]:
        kata_kunci.add(f"pensijilan dalam {top}")
        kata_kunci.add(f"peperiksaan {top}")
        kata_kunci.add(f"buku tentang {top}")
        kata_kunci.add(f"video tentang {top}")

for cat_data in topik.values():
    for top in cat_data["topik"][:10]:
        kata_kunci.add(f"tips untuk {top}")
        kata_kunci.add(f"nasihat untuk meningkatkan dalam {top}")

for i in range(1, 2000):
    cat_name = random.choice(list(topik.keys()))
    top = random.choice(topik[cat_name]["topik"])
    kata_kunci.add(f"{top} pelajaran {i}")
    kata_kunci.add(f"{top} bab {i}")
    kata_kunci.add(f"{top} unit {i}")

# ============================================
# HAD
# ============================================
senarai_kata_kunci = sorted(list(kata_kunci))
random.shuffle(senarai_kata_kunci)

if len(senarai_kata_kunci) < BILANGAN_KATA_KUNCI:
    print(f"⚠ Hanya {len(senarai_kata_kunci)} kata kunci dihasilkan. Mengulang beberapa untuk mencapai {BILANGAN_KATA_KUNCI}...")
    while len(senarai_kata_kunci) < BILANGAN_KATA_KUNCI:
        senarai_kata_kunci.extend(senarai_kata_kunci[:min(1000, BILANGAN_KATA_KUNCI - len(senarai_kata_kunci))])

kata_kunci_akhir = senarai_kata_kunci[:BILANGAN_KATA_KUNCI]
random.shuffle(kata_kunci_akhir)

# ============================================
# SIMPAN
# ============================================
with open('keywords/ms.json', 'w', encoding='utf-8') as f:
    json.dump(kata_kunci_akhir, f, indent=2, ensure_ascii=False)

# ============================================
# LAPORAN
# ============================================
print(f"\n✅ {len(kata_kunci_akhir)} kata kunci bahasa Melayu dihasilkan")
print(f"📁 Disimpan dalam: keywords/ms.json")
print(f"\n📊 Pratonton (30 kata kunci pertama):")
for i, kw in enumerate(kata_kunci_akhir[:30]):
    print(f"   {i+1}. {kw}")
