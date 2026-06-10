import json
import random

# ============================================
# KONFIGURASI
# ============================================
JUMLAH_KATA_KUNCI = 10000

# ============================================
# TOPIK DALAM BAHASA INDONESIA
# ============================================
topik = {
    "matematika": {
        "topik": ["matematika", "kalkulus", "aljabar", "geometri", "trigonometri", 
                   "statistika", "probabilitas", "turunan", "integral", "limit", 
                   "fungsi", "matriks", "vektor", "persamaan", "logaritma", 
                   "pecahan", "persentase", "akar", "pangkat", "polinomial", 
                   "bilangan kompleks", "persamaan diferensial", "aljabar linear",
                   "trigonometri bola", "kalkulus vektor", "topologi", "teori bilangan"]
    },
    "fisika": {
        "topik": ["fisika", "mekanika", "termodinamika", "elektromagnetisme", "optika", 
                   "akustik", "kinematika", "dinamika", "fluida", "fisika kuantum", 
                   "relativitas", "energi", "usaha", "daya", "gerak", 
                   "gaya", "gravitasi", "listrik", "magnetisme", "gelombang",
                   "astrofisika", "kosmologi", "fisika nuklir", "fisika molekuler"]
    },
    "kimia": {
        "topik": ["kimia", "kimia organik", "kimia anorganik", "kimia analitik", 
                   "biokimia", "reaksi kimia", "penyetaraan", "stoikiometri", 
                   "tabel periodik", "ikatan kimia", "molekul", "atom", 
                   "senyawa kimia", "asam", "basa", "ph", "larutan", 
                   "gas", "termokimia", "kimia kuantum", "elektrokimia"]
    },
    "biologi": {
        "topik": ["biologi", "biologi sel", "biologi molekuler", "genetika", 
                   "anatomi", "fisiologi", "ekologi", "evolusi", "botani", 
                   "zoologi", "mikrobiologi", "dna", "rna", "protein", "enzim", 
                   "metabolisme", "sel", "jaringan", "organ", "sistem tubuh",
                   "neurobiologi", "imunologi", "embriologi"]
    },
    "pemrograman": {
        "topik": ["pemrograman", "python", "javascript", "java", "c++", "c#", "php", 
                   "ruby", "swift", "kotlin", "go", "rust", "html", "css", "sql", 
                   "mongodb", "git", "react", "angular", "vue", "nodejs", "django",
                   "flask", "spring boot", "laravel", "typescript", "graphql"]
    },
    "kecerdasan_buatan": {
        "topik_khusus": ["pembelajaran mesin", "pembelajaran mendalam", "gpt", "llm"],
        "topik": ["kecerdasan buatan", "jaringan saraf", "pemrosesan bahasa alami", 
                   "penglihatan komputer", "chatbot", "transformator", "otomatisasi",
                   "pembelajaran mesin", "pembelajaran mendalam", "pemrosesan bahasa alami", "penglihatan komputer"]
    },
    "keamanan_siber": {
        "topik": ["keamanan siber", "peretasan etis", "firewall", "enkripsi", 
                   "keamanan informasi", "pengujian penetrasi", "perangkat lunak berbahaya", "perangkat lunak tebusan", 
                   "phishing", "rekayasa sosial", "kriptografi", "keamanan jaringan",
                   "keamanan web", "keamanan seluler", "peretasan etis"]
    },
    "memasak": {
        "topik": ["memasak", "resep mudah", "makanan penutup", "memanggang", "kue kering", 
                   "masakan meksiko", "masakan italia", "masakan spanyol", "minuman", 
                   "koktail", "koktail", "pemasangan anggur", "anggur", "bir kerajinan",
                   "gastronomi molekuler", "masakan vegetarian", "masakan vegan"]
    },
    "olahraga": {
        "topik": ["olahraga", "sepak bola", "basket", "tenis", "renang", "lari", 
                   "kebugaran", "gym", "yoga", "pilates", "crossfit", "nutrisi olahraga",
                   "latihan fungsional", "kalistenik", "tinju", "seni bela diri"]
    },
    "bisnis": {
        "topik": ["bisnis", "kewirausahaan", "startup", "pemasaran digital", "penjualan", 
                   "keuangan pribadi", "investasi", "bisnis online", "e-commerce", 
                   "logistik", "kepemimpinan", "manajemen bisnis", "sumber daya manusia",
                   "layanan pelanggan", "pembentukan merek", "seo", "sem", "pemasaran email"]
    }
}

# ============================================
# AWALAN
# ============================================
awalan = [
    "cara belajar", "cara menguasai", "panduan lengkap", "tutorial", "kursus",
    "menguasai", "memahami", "berlatih", "memecahkan masalah", "latihan",
    "pengantar", "konsep dasar", "manual", "teori",
    "contoh", "dasar-dasar", "tips belajar", "sumber belajar",
    "pelajaran", "pelajaran", "cara meningkatkan", "cara menggunakan"
]

# ============================================
# AKHIRAN
# ============================================
akhiran = [
    "pemula", "menengah", "mahir", "profesional", "lengkap",
    "mudah", "cepat", "untuk pemula", "dari nol", "langkah demi langkah",
    "dengan latihan", "online", "gratis", "tersertifikasi", "tingkat universitas",
    "untuk anak-anak", "untuk dewasa", "intensif", "praktis", "teoretis"
]

# ============================================
# PERTANYAAN
# ============================================
pertanyaan = [
    "apa itu", "bagaimana cara kerjanya", "untuk apa", "di mana belajar",
    "kapan menggunakan", "mengapa penting", "apa manfaatnya",
    "berapa lama belajar", "apa yang perlu untuk belajar"
]

# ============================================
# MEMBUAT KATA KUNCI
# ============================================
kata_kunci = set()

print("🔄 Membuat kata kunci bahasa Indonesia...")

for awal in awalan:
    for cat_data in topik.values():
        for top in cat_data["topik"]:
            kata_kunci.add(f"{awal} {top}")
        for top_khusus in cat_data.get("topik_khusus", []):
            kata_kunci.add(f"{awal} {top_khusus}")

for akh in akhiran:
    for cat_data in topik.values():
        for top in cat_data["topik"][:15]:
            kata_kunci.add(f"{top} {akh}")
        for top_khusus in cat_data.get("topik_khusus", []):
            kata_kunci.add(f"{top_khusus} {akh}")

for tanya in pertanyaan:
    for cat_data in topik.values():
        for top in cat_data["topik"][:15]:
            kata_kunci.add(f"{tanya} {top}")
        for top_khusus in cat_data.get("topik_khusus", []):
            kata_kunci.add(f"{tanya} {top_khusus}")

kata_kerja = ["belajar", "menguasai", "berlatih", "studi", "memahami", "menerapkan"]
for kerja in kata_kerja:
    for cat_data in topik.values():
        for top in cat_data["topik"][:15]:
            kata_kunci.add(f"{kerja} {top}")

for cat_data in topik.values():
    semua_topik = cat_data["topik"] + cat_data.get("topik_khusus", [])
    if len(semua_topik) >= 2:
        for _ in range(min(30, len(semua_topik) * 3)):
            top1, top2 = random.sample(semua_topik, 2)
            kata_kunci.add(f"perbedaan antara {top1} dan {top2}")
            kata_kunci.add(f"{top1} vs {top2}")
            kata_kunci.add(f"perbandingan {top1} dan {top2}")

for cat_data in topik.values():
    for top in cat_data["topik"][:10]:
        kata_kunci.add(f"kesalahan umum dalam {top}")
        kata_kunci.add(f"cara menghindari kesalahan dalam {top}")
        kata_kunci.add(f"solusi masalah {top}")

tingkat = ["dasar", "menengah", "lanjutan", "profesional", "intensif"]
for tkt in tingkat:
    for cat_data in topik.values():
        for top in cat_data["topik"][:12]:
            kata_kunci.add(f"kursus {tkt} {top}")
            kata_kunci.add(f"pelajaran {top} tingkat {tkt}")

for cat_data in topik.values():
    for top in cat_data["topik"][:10]:
        kata_kunci.add(f"sertifikasi dalam {top}")
        kata_kunci.add(f"ujian {top}")
        kata_kunci.add(f"buku tentang {top}")
        kata_kunci.add(f"video tentang {top}")

for cat_data in topik.values():
    for top in cat_data["topik"][:10]:
        kata_kunci.add(f"tips untuk {top}")
        kata_kunci.add(f"saran untuk meningkatkan {top}")

for i in range(1, 2000):
    cat_name = random.choice(list(topik.keys()))
    top = random.choice(topik[cat_name]["topik"])
    kata_kunci.add(f"{top} pelajaran {i}")
    kata_kunci.add(f"{top} bab {i}")
    kata_kunci.add(f"{top} unit {i}")

# ============================================
# BATASI
# ============================================
daftar_kata_kunci = sorted(list(kata_kunci))
random.shuffle(daftar_kata_kunci)

if len(daftar_kata_kunci) < JUMLAH_KATA_KUNCI:
    print(f"⚠ Hanya {len(daftar_kata_kunci)} kata kunci yang dibuat. Mengulang beberapa untuk mencapai {JUMLAH_KATA_KUNCI}...")
    while len(daftar_kata_kunci) < JUMLAH_KATA_KUNCI:
        daftar_kata_kunci.extend(daftar_kata_kunci[:min(1000, JUMLAH_KATA_KUNCI - len(daftar_kata_kunci))])

kata_kunci_akhir = daftar_kata_kunci[:JUMLAH_KATA_KUNCI]
random.shuffle(kata_kunci_akhir)

# ============================================
# SIMPAN
# ============================================
with open('keywords/id.json', 'w', encoding='utf-8') as f:
    json.dump(kata_kunci_akhir, f, indent=2, ensure_ascii=False)

# ============================================
# LAPORAN
# ============================================
print(f"\n✅ {len(kata_kunci_akhir)} kata kunci bahasa Indonesia dibuat")
print(f"📁 Disimpan di: keywords/id.json")
print(f"\n📊 Pratinjau (30 kata kunci pertama):")
for i, kw in enumerate(kata_kunci_akhir[:30]):
    print(f"   {i+1}. {kw}")
