import json
import random

# ============================================
# KONFIGURACJA
# ============================================
LICZBA_SLOW_KLUCZOWYCH = 10000

# ============================================
# TEMATY W JĘZYKU POLSKIM
# ============================================
tematy = {
    "matematyka": {
        "tematy": ["matematyka", "rachunek rozniczkowy", "algebra", "geometria", "trygonometria", 
                   "statystyka", "rachunek prawdopodobienstwa", "pochodne", "calki", "granice", 
                   "funkcje", "macierze", "wektory", "rownania", "logarytmy", 
                   "ulamki", "procenty", "pierwiastki", "potegi", "wielomiany", 
                   "liczby zespolone", "rownania rozniczkowe", "algebra liniowa",
                   "trygonometria sferyczna", "rachunek wektorowy", "topologia", "teoria liczb"]
    },
    "fizyka": {
        "tematy": ["fizyka", "mechanika", "termodynamika", "elektromagnetyzm", "optyka", 
                   "akustyka", "kinematyka", "dynamika", "plyny", "kwantowa", 
                   "teoria wzglednosci", "energia", "praca", "moc", "ruch", 
                   "sily", "grawitacja", "elektrycznosc", "magnetyzm", "fale",
                   "astrofizyka", "kosmologia", "fizyka jadrowa", "fizyka molekularna"]
    },
    "chemia": {
        "tematy": ["chemia", "chemia organiczna", "chemia nieorganiczna", "chemia analityczna", 
                   "biochemia", "reakcje chemiczne", "bilansowanie", "stechiometria", 
                   "tablica okresowa", "wiązania chemiczne", "czasteczki", "atomy", 
                   "zwiazki chemiczne", "kwasy", "zasady", "ph", "roztwory", 
                   "gazy", "termochemia", "chemia kwantowa", "elektrochemia"]
    },
    "biologia": {
        "tematy": ["biologia", "biologia komorki", "biologia molekularna", "genetyka", 
                   "anatomia", "fizjologia", "ekologia", "ewolucja", "botanika", 
                   "zoologia", "mikrobiologia", "dna", "rna", "bialka", "enzymy", 
                   "metabolizm", "komorki", "tkanki", "narzady", "uklady ciala",
                   "neurobiologia", "immunologia", "embriologia"]
    },
    "programowanie": {
        "tematy": ["programowanie", "python", "javascript", "java", "c++", "c#", "php", 
                   "ruby", "swift", "kotlin", "go", "rust", "html", "css", "sql", 
                   "mongodb", "git", "react", "angular", "vue", "nodejs", "django",
                   "flask", "spring boot", "laravel", "typescript", "graphql"]
    },
    "sztuczna_inteligencja": {
        "tematy_specjalne": ["machine learning", "deep learning", "gpt", "llm"],
        "tematy": ["sztuczna inteligencja", "sieci neuronowe", "przetwarzanie jezyka naturalnego", 
                   "widzenie komputerowe", "chatboty", "transformery", "automatyzacja",
                   "uczenie maszynowe", "uczenie glebokie", "nlp", "widzenie komputerowe"]
    },
    "cyberbezpieczenstwo": {
        "tematy": ["cyberbezpieczenstwo", "etyczny hacking", "firewalle", "szyfrowanie", 
                   "bezpieczenstwo informacji", "testy penetracyjne", "malware", "ransomware", 
                   "phishing", "inzynieria spoleczna", "kryptografia", "bezpieczenstwo sieci",
                   "bezpieczenstwo stron", "bezpieczenstwo mobilne", "etyczny hacking"]
    },
    "kuchnia": {
        "tematy": ["kuchnia", "latwe przepisy", "desery", "ciastka", "wypieki", 
                   "kuchnia meksykanska", "kuchnia wloska", "kuchnia hiszpanska", "napoje", 
                   "koktajle", "koktajle", "laczenie win", "wino", "piwo rzemioslnicze",
                   "gastronomia molekularna", "kuchnia vegetarianska", "kuchnia weganska"]
    },
    "sport": {
        "tematy": ["sport", "pilka nozna", "koszykowka", "tenis", "plywanie", "bieganie", 
                   "fitness", "silownia", "joga", "pilates", "crossfit", "zywienie sportowe",
                   "trening funkcjonalny", "kalistenika", "boks", "sztuki walki"]
    },
    "biznes": {
        "tematy": ["biznes", "przedsiebiorczosc", "startupy", "marketing cyfrowy", "sprzedaz", 
                   "finanse osobiste", "inwestycje", "biznes online", "ecommerce", 
                   "logistyka", "przywodztwo", "zarzadzanie firma", "zasoby ludzkie",
                   "obsluga klienta", "branding", "seo", "sem", "email marketing"]
    }
}

# ============================================
# PREFIKSY
# ============================================
prefiksy = [
    "jak sie nauczyc", "jak opanowac", "pelny przewodnik po", "poradnik", "kurs",
    "opanowac", "zrozumiec", "cwiczyc", "rozwiazywac problemy z", "cwiczenia z",
    "wprowadzenie do", "podstawy", "podrecznik", "teoria",
    "przyklady", "fundamenty", "wskazowki jak sie nauczyc", "materialy do nauki",
    "lekcje", "lekcje", "jak sie poprawic w", "jak uzywac"
]

# ============================================
# PRZYDATKI
# ============================================
przyrostki = [
    "podstawowy", "sredniozaawansowany", "zaawansowany", "profesjonalny", "pelny",
    "latwy", "szybki", "dla poczatkujacych", "od zera", "krok po kroku",
    "z cwiczeniami", "online", "darmowy", "certyfikowany", "uniwersytecki",
    "dla dzieci", "dla doroslych", "intensywny", "praktyczny", "teoretyczny"
]

# ============================================
# PYTANIA
# ============================================
pytania = [
    "co to jest", "jak to dziala", "do czego sluzy", "gdzie sie nauczyc",
    "kiedy uzywac", "dlaczego to jest wazne", "jakie sa korzysci z",
    "jak dlugo trwa nauka", "czego potrzebuje do nauki"
]

# ============================================
# GENEROWANIE SLOW KLUCZOWYCH
# ============================================
slowa_kluczowe = set()

print("🔄 Generowanie polskich słów kluczowych...")

# 1. Kombinacje z prefiksami
for prefiks in prefiksy:
    for cat_data in tematy.values():
        for temat in cat_data["tematy"]:
            slowa_kluczowe.add(f"{prefiks} {temat}")
        for temat_spec in cat_data.get("tematy_specjalne", []):
            slowa_kluczowe.add(f"{prefiks} {temat_spec}")

# 2. Kombinacje z przyrostkami
for przyrostek in przyrostki:
    for cat_data in tematy.values():
        for temat in cat_data["tematy"][:15]:
            slowa_kluczowe.add(f"{temat} {przyrostek}")
        for temat_spec in cat_data.get("tematy_specjalne", []):
            slowa_kluczowe.add(f"{temat_spec} {przyrostek}")

# 3. Pytania
for pytanie in pytania:
    for cat_data in tematy.values():
        for temat in cat_data["tematy"][:15]:
            slowa_kluczowe.add(f"{pytanie} {temat}")
        for temat_spec in cat_data.get("tematy_specjalne", []):
            slowa_kluczowe.add(f"{pytanie} {temat_spec}")

# 4. Czasowniki + temat
czasowniki = ["nauczyc sie", "opanowac", "cwiczyc", "studiowac", "zrozumiec", "stosowac"]
for czasownik in czasowniki:
    for cat_data in tematy.values():
        for temat in cat_data["tematy"][:15]:
            slowa_kluczowe.add(f"{czasownik} {temat}")

# 5. Porownania
for cat_data in tematy.values():
    wszystkie_tematy = cat_data["tematy"] + cat_data.get("tematy_specjalne", [])
    if len(wszystkie_tematy) >= 2:
        for _ in range(min(30, len(wszystkie_tematy) * 3)):
            temat1, temat2 = random.sample(wszystkie_tematy, 2)
            slowa_kluczowe.add(f"roznica miedzy {temat1} a {temat2}")
            slowa_kluczowe.add(f"{temat1} vs {temat2}")
            slowa_kluczowe.add(f"porownanie {temat1} vs {temat2}")

# 6. Częste błędy
for cat_data in tematy.values():
    for temat in cat_data["tematy"][:10]:
        slowa_kluczowe.add(f"czeste bledy w {temat}")
        slowa_kluczowe.add(f"jak unikac bledow w {temat}")
        slowa_kluczowe.add(f"rozwiazanie problemow z {temat}")

# 7. Kursy i poziomy
poziomy = ["podstawowy", "sredniozaawansowany", "zaawansowany", "profesjonalny", "intensywny"]
for poziom in poziomy:
    for cat_data in tematy.values():
        for temat in cat_data["tematy"][:12]:
            slowa_kluczowe.add(f"kurs {poziom} z {temat}")
            slowa_kluczowe.add(f"lekcje {temat} poziom {poziom}")

# 8. Certyfikaty i zasoby
for cat_data in tematy.values():
    for temat in cat_data["tematy"][:10]:
        slowa_kluczowe.add(f"certyfikat z {temat}")
        slowa_kluczowe.add(f"egzamin z {temat}")
        slowa_kluczowe.add(f"ksiazki o {temat}")
        slowa_kluczowe.add(f"filmy o {temat}")

# 9. Wskazowki
for cat_data in tematy.values():
    for temat in cat_data["tematy"][:10]:
        slowa_kluczowe.add(f"wskazowki dla {temat}")
        slowa_kluczowe.add(f"rady jak poprawic sie w {temat}")

# 10. Wariacje numeryczne
for i in range(1, 2000):
    cat_name = random.choice(list(tematy.keys()))
    temat = random.choice(tematy[cat_name]["tematy"])
    slowa_kluczowe.add(f"lekcja {i} z {temat}")
    slowa_kluczowe.add(f"rozdzial {i} z {temat}")
    slowa_kluczowe.add(f"jednostka {i} z {temat}")

# ============================================
# OGRANICZENIE
# ============================================
lista_slow = sorted(list(slowa_kluczowe))
random.shuffle(lista_slow)

if len(lista_slow) < LICZBA_SLOW_KLUCZOWYCH:
    print(f"⚠ Wygenerowano tylko {len(lista_slow)} słów kluczowych. Powtarzanie niektórych, aby osiągnąć {LICZBA_SLOW_KLUCZOWYCH}...")
    while len(lista_slow) < LICZBA_SLOW_KLUCZOWYCH:
        lista_slow.extend(lista_slow[:min(1000, LICZBA_SLOW_KLUCZOWYCH - len(lista_slow))])

slowa_finalne = lista_slow[:LICZBA_SLOW_KLUCZOWYCH]
random.shuffle(slowa_finalne)

# ============================================
# ZAPIS
# ============================================
with open('keywords/pl.json', 'w', encoding='utf-8') as f:
    json.dump(slowa_finalne, f, indent=2, ensure_ascii=False)

# ============================================
# RAPORT
# ============================================
print(f"\n✅ Wygenerowano {len(slowa_finalne)} słów kluczowych w języku polskim")
print(f"📁 Zapisano w: keywords/pl.json")
print(f"\n📊 Podgląd (pierwsze 30 słów kluczowych):")
for i, kw in enumerate(slowa_finalne[:30]):
    print(f"   {i+1}. {kw}")
