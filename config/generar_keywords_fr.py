import json
import random

# ============================================
# CONFIGURATION
# ============================================
CANTIDAD_KEYWORDS = 10000

# ============================================
# SUJETS EN FRANÇAIS
# ============================================
sujets = {
    "mathematiques": {
        "sujets": ["mathematiques", "calcul", "algebre", "geometrie", "trigonometrie", 
                   "statistiques", "probabilites", "derivees", "integrales", "limites", 
                   "fonctions", "matrices", "vecteurs", "equations", "logarithmes", 
                   "fractions", "pourcentages", "racines", "puissances", "polynomes", 
                   "nombres complexes", "equations differentielles", "algebre lineaire",
                   "trigonometrie spherique", "calcul vectoriel", "topologie", "theorie des nombres"]
    },
    "physique": {
        "sujets": ["physique", "mecanique", "thermodynamique", "electromagnetisme", "optique", 
                   "acoustique", "cinematique", "dynamique", "fluides", "quantique", 
                   "relativite", "energie", "travail", "puissance", "mouvement", "forces", 
                   "gravite", "electricite", "magnetisme", "ondes",
                   "astrophysique", "cosmologie", "physique nucleaire", "physique moleculaire"]
    },
    "chimie": {
        "sujets": ["chimie", "chimie organique", "chimie inorganique", "chimie analytique", 
                   "biochimie", "reactions chimiques", "equilibrage", "stoechiometrie", 
                   "tableau periodique", "liaisons chimiques", "molecules", "atomes", 
                   "composes chimiques", "acides", "bases", "ph", "solutions", 
                   "gaz", "thermochimie", "chimie quantique", "electrochimie"]
    },
    "biologie": {
        "sujets": ["biologie", "biologie cellulaire", "biologie moleculaire", "genetique", 
                   "anatomie", "physiologie", "ecologie", "evolution", "botanique", 
                   "zoologie", "microbiologie", "adn", "arn", "proteines", "enzymes", 
                   "metabolisme", "cellules", "tissus", "organes", "systemes du corps",
                   "neuroscience", "immunologie", "embryologie"]
    },
    "programmation": {
        "sujets": ["programmation", "python", "javascript", "java", "c++", "c#", "php", 
                   "ruby", "swift", "kotlin", "go", "rust", "html", "css", "sql", 
                   "mongodb", "git", "react", "angular", "vue", "nodejs", "django",
                   "flask", "spring boot", "laravel", "typescript", "graphql"]
    },
    "intelligence_artificielle": {
        "sujets_speciaux": ["machine learning", "deep learning", "gpt", "llm"],
        "sujets": ["intelligence artificielle", "reseaux de neurones", "traitement du langage naturel", 
                   "vision par ordinateur", "chatbots", "transformers", "automatisation",
                   "apprentissage automatique", "apprentissage profond", "tln", "vision par ordinateur"]
    },
    "cybersecurite": {
        "sujets": ["cybersecurite", "hacking ethique", "firewalls", "cryptage", 
                   "securite informatique", "test de penetration", "malware", "ransomware", 
                   "phishing", "ingenierie sociale", "cryptographie", "securite reseau",
                   "securite web", "securite mobile", "hacking ethique"]
    },
    "cuisine": {
        "sujets": ["cuisine", "recettes faciles", "desserts", "patisserie", "viennoiseries", 
                   "cuisine mexicaine", "cuisine italienne", "cuisine espagnole", "boissons", 
                   "cocktails", "cocktails", "accords mets et vins", "vin", "biere artisanale",
                   "gastronomie moleculaire", "cuisine vegetarienne", "cuisine vegane"]
    },
    "sports": {
        "sujets": ["sports", "football", "basketball", "tennis", "natation", "course a pied", 
                   "fitness", "salle de sport", "yoga", "pilates", "crossfit", "nutrition sportive",
                   "entrainement fonctionnel", "callisthenie", "boxe", "arts martiaux"]
    },
    "affaires": {
        "sujets": ["affaires", "entrepreneuriat", "startups", "marketing digital", "ventes", 
                   "finances personnelles", "investissements", "business en ligne", "ecommerce", 
                   "logistique", "leadership", "gestion d'entreprise", "ressources humaines",
                   "service client", "image de marque", "seo", "sem", "email marketing"]
    }
}

# ============================================
# PRÉFIXES
# ============================================
prefices = [
    "comment apprendre", "comment maitriser", "guide complet de", "tutoriel sur", "cours de",
    "maitriser", "comprendre", "pratiquer", "resoudre des problemes de", "exercices de",
    "introduction a", "concepts de base de", "manuel de", "theorie de",
    "exemples de", "fondamentaux de", "conseils pour apprendre", "ressources pour etudier",
    "cours de", "lecons de", "comment sameliorer en", "comment utiliser"
]

# ============================================
# SUFFIXES
# ============================================
suffixes = [
    "debutant", "intermediaire", "avance", "professionnel", "complet",
    "facile", "rapide", "pour debutants", "a partir de zero", "pas a pas",
    "avec exercices", "en ligne", "gratuit", "certifie", "universitaire",
    "pour enfants", "pour adultes", "intensif", "pratique", "theorique"
]

# ============================================
# QUESTIONS
# ============================================
questions = [
    "quest ce que", "comment ca fonctionne", "a quoi ca sert", "ou apprendre",
    "quand utiliser", "pourquoi est ce important", "quels sont les avantages de",
    "combien de temps faut il pour apprendre", "de quoi ai je besoin pour etudier"
]

# ============================================
# GÉNÉRATION DES MOTS CLÉS
# ============================================
mots_cles = set()

print("🔄 Génération des mots clés en français...")

# 1. Combinaisons avec préfixes
for prefixe in prefices:
    for cat_data in sujets.values():
        for sujet in cat_data["sujets"]:
            mots_cles.add(f"{prefixe} {sujet}")
        for sujet_spec in cat_data.get("sujets_speciaux", []):
            mots_cles.add(f"{prefixe} {sujet_spec}")

# 2. Combinaisons avec suffixes
for suffixe in suffixes:
    for cat_data in sujets.values():
        for sujet in cat_data["sujets"][:15]:
            mots_cles.add(f"{sujet} {suffixe}")
        for sujet_spec in cat_data.get("sujets_speciaux", []):
            mots_cles.add(f"{sujet_spec} {suffixe}")

# 3. Questions
for question in questions:
    for cat_data in sujets.values():
        for sujet in cat_data["sujets"][:15]:
            mots_cles.add(f"{question} {sujet}")
        for sujet_spec in cat_data.get("sujets_speciaux", []):
            mots_cles.add(f"{question} {sujet_spec}")

# 4. Verbes + sujet
verbes = ["apprendre", "maitriser", "pratiquer", "etudier", "comprendre", "appliquer"]
for verbe in verbes:
    for cat_data in sujets.values():
        for sujet in cat_data["sujets"][:15]:
            mots_cles.add(f"{verbe} {sujet}")

# 5. Comparaisons
for cat_data in sujets.values():
    tous_sujets = cat_data["sujets"] + cat_data.get("sujets_speciaux", [])
    if len(tous_sujets) >= 2:
        for _ in range(min(30, len(tous_sujets) * 3)):
            sujet1, sujet2 = random.sample(tous_sujets, 2)
            mots_cles.add(f"difference entre {sujet1} et {sujet2}")
            mots_cles.add(f"{sujet1} vs {sujet2}")
            mots_cles.add(f"comparaison {sujet1} vs {sujet2}")

# 6. Erreurs courantes
for cat_data in sujets.values():
    for sujet in cat_data["sujets"][:10]:
        mots_cles.add(f"erreurs courantes en {sujet}")
        mots_cles.add(f"comment eviter les erreurs en {sujet}")
        mots_cles.add(f"solutions aux problemes de {sujet}")

# 7. Cours et niveaux
niveaux = ["debutant", "intermediaire", "avance", "professionnel", "intensif"]
for niveau in niveaux:
    for cat_data in sujets.values():
        for sujet in cat_data["sujets"][:12]:
            mots_cles.add(f"cours {niveau} de {sujet}")
            mots_cles.add(f"cours de {sujet} niveau {niveau}")

# 8. Certifications et ressources
for cat_data in sujets.values():
    for sujet in cat_data["sujets"][:10]:
        mots_cles.add(f"certification en {sujet}")
        mots_cles.add(f"examen de {sujet}")
        mots_cles.add(f"livres de {sujet}")
        mots_cles.add(f"videos de {sujet}")

# 9. Conseils
for cat_data in sujets.values():
    for sujet in cat_data["sujets"][:10]:
        mots_cles.add(f"conseils pour {sujet}")
        mots_cles.add(f"astuces pour sameliorer en {sujet}")

# 10. Variations numériques
for i in range(1, 2000):
    cat_name = random.choice(list(sujets.keys()))
    sujet = random.choice(sujets[cat_name]["sujets"])
    mots_cles.add(f"lecon {i} de {sujet}")
    mots_cles.add(f"chapitre {i} de {sujet}")
    mots_cles.add(f"unite {i} de {sujet}")

# ============================================
# LIMITATION
# ============================================
liste_mots_cles = sorted(list(mots_cles))
random.shuffle(liste_mots_cles)

if len(liste_mots_cles) < CANTIDAD_KEYWORDS:
    print(f"⚠ Seulement {len(liste_mots_cles)} mots clés générés. Répétition de certains pour atteindre {CANTIDAD_KEYWORDS}...")
    while len(liste_mots_cles) < CANTIDAD_KEYWORDS:
        liste_mots_cles.extend(liste_mots_cles[:min(1000, CANTIDAD_KEYWORDS - len(liste_mots_cles))])

mots_cles_final = liste_mots_cles[:CANTIDAD_KEYWORDS]
random.shuffle(mots_cles_final)

# ============================================
# SAUVEGARDE
# ============================================
with open('keywords/fr.json', 'w', encoding='utf-8') as f:
    json.dump(mots_cles_final, f, indent=2, ensure_ascii=False)

# ============================================
# RAPPORT
# ============================================
print(f"\n✅ {len(mots_cles_final)} mots clés générés en français")
print(f"📁 Sauvegardé dans: keywords/fr.json")
print(f"\n📊 Aperçu (30 premiers mots clés):")
for i, kw in enumerate(mots_cles_final[:30]):
    print(f"   {i+1}. {kw}")
