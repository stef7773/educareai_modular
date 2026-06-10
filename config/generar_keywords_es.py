import json
import random

# ============================================
# CONFIGURACIÓN
# ============================================
CANTIDAD_KEYWORDS = 10000

# ============================================
# TEMAS CON ARTÍCULOS CORRECTOS
# ============================================
temas = {
    "matematicas": {
        "articulo": "las",
        "temas": ["matematicas", "calculo", "algebra", "geometria", "trigonometria", 
                  "estadistica", "probabilidad", "derivadas", "integrales", "limites", 
                  "funciones", "matrices", "vectores", "ecuaciones", "logaritmos", 
                  "fracciones", "porcentajes", "raices", "potencias", "polinomios", 
                  "numeros complejos", "ecuaciones diferenciales", "algebra lineal",
                  "trigonometria esferica", "calculo vectorial", "topologia", "teoria de numeros"]
    },
    "fisica": {
        "articulo": "la",
        "temas": ["fisica", "mecanica", "termodinamica", "electromagnetismo", "optica", 
                  "acustica", "cinematica", "dinamica", "fluidos", "cuantica", 
                  "relatividad", "energia", "trabajo", "potencia", "movimiento", 
                  "fuerzas", "gravedad", "electricidad", "magnetismo", "ondas",
                  "astrofisica", "cosmologia", "fisica nuclear", "fisica molecular"]
    },
    "quimica": {
        "articulo": "la",
        "temas": ["quimica", "quimica organica", "quimica inorganica", "quimica analitica", 
                  "bioquimica", "reacciones quimicas", "balanceo", "estequiometria", 
                  "tabla periodica", "enlaces quimicos", "moleculas", "atomos", 
                  "compuestos quimicos", "acidos", "bases", "ph", "soluciones", 
                  "gases", "termoquimica", "quimica cuantica", "electroquimica"]
    },
    "biologia": {
        "articulo": "la",
        "temas": ["biologia", "biologia celular", "biologia molecular", "genetica", 
                  "anatomia", "fisiologia", "ecologia", "evolucion", "botanica", 
                  "zoologia", "microbiologia", "adn", "arn", "proteinas", "enzimas", 
                  "metabolismo", "celulas", "tejidos", "organos", "sistemas del cuerpo",
                  "neurociencia", "inmunologia", "embriologia"]
    },
    "programacion": {
        "articulo": "la",
        "temas": ["programacion", "python", "javascript", "java", "c++", "c#", "php", 
                  "ruby", "swift", "kotlin", "go", "rust", "html", "css", "sql", 
                  "mongodb", "git", "react", "angular", "vue", "nodejs", "django",
                  "flask", "spring boot", "laravel", "typescript", "graphql"]
    },
    "inteligencia_artificial": {
        "articulo": "la",
        "temas_especiales": ["machine learning", "deep learning", "gpt", "llm"],
        "temas": ["inteligencia artificial", "redes neuronales", "procesamiento de lenguaje natural", 
                  "vision artificial", "chatbots", "transformers", "automatizacion",
                  "aprendizaje automatico", "aprendizaje profundo", "nlp", "computer vision"]
    },
    "ciberseguridad": {
        "articulo": "la",
        "temas": ["ciberseguridad", "hacking etico", "firewalls", "encriptacion", 
                  "seguridad informatica", "pentesting", "malware", "ransomware", 
                  "phishing", "ingenieria social", "cryptografia", "seguridad en redes",
                  "seguridad web", "seguridad movil", "ethical hacking"]
    },
    "cocina": {
        "articulo": "la",
        "temas": ["cocina", "recetas faciles", "postres", "pasteleria", "reposteria", 
                  "comida mexicana", "comida italiana", "comida española", "bebidas", 
                  "cocteles", "cocktails", "maridaje", "vino", "cerveza artesanal",
                  "gastronomia molecular", "cocina vegetariana", "cocina vegana"]
    },
    "deportes": {
        "articulo": "los",
        "temas": ["deportes", "futbol", "baloncesto", "tenis", "natacion", "running", 
                  "fitness", "gimnasio", "yoga", "pilates", "crossfit", "nutricion deportiva",
                  "entrenamiento funcional", "calistenia", "boxeo", "artes marciales"]
    },
    "negocios": {
        "articulo": "los",
        "temas": ["negocios", "emprendimiento", "startups", "marketing digital", "ventas", 
                  "finanzas personales", "inversiones", "negocios online", "ecommerce", 
                  "logistica", "liderazgo", "gestion empresarial", "recursos humanos",
                  "atencion al cliente", "branding", "seo", "sem", "email marketing"]
    }
}

# ============================================
# VERBOS Y PREFIJOS (sin preposiciones forzadas)
# ============================================
prefijos = [
    "como aprender", "como dominar", "guia completa de", "tutorial de", "curso de",
    "dominar", "entender", "practicar", "resolver problemas de", "ejercicios de",
    "introduccion a", "conceptos basicos de", "manual de", "teoria de",
    "ejemplos de", "fundamentos de", "consejos para aprender", "recursos para estudiar",
    "clases de", "lecciones de", "como mejorar en", "como usar"
]

# ============================================
# SUFIJOS
# ============================================
sufijos = [
    "básico", "intermedio", "avanzado", "profesional", "completo",
    "fácil", "rápido", "para principiantes", "desde cero", "paso a paso",
    "con ejercicios", "online", "gratis", "certificado", "universitario",
    "para niños", "para adultos", "intensivo", "práctico", "teórico"
]

# ============================================
# PREGUNTAS
# ============================================
preguntas = [
    "qué es", "cómo funciona", "para qué sirve", "dónde aprender",
    "cuándo usar", "por qué es importante", "cuáles son los beneficios de",
    "cuánto tiempo se tarda en aprender", "qué necesito para estudiar"
]

# ============================================
# GENERACIÓN DE KEYWORDS
# ============================================
keywords = set()
total_temas = sum(len(cat["temas"]) + len(cat.get("temas_especiales", [])) for cat in temas.values())

print("🔄 Generando keywords...")

# 1. Combinaciones con prefijos (2000 - 3000 keywords)
for prefijo in prefijos:
    for cat_name, cat_data in temas.items():
        for tema in cat_data["temas"]:
            keywords.add(f"{prefijo} {tema}")
        for tema_esp in cat_data.get("temas_especiales", []):
            keywords.add(f"{prefijo} {tema_esp}")

# 2. Combinaciones con sufijos (1500 - 2000 keywords)
for sufijo in sufijos:
    for cat_data in temas.values():
        for tema in cat_data["temas"][:15]:
            keywords.add(f"{tema} {sufijo}")
        for tema_esp in cat_data.get("temas_especiales", []):
            keywords.add(f"{tema_esp} {sufijo}")

# 3. Preguntas (1000 - 1500 keywords)
for pregunta in preguntas:
    for cat_data in temas.values():
        for tema in cat_data["temas"][:15]:
            keywords.add(f"{pregunta} {tema}")
        for tema_esp in cat_data.get("temas_especiales", []):
            keywords.add(f"{pregunta} {tema_esp}")

# 4. Verbos + tema (800 - 1000 keywords)
verbos = ["aprender", "dominar", "practicar", "estudiar", "comprender", "aplicar"]
for verbo in verbos:
    for cat_data in temas.values():
        for tema in cat_data["temas"][:15]:
            keywords.add(f"{verbo} {tema}")

# 5. Comparativas inteligentes dentro de misma categoría (500 - 800 keywords)
for cat_data in temas.values():
    todos_temas = cat_data["temas"] + cat_data.get("temas_especiales", [])
    if len(todos_temas) >= 2:
        for _ in range(min(30, len(todos_temas) * 3)):
            tema1, tema2 = random.sample(todos_temas, 2)
            keywords.add(f"diferencia entre {tema1} y {tema2}")
            keywords.add(f"{tema1} vs {tema2}")
            keywords.add(f"comparacion {tema1} vs {tema2}")

# 6. Errores comunes (con artículo correcto)
for cat_data in temas.values():
    articulo = cat_data["articulo"]
    for tema in cat_data["temas"][:10]:
        keywords.add(f"errores comunes en {articulo} {tema}")
        keywords.add(f"como evitar errores en {tema}")
        keywords.add(f"solucion a problemas de {tema}")

# 7. Cursos y niveles (800 - 1000 keywords)
niveles = ["básico", "intermedio", "avanzado", "profesional", "intensivo"]
for nivel in niveles:
    for cat_data in temas.values():
        for tema in cat_data["temas"][:12]:
            keywords.add(f"curso {nivel} de {tema}")
            keywords.add(f"clases de {tema} nivel {nivel}")

# 8. Certificaciones y recursos (600 - 800 keywords)
for cat_data in temas.values():
    for tema in cat_data["temas"][:10]:
        keywords.add(f"certificacion en {tema}")
        keywords.add(f"examen de {tema}")
        keywords.add(f"libros de {tema}")
        keywords.add(f"videos de {tema}")

# 9. Tips y consejos (600 - 800 keywords)
for cat_data in temas.values():
    articulo = cat_data["articulo"]
    for tema in cat_data["temas"][:10]:
        keywords.add(f"tips para {articulo} {tema}")
        keywords.add(f"consejos para mejorar en {tema}")

# 10. Variaciones numéricas (para asegurar llegar a 10000)
for i in range(1, 2000):
    cat_name = random.choice(list(temas.keys()))
    tema = random.choice(temas[cat_name]["temas"])
    keywords.add(f"leccion {i} de {tema}")
    keywords.add(f"capitulo {i} de {tema}")
    keywords.add(f"unidad {i} de {tema}")

# ============================================
# LIMITAR A LA CANTIDAD DESEADA
# ============================================
keywords_lista = sorted(list(keywords))
random.shuffle(keywords_lista)

if len(keywords_lista) < CANTIDAD_KEYWORDS:
    print(f"⚠️ Solo se generaron {len(keywords_lista)} keywords. Repitiendo algunas para llegar a {CANTIDAD_KEYWORDS}...")
    while len(keywords_lista) < CANTIDAD_KEYWORDS:
        keywords_lista.extend(keywords_lista[:min(1000, CANTIDAD_KEYWORDS - len(keywords_lista))])

keywords_final = keywords_lista[:CANTIDAD_KEYWORDS]
random.shuffle(keywords_final)

# ============================================
# GUARDAR
# ============================================
with open('keywords/es.json', 'w', encoding='utf-8') as f:
    json.dump(keywords_final, f, indent=2, ensure_ascii=False)

# ============================================
# REPORTE
# ============================================
print(f"\n✅ Generadas {len(keywords_final)} keywords en español")
print(f"📁 Guardado en: keywords/es.json")
print(f"\n📊 Vista previa (primeras 30 keywords):")
for i, kw in enumerate(keywords_final[:30]):
    print(f"   {i+1}. {kw}")
