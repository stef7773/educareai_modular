import json
import random

# ============================================
# CONFIGURACIÓN
# ============================================
CANTIDAD_KEYWORDS = 10000

# ============================================
# TOPICS IN ENGLISH
# ============================================
topics = {
    "mathematics": {
        "topics": ["mathematics", "calculus", "algebra", "geometry", "trigonometry", 
                   "statistics", "probability", "derivatives", "integrals", "limits", 
                   "functions", "matrices", "vectors", "equations", "logarithms", 
                   "fractions", "percentages", "roots", "powers", "polynomials", 
                   "complex numbers", "differential equations", "linear algebra",
                   "spherical trigonometry", "vector calculus", "topology", "number theory"]
    },
    "physics": {
        "topics": ["physics", "mechanics", "thermodynamics", "electromagnetism", "optics", 
                   "acoustics", "kinematics", "dynamics", "fluids", "quantum", 
                   "relativity", "energy", "work", "power", "motion", "forces", 
                   "gravity", "electricity", "magnetism", "waves",
                   "astrophysics", "cosmology", "nuclear physics", "molecular physics"]
    },
    "chemistry": {
        "topics": ["chemistry", "organic chemistry", "inorganic chemistry", "analytical chemistry", 
                   "biochemistry", "chemical reactions", "balancing", "stoichiometry", 
                   "periodic table", "chemical bonds", "molecules", "atoms", 
                   "chemical compounds", "acids", "bases", "ph", "solutions", 
                   "gases", "thermochemistry", "quantum chemistry", "electrochemistry"]
    },
    "biology": {
        "topics": ["biology", "cell biology", "molecular biology", "genetics", 
                   "anatomy", "physiology", "ecology", "evolution", "botany", 
                   "zoology", "microbiology", "dna", "rna", "proteins", "enzymes", 
                   "metabolism", "cells", "tissues", "organs", "body systems",
                   "neuroscience", "immunology", "embryology"]
    },
    "programming": {
        "topics": ["programming", "python", "javascript", "java", "c++", "c#", "php", 
                   "ruby", "swift", "kotlin", "go", "rust", "html", "css", "sql", 
                   "mongodb", "git", "react", "angular", "vue", "nodejs", "django",
                   "flask", "spring boot", "laravel", "typescript", "graphql"]
    },
    "artificial_intelligence": {
        "topics_special": ["machine learning", "deep learning", "gpt", "llm"],
        "topics": ["artificial intelligence", "neural networks", "natural language processing", 
                   "computer vision", "chatbots", "transformers", "automation",
                   "machine learning", "deep learning", "nlp", "computer vision"]
    },
    "cybersecurity": {
        "topics": ["cybersecurity", "ethical hacking", "firewalls", "encryption", 
                   "information security", "pentesting", "malware", "ransomware", 
                   "phishing", "social engineering", "cryptography", "network security",
                   "web security", "mobile security", "ethical hacking"]
    },
    "cooking": {
        "topics": ["cooking", "easy recipes", "desserts", "baking", "pastry", 
                   "mexican food", "italian food", "spanish food", "drinks", 
                   "cocktails", "cocktails", "pairing", "wine", "craft beer",
                   "molecular gastronomy", "vegetarian cooking", "vegan cooking"]
    },
    "sports": {
        "topics": ["sports", "soccer", "basketball", "tennis", "swimming", "running", 
                   "fitness", "gym", "yoga", "pilates", "crossfit", "sports nutrition",
                   "functional training", "calisthenics", "boxing", "martial arts"]
    },
    "business": {
        "topics": ["business", "entrepreneurship", "startups", "digital marketing", "sales", 
                   "personal finance", "investments", "online business", "ecommerce", 
                   "logistics", "leadership", "business management", "human resources",
                   "customer service", "branding", "seo", "sem", "email marketing"]
    }
}

# ============================================
# PREFIXES (no forced prepositions)
# ============================================
prefixes = [
    "how to learn", "how to master", "complete guide to", "tutorial on", "course on",
    "master", "understand", "practice", "solve problems of", "exercises on",
    "introduction to", "basics of", "manual of", "theory of",
    "examples of", "fundamentals of", "tips to learn", "resources to study",
    "classes on", "lessons on", "how to improve in", "how to use"
]

# ============================================
# SUFFIXES
# ============================================
suffixes = [
    "basics", "intermediate", "advanced", "professional", "complete",
    "easy", "fast", "for beginners", "from scratch", "step by step",
    "with exercises", "online", "free", "certified", "university level",
    "for kids", "for adults", "intensive", "practical", "theoretical"
]

# ============================================
# QUESTIONS
# ============================================
questions = [
    "what is", "how does it work", "what is it for", "where to learn",
    "when to use", "why is it important", "what are the benefits of",
    "how long does it take to learn", "what do I need to study"
]

# ============================================
# GENERATION OF KEYWORDS
# ============================================
keywords = set()

print("🔄 Generating English keywords...")

# 1. Combinations with prefixes (2000 - 3000 keywords)
for prefix in prefixes:
    for cat_data in topics.values():
        for topic in cat_data["topics"]:
            keywords.add(f"{prefix} {topic}")
        for topic_spec in cat_data.get("topics_special", []):
            keywords.add(f"{prefix} {topic_spec}")

# 2. Combinations with suffixes (1500 - 2000 keywords)
for suffix in suffixes:
    for cat_data in topics.values():
        for topic in cat_data["topics"][:15]:
            keywords.add(f"{topic} {suffix}")
        for topic_spec in cat_data.get("topics_special", []):
            keywords.add(f"{topic_spec} {suffix}")

# 3. Questions (1000 - 1500 keywords)
for question in questions:
    for cat_data in topics.values():
        for topic in cat_data["topics"][:15]:
            keywords.add(f"{question} {topic}")
        for topic_spec in cat_data.get("topics_special", []):
            keywords.add(f"{question} {topic_spec}")

# 4. Verbs + topic (800 - 1000 keywords)
verbs = ["learn", "master", "practice", "study", "understand", "apply"]
for verb in verbs:
    for cat_data in topics.values():
        for topic in cat_data["topics"][:15]:
            keywords.add(f"{verb} {topic}")

# 5. Smart comparisons within same category (500 - 800 keywords)
for cat_data in topics.values():
    all_topics = cat_data["topics"] + cat_data.get("topics_special", [])
    if len(all_topics) >= 2:
        for _ in range(min(30, len(all_topics) * 3)):
            topic1, topic2 = random.sample(all_topics, 2)
            keywords.add(f"difference between {topic1} and {topic2}")
            keywords.add(f"{topic1} vs {topic2}")
            keywords.add(f"comparison {topic1} vs {topic2}")

# 6. Common errors
for cat_data in topics.values():
    for topic in cat_data["topics"][:10]:
        keywords.add(f"common errors in {topic}")
        keywords.add(f"how to avoid errors in {topic}")
        keywords.add(f"solutions to {topic} problems")

# 7. Courses and levels (800 - 1000 keywords)
levels = ["basic", "intermediate", "advanced", "professional", "intensive"]
for level in levels:
    for cat_data in topics.values():
        for topic in cat_data["topics"][:12]:
            keywords.add(f"{level} course on {topic}")
            keywords.add(f"{topic} classes {level} level")

# 8. Certifications and resources (600 - 800 keywords)
for cat_data in topics.values():
    for topic in cat_data["topics"][:10]:
        keywords.add(f"certification in {topic}")
        keywords.add(f"{topic} exam")
        keywords.add(f"{topic} books")
        keywords.add(f"{topic} videos")

# 9. Tips and advice (600 - 800 keywords)
for cat_data in topics.values():
    for topic in cat_data["topics"][:10]:
        keywords.add(f"tips for {topic}")
        keywords.add(f"advice to improve in {topic}")

# 10. Numerical variations (to ensure reaching 10000)
for i in range(1, 2000):
    cat_name = random.choice(list(topics.keys()))
    topic = random.choice(topics[cat_name]["topics"])
    keywords.add(f"lesson {i} of {topic}")
    keywords.add(f"chapter {i} of {topic}")
    keywords.add(f"unit {i} of {topic}")

# ============================================
# LIMIT TO DESIRED AMOUNT
# ============================================
keywords_list = sorted(list(keywords))
random.shuffle(keywords_list)

if len(keywords_list) < CANTIDAD_KEYWORDS:
    print(f"⚠ Only {len(keywords_list)} keywords generated. Repeating some to reach {CANTIDAD_KEYWORDS}...")
    while len(keywords_list) < CANTIDAD_KEYWORDS:
        keywords_list.extend(keywords_list[:min(1000, CANTIDAD_KEYWORDS - len(keywords_list))])

keywords_final = keywords_list[:CANTIDAD_KEYWORDS]
random.shuffle(keywords_final)

# ============================================
# SAVE
# ============================================
with open('keywords/en.json', 'w', encoding='utf-8') as f:
    json.dump(keywords_final, f, indent=2, ensure_ascii=False)

# ============================================
# REPORT
# ============================================
print(f"\n✅ Generated {len(keywords_final)} keywords in English")
print(f"📁 Saved in: keywords/en.json")
print(f"\n📊 Preview (first 30 keywords):")
for i, kw in enumerate(keywords_final[:30]):
    print(f"   {i+1}. {kw}")
