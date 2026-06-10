import os
import json
import random
import re
import time
import urllib.request
import concurrent.futures
from datetime import datetime
from modules.data_loader import config_loader
from modules.html_builder import generar_html_seo
from modules.frontend_builder import generar_frontend_impactante
from static_assets import crear_assets_estaticos
from content_generator import generar_contenido_estatico

# ============================================
# FALLBACK POOLS (cuando el Worker falla)
# ============================================
FALLBACK = {
    "es": [
        "Aprende {kw} de forma fácil con explicaciones paso a paso y ejemplos prácticos.",
        "Domina {kw} con nuestra IA educativa disponible 24/7.",
        "Resuelve tus dudas sobre {kw} al instante con Educare AI.",
    ],
    "en": [
        "Learn {kw} easily with step-by-step explanations and practical examples.",
        "Master {kw} with our educational AI available 24/7.",
        "Solve your questions about {kw} instantly with Educare AI.",
    ],
    "fr": [
        "Apprenez {kw} facilement avec des explications étape par étape.",
        "Maîtrisez {kw} avec notre IA éducative disponible 24h/24.",
        "Résolvez vos questions sur {kw} instantanément avec Educare AI.",
    ],
    "de": [
        "Lernen Sie {kw} einfach mit Schritt-für-Schritt-Erklärungen.",
        "Meistern Sie {kw} mit unserer KI rund um die Uhr.",
        "Lösen Sie Ihre Fragen zu {kw} sofort mit Educare AI.",
    ],
    "pt": [
        "Aprenda {kw} facilmente com explicações passo a passo.",
        "Domine {kw} com nossa IA educacional disponível 24h.",
        "Resolva suas dúvidas sobre {kw} instantaneamente com Educare AI.",
    ],
    "it": [
        "Impara {kw} facilmente con spiegazioni passo dopo passo.",
        "Padroneggia {kw} con la nostra IA educativa disponibile 24/7.",
        "Risolvi le tue domande su {kw} istantaneamente con Educare AI.",
    ],
}

WORKER_URL = "https://educare-gemini-api.stefanodelmoro7773.workers.dev"

# ============================================
# PROMPTS POR IDIOMA
# ============================================
PROMPTS = {
    "es": "Escribe 3 párrafos educativos sobre: {kw}. Párrafo 1: definición. Párrafo 2: importancia y conceptos clave. Párrafo 3: ejemplo práctico. Solo párrafos, sin listas numeradas ni headers. Máximo 200 palabras.",
    "en": "Explain in an educational, clear and useful way about: {kw}. Include: 1) brief definition, 2) why it is important to learn, 3) key concepts, 4) a practical example. Use paragraph format. Maximum 200 words.",
    "fr": "Expliquez de manière éducative, claire et utile: {kw}. Incluez: 1) définition brève, 2) pourquoi c'est important, 3) concepts clés, 4) exemple pratique. Format paragraphes. Maximum 200 mots.",
    "de": "Erkläre lehrreich, klar und nützlich: {kw}. Beinhalte: 1) kurze Definition, 2) warum wichtig, 3) Schlüsselkonzepte, 4) praktisches Beispiel. Absatzformat. Maximal 200 Wörter.",
    "pt": "Explique de forma educativa, clara e útil: {kw}. Inclua: 1) definição breve, 2) por que é importante, 3) conceitos-chave, 4) exemplo prático. Formato parágrafo. Máximo 200 palavras.",
    "it": "Spiega in modo educativo, chiaro e utile: {kw}. Includi: 1) breve definizione, 2) perché è importante, 3) concetti chiave, 4) esempio pratico. Formato paragrafi. Massimo 200 parole.",
    "ja": "{kw}について教育的にわかりやすく説明してください。定義、重要性、主要概念、実例を含めて200語以内で。",
    "zh": "请用教育性、清晰的方式解释：{kw}。包括定义、重要性、关键概念和实际例子。200字以内。",
    "ko": "{kw}에 대해 교육적으로 명확하게 설명해주세요. 정의, 중요성, 핵심개념, 실제예시 포함. 200단어 이내.",
    "ru": "Объясни образовательно и понятно: {kw}. Включи определение, важность, ключевые понятия, практический пример. Максимум 200 слов.",
    "ar": "اشرح بطريقة تعليمية وواضحة: {kw}. اشمل التعريف والأهمية والمفاهيم الرئيسية ومثال عملي. 200 كلمة كحد أقصى.",
    "hi": "{kw} ke baare mein educational aur clear tarike se explain karein. Definition, importance, key concepts, practical example. 200 words maximum.",
}

def _get_prompt(lang, kw):
    template = PROMPTS.get(lang, PROMPTS["en"])
    return template.replace("{kw}", kw)

def _get_fallback(lang, kw):
    pool = FALLBACK.get(lang, FALLBACK["en"])
    text = random.choice(pool).replace("{kw}", kw)
    return f"<p>{text}</p>"

def _convert_md_to_html(text):
    """Convierte markdown básico a HTML para el contenido estático."""
    text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*([^*]+)\*', r'<em>\1</em>', text)
    paras = [p.strip() for p in text.split('\n\n') if p.strip()]
    if len(paras) > 1:
        return ''.join(f'<p>{p.replace(chr(10), " ")}</p>' for p in paras)
    return f'<p>{text.replace(chr(10), " ")}</p>'

def llamar_worker(kw, lang, timeout=10):
    """Llama al Worker y retorna contenido HTML único. Thread-safe."""
    try:
        prompt  = _get_prompt(lang, kw)
        payload = json.dumps({"prompt": prompt, "lang": lang}).encode("utf-8")
        req     = urllib.request.Request(
            WORKER_URL,
            data=payload,
            headers={
                "Content-Type": "application/json",
                "User-Agent": "Mozilla/5.0 (compatible; EducareAI-Generator/4.0)"
            },
            method="POST"
        )
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            text = data.get("text", "").strip()
            if text and len(text) > 80:
                return _convert_md_to_html(text)
    except Exception:
        pass
    return None

def limpiar_nombre_archivo(texto):
    nombre = texto.replace(' ', '-')
    nombre = re.sub(r'[^\w\-]', '', nombre, flags=re.UNICODE)
    nombre = nombre[:80]
    nombre = re.sub(r'-+', '-', nombre)
    nombre = nombre.strip('-')
    if not nombre:
        nombre = f"pagina-{random.randint(1000,9999)}"
    return nombre

def cargar_categorias_por_idioma(lang):
    archivo = f'categories_{lang}.json'
    if os.path.exists(os.path.join('config', archivo)):
        return config_loader.load_json(archivo)
    return config_loader.load_json('categories.json')

def cargar_keywords_por_idioma():
    keywords = {}
    idiomas = [
        "es","en","fr","de","pt","it","ja","ko","zh","ru",
        "hi","ar","tr","nl","pl","vi","th","id","ur","fa",
        "sv","da","no","fi","el","cs","hu","ro","uk","he",
        "bn","ta","te","mr","kn","ms","tl","sr","hr","bg",
        "sk","sl","lt","lv","et","ka","az","kk","mn","ne"
    ]
    for lang in idiomas:
        archivo = f'config/keywords/{lang}.json'
        if os.path.exists(archivo):
            with open(archivo, 'r', encoding='utf-8') as f:
                keywords[lang] = json.load(f)
            print(f"   ✅ {lang}: {len(keywords[lang])} keywords")
        else:
            print(f"   ⚠ No encontrado {archivo}")
    return keywords

def generar_sitemaps_por_idioma(base_dir, urls_por_idioma):
    sitemaps_dir = os.path.join(base_dir, 'sitemaps')
    os.makedirs(sitemaps_dir, exist_ok=True)
    fecha    = datetime.now().strftime("%Y-%m-%d")
    base_url = "https://stef7773.github.io/EducareAI_Modular"
    sitemap_index = []
    for idioma, urls in urls_por_idioma.items():
        if not urls:
            continue
        sitemap_file = f"sitemap_{idioma}.xml"
        sitemap_path = os.path.join(sitemaps_dir, sitemap_file)
        with open(sitemap_path, 'w', encoding='utf-8') as f:
            f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
            f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
            for url in urls:
                f.write(f'  <url><loc>{url}</loc><lastmod>{fecha}</lastmod>'
                        f'<changefreq>weekly</changefreq><priority>0.8</priority></url>\n')
            f.write('</urlset>')
        sitemap_index.append(
            f'  <sitemap><loc>{base_url}/sitemaps/{sitemap_file}</loc>'
            f'<lastmod>{fecha}</lastmod></sitemap>'
        )
        print(f"   ✅ sitemap_{idioma}.xml: {len(urls)} URLs")
    with open(os.path.join(base_dir, 'sitemap_index.xml'), 'w', encoding='utf-8') as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        f.write('\n'.join(sitemap_index))
        f.write('\n</sitemapindex>')
    with open(os.path.join(base_dir, 'robots.txt'), 'w', encoding='utf-8') as f:
        f.write(f'User-agent: *\nAllow: /\nSitemap: {base_url}/sitemap_index.xml\nCrawl-delay: 1\n')
    print(f"   ✅ sitemap_index.xml y robots.txt generados")

def main():
    print("\n🚀 EDUCARE AI v6.0 — 166k paginas CSS/JS externos")
    print("=" * 60)

    estrategia = cargar_keywords_por_idioma()
    if not estrategia:
        print("❌ No se encontraron keywords")
        return

    # ── Configuración ──
    MAX_KW_POR_IDIOMA = 2300   # Páginas por idioma
    MAX_WORKERS       = 10    # Hilos paralelos
    USE_AI            = False  # Desactivado — usamos generador estático

    base_dir = os.path.join(os.getcwd(), 'docs')
    os.makedirs(base_dir, exist_ok=True)
    print("Creando assets estaticos...")
    crear_assets_estaticos(base_dir)

    urls_por_idioma = {lang: [] for lang in estrategia.keys()}
    total = 0
    ai_ok = 0
    ai_fail = 0

    print(f"\n📊 Idiomas: {len(estrategia)}")
    print(f"📄 Páginas por idioma: {MAX_KW_POR_IDIOMA}")
    print(f"⚡ Hilos paralelos: {MAX_WORKERS}")
    print(f"🤖 IA activada: {USE_AI}")
    print(f"📊 Total estimado: {len(estrategia) * MAX_KW_POR_IDIOMA} páginas\n")

    for lang, keywords in estrategia.items():
        keywords = keywords[:MAX_KW_POR_IDIOMA]
        print(f"\n📝 {lang.upper()} — {len(keywords)} keywords...")

        categorias = cargar_categorias_por_idioma(lang)
        lang_dir   = os.path.join(base_dir, lang)
        os.makedirs(lang_dir, exist_ok=True)
        for cat in categorias.keys():
            os.makedirs(os.path.join(lang_dir, cat), exist_ok=True)
        os.makedirs(os.path.join(lang_dir, "general"), exist_ok=True)

        # ── Preparar lista de tareas ──
        tareas = []
        for idx, kw in enumerate(keywords):
            categoria = "general"
            kw_lower  = kw.lower()
            for cat, subcats in categorias.items():
                for sub in subcats[:5]:
                    if sub.lower() in kw_lower:
                        categoria = cat
                        break
                if categoria != "general":
                    break
            nombre = limpiar_nombre_archivo(kw)
            tareas.append((idx, kw, categoria, nombre))

        # ── Generación estática sin API ──
        contenidos = {}
        for idx, kw, categoria, nombre in tareas:
            contenido = generar_contenido_estatico(kw, categoria, lang)
            contenidos[(idx, kw)] = (categoria, nombre, contenido)

        # ── Escribir HTMLs ──
        for idx, kw, categoria, nombre in tareas:
            _, _, content = contenidos.get((idx, kw), (categoria, nombre, None))

            if content:
                ai_ok += 1
                contenido_final = content
            else:
                ai_fail += 1
                contenido_final = _get_fallback(lang, kw)

            ruta = os.path.join(lang_dir, categoria, f"{nombre}.html")
            html = generar_html_seo(
                kw, lang, idx,
                depth=2 if lang != 'es' else 1,
                contenido_dinamico=contenido_final,
                categoria=categoria,
                nombre=nombre
            )
            with open(ruta, 'w', encoding='utf-8') as f:
                f.write(html)

            url = f"https://stef7773.github.io/EducareAI_Modular/{lang}/{categoria}/{nombre}.html"
            urls_por_idioma[lang].append(url)
            total += 1

        print(f"   ✅ {lang.upper()}: {len(tareas)} páginas | IA: {ai_ok} | Fallback: {ai_fail}")

    print("\n📁 Generando sitemaps...")
    generar_sitemaps_por_idioma(base_dir, urls_por_idioma)

    print("\n🎨 Generando landings principales...")
    generar_frontend_impactante(base_dir)

    print("\n" + "=" * 60)
    print(f"✅ COMPLETADO!")
    print(f"📊 TOTAL PÁGINAS: {total}")
    print(f"🤖 Con contenido IA único: {ai_ok}")
    print(f"⚠  Con fallback: {ai_fail}")
    print(f"🌍 https://stef7773.github.io/EducareAI_Modular/")
    print("=" * 60)

if __name__ == "__main__":
    main()
