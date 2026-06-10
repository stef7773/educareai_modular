import json
import random

# ============================================
# KONFIGÜRASYON
# ============================================
ANAHTAR_KELIME_SAYISI = 10000

# ============================================
# TÜRKÇE KONULAR
# ============================================
konular = {
    "matematik": {
        "konular": ["matematik", "kalkülüs", "cebir", "geometri", "trigonometri", 
                   "istatistik", "olasılık", "türevler", "integraller", "limitler", 
                   "fonksiyonlar", "matrisler", "vektörler", "denklemler", "logaritmalar", 
                   "kesirler", "yüzdeler", "kökler", "üsler", "polinomlar", 
                   "karmaşık sayılar", "diferansiyel denklemler", "lineer cebir",
                   "küresel trigonometri", "vektörel analiz", "topoloji", "sayı teorisi"]
    },
    "fizik": {
        "konular": ["fizik", "mekanik", "termodinamik", "elektromanyetizma", "optik", 
                   "akustik", "kinematik", "dinamik", "akışkanlar", "kuantum", 
                   "görelilik", "enerji", "iş", "güç", "hareket", 
                   "kuvvetler", "yerçekimi", "elektrik", "manyetizma", "dalgalar",
                   "astrofizik", "kozmolojik", "nükleer fizik", "moleküler fizik"]
    },
    "kimya": {
        "konular": ["kimya", "organik kimya", "inorganik kimya", "analitik kimya", 
                   "biyokimya", "kimyasal reaksiyonlar", "denkleştirme", "stokiyometri", 
                   "periyodik tablo", "kimyasal bağlar", "moleküller", "atomlar", 
                   "kimyasal bileşikler", "asitler", "bazlar", "ph", "çözeltiler", 
                   "gazlar", "termokimya", "kuantum kimyası", "elektrokimya"]
    },
    "biyoloji": {
        "konular": ["biyoloji", "hücre biyolojisi", "moleküler biyoloji", "genetik", 
                   "anatomi", "fizyoloji", "ekoloji", "evrim", "botanik", 
                   "zooloji", "mikrobiyoloji", "dna", "rna", "proteinler", "enzimler", 
                   "metabolizma", "hücreler", "dokular", "organlar", "vücut sistemleri",
                   "nörobilim", "immünoloji", "embriyoloji"]
    },
    "programlama": {
        "konular": ["programlama", "python", "javascript", "java", "c++", "c#", "php", 
                   "ruby", "swift", "kotlin", "go", "rust", "html", "css", "sql", 
                   "mongodb", "git", "react", "angular", "vue", "nodejs", "django",
                   "flask", "spring boot", "laravel", "typescript", "graphql"]
    },
    "yapay_zeka": {
        "konular_ozel": ["makine öğrenmesi", "derin öğrenme", "gpt", "llm"],
        "konular": ["yapay zeka", "sinir ağları", "doğal dil işleme", 
                   "bilgisayarlı görü", "sohbet robotları", "dönüştürücüler", "otomasyon",
                   "makine öğrenmesi", "derin öğrenme", "doğal dil işleme", "bilgisayarlı görü"]
    },
    "siber_güvenlik": {
        "konular": ["siber güvenlik", "etik hackleme", "güvenlik duvarları", "şifreleme", 
                   "bilgi güvenliği", "sızma testi", "kötü amaçlı yazılım", "fidye yazılımı", 
                   "oltalama", "sosyal mühendislik", "kriptografi", "ağ güvenliği",
                   "web güvenliği", "mobil güvenlik", "etik hackleme"]
    },
    "yemek": {
        "konular": ["yemek", "kolay tarifler", "tatlılar", "pişirme", "hamur işleri", 
                   "meksika yemekleri", "italyan yemekleri", "ispanyol yemekleri", "içecekler", 
                   "kokteyller", "kokteyller", "şarap eşleştirmesi", "şarap", "el yapımı bira",
                   "moleküler gastronomi", "vejetaryen yemek", "vegan yemek"]
    },
    "spor": {
        "konular": ["spor", "futbol", "basketbol", "tenis", "yüzme", "koşu", 
                   "fitness", "spor salonu", "yoga", "pilates", "crossfit", "spor beslenmesi",
                   "fonksiyonel antrenman", "kalistenik", "boks", "dövüş sanatları"]
    },
    "iş": {
        "konular": ["iş", "girişimcilik", "startuplar", "dijital pazarlama", "satış", 
                   "kişisel finans", "yatırımlar", "çevrimiçi iş", "e-ticaret", 
                   "lojistik", "liderlik", "iş yönetimi", "insan kaynakları",
                   "müşteri hizmetleri", "markalaşma", "seo", "sem", "e-posta pazarlaması"]
    }
}

# ============================================
# ÖNEKLER
# ============================================
onekler = [
    "nasıl öğrenilir", "nasıl ustalaşılır", "tam kılavuz", "eğitici", "kurs",
    "ustalaşmak", "anlamak", "pratik yapmak", "problemleri çözmek", "alıştırmalar",
    "giriş", "temel kavramlar", "kılavuz", "teori",
    "örnekler", "temel bilgiler", "öğrenme ipuçları", "çalışma kaynakları",
    "dersler", "dersler", "nasıl geliştirilir", "nasıl kullanılır"
]

# ============================================
# SONEKLER
# ============================================
sonekler = [
    "başlangıç", "orta seviye", "ileri seviye", "profesyonel", "tam",
    "kolay", "hızlı", "yeni başlayanlar için", "sıfırdan", "adım adım",
    "alıştırmalı", "çevrimiçi", "ücretsiz", "sertifikalı", "üniversite seviyesi",
    "çocuklar için", "yetişkinler için", "yoğun", "pratik", "teorik"
]

# ============================================
# SORULAR
# ============================================
sorular = [
    "nedir", "nasıl çalışır", "ne işe yarar", "nerede öğrenilir",
    "ne zaman kullanılır", "neden önemlidir", "faydaları nelerdir",
    "öğrenmek ne kadar sürer", "çalışmak için ne gerekir"
]

# ============================================
# ANAHTAR KELİME ÜRETİMİ
# ============================================
anahtar_kelimeler = set()

print("🔄 Türkçe anahtar kelimeler üretiliyor...")

# 1. Öneklerle kombinasyonlar
for onek in onekler:
    for cat_data in konular.values():
        for konu in cat_data["konular"]:
            anahtar_kelimeler.add(f"{onek} {konu}")
        for konu_ozel in cat_data.get("konular_ozel", []):
            anahtar_kelimeler.add(f"{onek} {konu_ozel}")

# 2. Son eklerle kombinasyonlar
for sonek in sonekler:
    for cat_data in konular.values():
        for konu in cat_data["konular"][:15]:
            anahtar_kelimeler.add(f"{konu} {sonek}")
        for konu_ozel in cat_data.get("konular_ozel", []):
            anahtar_kelimeler.add(f"{konu_ozel} {sonek}")

# 3. Sorular
for soru in sorular:
    for cat_data in konular.values():
        for konu in cat_data["konular"][:15]:
            anahtar_kelimeler.add(f"{soru} {konu}")
        for konu_ozel in cat_data.get("konular_ozel", []):
            anahtar_kelimeler.add(f"{soru} {konu_ozel}")

# 4. Fiiller + konu
fiiller = ["öğren", "usta ol", "pratik yap", "çalış", "anla", "uygula"]
for fiil in fiiller:
    for cat_data in konular.values():
        for konu in cat_data["konular"][:15]:
            anahtar_kelimeler.add(f"{fiil} {konu}")

# 5. Karşılaştırmalar
for cat_data in konular.values():
    tum_konular = cat_data["konular"] + cat_data.get("konular_ozel", [])
    if len(tum_konular) >= 2:
        for _ in range(min(30, len(tum_konular) * 3)):
            konu1, konu2 = random.sample(tum_konular, 2)
            anahtar_kelimeler.add(f"{konu1} ve {konu2} arasındaki fark")
            anahtar_kelimeler.add(f"{konu1} vs {konu2}")
            anahtar_kelimeler.add(f"{konu1} ve {konu2} karşılaştırması")

# 6. Yaygın hatalar
for cat_data in konular.values():
    for konu in cat_data["konular"][:10]:
        anahtar_kelimeler.add(f"{konu} içindeki yaygın hatalar")
        anahtar_kelimeler.add(f"{konu} içindeki hatalardan nasıl kaçınılır")
        anahtar_kelimeler.add(f"{konu} sorunlarına çözümler")

# 7. Kurslar ve seviyeler
seviyeler = ["başlangıç", "orta", "ileri", "profesyonel", "yoğun"]
for seviye in seviyeler:
    for cat_data in konular.values():
        for konu in cat_data["konular"][:12]:
            anahtar_kelimeler.add(f"{seviye} {konu} kursu")
            anahtar_kelimeler.add(f"{konu} {seviye} seviye dersler")

# 8. Sertifikalar ve kaynaklar
for cat_data in konular.values():
    for konu in cat_data["konular"][:10]:
        anahtar_kelimeler.add(f"{konu} sertifikası")
        anahtar_kelimeler.add(f"{konu} sınavı")
        anahtar_kelimeler.add(f"{konu} kitapları")
        anahtar_kelimeler.add(f"{konu} videoları")

# 9. İpuçları
for cat_data in konular.values():
    for konu in cat_data["konular"][:10]:
        anahtar_kelimeler.add(f"{konu} için ipuçları")
        anahtar_kelimeler.add(f"{konu} içinde gelişmek için tavsiyeler")

# 10. Sayısal varyasyonlar
for i in range(1, 2000):
    cat_name = random.choice(list(konular.keys()))
    konu = random.choice(konular[cat_name]["konular"])
    anahtar_kelimeler.add(f"{konu} ders {i}")
    anahtar_kelimeler.add(f"{konu} bölüm {i}")
    anahtar_kelimeler.add(f"{konu} ünite {i}")

# ============================================
# SINIRLANDIR
# ============================================
kelime_listesi = sorted(list(anahtar_kelimeler))
random.shuffle(kelime_listesi)

if len(kelime_listesi) < ANAHTAR_KELIME_SAYISI:
    print(f"⚠ Sadece {len(kelime_listesi)} anahtar kelime üretildi. {ANAHTAR_KELIME_SAYISI}'ye ulaşmak için bazıları tekrarlanıyor...")
    while len(kelime_listesi) < ANAHTAR_KELIME_SAYISI:
        kelime_listesi.extend(kelime_listesi[:min(1000, ANAHTAR_KELIME_SAYISI - len(kelime_listesi))])

son_kelimeler = kelime_listesi[:ANAHTAR_KELIME_SAYISI]
random.shuffle(son_kelimeler)

# ============================================
# KAYDET
# ============================================
with open('keywords/tr.json', 'w', encoding='utf-8') as f:
    json.dump(son_kelimeler, f, indent=2, ensure_ascii=False)

# ============================================
# RAPOR
# ============================================
print(f"\n✅ {len(son_kelimeler)} Türkçe anahtar kelime üretildi")
print(f"📁 Kaydedildi: keywords/tr.json")
print(f"\n📊 Önizleme (ilk 30 anahtar kelime):")
for i, kw in enumerate(son_kelimeler[:30]):
    print(f"   {i+1}. {kw}")

