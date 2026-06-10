import random, sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# UI texts per language
UI_TEXTS = {
    'es':{'ph':'Escribe tu pregunta...','btn':'Preguntar','stop':'Detener','copy':'Copiar','copied':'Copiado','thinking':'Pensando','error':'Error de conexion.','alert':'Escribe una pregunta primero','ai_title':'Pregunta a la IA','initial_msg':'Escribe una pregunta para obtener una explicacion personalizada.'},
    'en':{'ph':'Write your question...','btn':'Ask','stop':'Stop','copy':'Copy','copied':'Copied','thinking':'Thinking','error':'Connection error.','alert':'Write a question first','ai_title':'Ask the AI','initial_msg':'Write a question to get a personalized explanation.'},
    'fr':{'ph':'Ecrivez votre question...','btn':'Demander','stop':'Arreter','copy':'Copier','copied':'Copie','thinking':'Reflexion','error':'Erreur de connexion.','alert':'Ecrivez une question','ai_title':'Demandez a l IA','initial_msg':'Ecrivez une question pour obtenir une explication personnalisee.'},
    'de':{'ph':'Schreiben Sie Ihre Frage...','btn':'Fragen','stop':'Stoppen','copy':'Kopieren','copied':'Kopiert','thinking':'Denke nach','error':'Verbindungsfehler.','alert':'Schreiben Sie eine Frage','ai_title':'Fragen Sie die KI','initial_msg':'Schreiben Sie eine Frage fuer eine Erklaerung.'},
    'it':{'ph':'Scrivi la tua domanda...','btn':'Chiedi','stop':'Ferma','copy':'Copia','copied':'Copiato','thinking':'Sto pensando','error':'Errore di connessione.','alert':'Scrivi una domanda','ai_title':'Chiedi alla IA','initial_msg':'Scrivi una domanda per una spiegazione personalizzata.'},
    'pt':{'ph':'Escreva sua pergunta...','btn':'Perguntar','stop':'Parar','copy':'Copiar','copied':'Copiado','thinking':'Pensando','error':'Erro de conexao.','alert':'Escreva uma pergunta','ai_title':'Pergunte a IA','initial_msg':'Escreva uma pergunta para uma explicacao personalizada.'},
    'ja':{'ph':'質問を書いてください...','btn':'質問する','stop':'停止','copy':'コピー','copied':'コピー済み','thinking':'考え中','error':'接続エラー。','alert':'質問を書いてください','ai_title':'AIに質問する','initial_msg':'質問を書いてください。'},
    'zh':{'ph':'写下你的问题...','btn':'提问','stop':'停止','copy':'复制','copied':'已复制','thinking':'思考中','error':'连接错误。','alert':'请先写一个问题','ai_title':'向AI提问','initial_msg':'写下问题获取个性化解释。'},
    'ko':{'ph':'질문을 작성하세요...','btn':'질문하기','stop':'중지','copy':'복사','copied':'복사됨','thinking':'생각 중','error':'연결 오류.','alert':'질문을 작성하세요','ai_title':'AI에게 질문하기','initial_msg':'질문을 작성하세요.'},
    'ru':{'ph':'Napishite vopros...','btn':'Sprosit','stop':'Ostanovit','copy':'Kopirovat','copied':'Skopirovano','thinking':'Dumayu','error':'Oshibka soedineniya.','alert':'Napishite vopros','ai_title':'Sprosit II','initial_msg':'Napishite vopros dlya obyasneniya.'},
    'ar':{'ph':'اكتب سؤالك...','btn':'اسأل','stop':'ايقاف','copy':'نسخ','copied':'تم النسخ','thinking':'جاري التفكير','error':'خطأ في الاتصال.','alert':'اكتب سؤالا','ai_title':'اسأل الذكاء الاصطناعي','initial_msg':'اكتب سؤالا للحصول على شرح.'},
    'hi':{'ph':'apna prashn likhen...','btn':'Puchhen','stop':'Rokein','copy':'Copy','copied':'Copied','thinking':'Soch raha hun','error':'Connection error.','alert':'Pehle prashn likhen','ai_title':'AI se Puchhen','initial_msg':'Prashn likhen.'},
    'tr':{'ph':'Sorunuzu yazin...','btn':'Sor','stop':'Durdur','copy':'Kopyala','copied':'Kopyalandi','thinking':'Dusunuyor','error':'Baglanti hatasi.','alert':'Bir soru yazin','ai_title':'Yapay Zekaya Sor','initial_msg':'Soru yazin.'},
    'nl':{'ph':'Schrijf uw vraag...','btn':'Vragen','stop':'Stoppen','copy':'Kopieren','copied':'Gekopieerd','thinking':'Denken','error':'Verbindingsfout.','alert':'Schrijf een vraag','ai_title':'Vraag de AI','initial_msg':'Schrijf een vraag.'},
    'pl':{'ph':'Napisz pytanie...','btn':'Zapytaj','stop':'Zatrzymaj','copy':'Kopiuj','copied':'Skopiowano','thinking':'Myslenie','error':'Blad polaczenia.','alert':'Napisz pytanie','ai_title':'Zapytaj AI','initial_msg':'Napisz pytanie.'},
    'sv':{'ph':'Skriv din fraga...','btn':'Fraga','stop':'Stoppa','copy':'Kopiera','copied':'Kopierat','thinking':'Tanker','error':'Anslutningsfel.','alert':'Skriv en fraga','ai_title':'Fraga AI','initial_msg':'Skriv en fraga.'},
    'vi':{'ph':'Viet cau hoi...','btn':'Hoi','stop':'Dung','copy':'Sao chep','copied':'Da sao chep','thinking':'Dang suy nghi','error':'Loi ket noi.','alert':'Viet cau hoi','ai_title':'Hoi AI','initial_msg':'Viet cau hoi.'},
    'uk':{'ph':'Napishit zapytannya...','btn':'Zapytaty','stop':'Zupynyty','copy':'Skopiyuvaty','copied':'Skopiyovano','thinking':'Dumayu','error':'Pomylka zvyazku.','alert':'Napishit zapytannya','ai_title':'Zapytaty II','initial_msg':'Napishit zapytannya.'},
}
DEFAULT_UI = UI_TEXTS['en']

OG_IMAGE  = "https://stef7773.github.io/EducareAI_Modular/static/images/logo-nuevo.png"
WORKER    = "https://educare-gemini-api.stefanodelmoro7773.workers.dev"
BASE_STATIC = "https://stef7773.github.io/EducareAI_Modular/static"

def _ui(lang):
    return UI_TEXTS.get(lang, DEFAULT_UI)

def generar_html_seo(tema, lang, idx, depth=1, contenido_dinamico=None, categoria="general", nombre=""):
    from modules.data_loader import config_loader
    textos    = config_loader.load_json('texts.json')
    stats_lbl = config_loader.load_json('stats_labels.json')
    tl        = textos.get(lang, textos['en'])
    labels    = stats_lbl.get(lang, stats_lbl['en'])

    h1      = random.choice(tl["h1_variations"]).replace("{tema}", tema)
    desc    = tl["desc"].replace("{tema}", tema)
    benefit = contenido_dinamico if contenido_dinamico else f"<p>{tema}</p>"
    feats   = " &nbsp;·&nbsp; ".join(random.sample(tl["features"], 4))
    cta     = random.choice(tl["cta_urgency"])
    subtext = random.choice(tl["subtexts"])
    canonical = f"https://stef7773.github.io/EducareAI_Modular/{lang}/{categoria}/{nombre}.html"
    ui      = _ui(lang)

    # Partículas mínimas (solo 8 para ahorrar bytes)
    pdots = "".join([
        f'<div class="pd" style="top:{random.randint(2,95)}%;left:{random.randint(2,95)}%;'
        f'width:{random.randint(3,6)}px;height:{random.randint(3,6)}px;'
        f'animation-duration:{random.randint(2,5)}s;animation-delay:{round(random.uniform(0,4),1)}s"></div>'
        for _ in range(8)
    ])

    # JSON para UI (pasado al JS externo)
    import json
    ui_json = json.dumps(ui, ensure_ascii=False)

    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="{desc[:200]}">
<meta name="robots" content="index,follow">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{tema} | Educare AI">
<meta property="og:description" content="{desc[:200]}">
<meta property="og:image" content="{OG_IMAGE}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:url" content="{canonical}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Educare AI">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{OG_IMAGE}">
<title>{tema} | Educare AI</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Fira+Code:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{BASE_STATIC}/edu.css">
<script>window.EDUCARE_WORKER='{WORKER}';window.EDUCARE_LANG='{lang}';window.EDUCARE_UI={ui_json};</script>
</head>
<body>
<div class="grid"></div>
{pdots}
<div class="card">
<div class="badge"><span class="live"></span>Educare AI · Gemini</div>
<div class="rw">
<div class="ring ring1"></div><div class="ring ring2"></div><div class="ring ring3"></div>
<span class="ri">🤖</span>
</div>
<div class="brand">Educare AI</div>
<h1>{h1}</h1>
<p class="desc">{desc}</p>
<div class="benefit-block">{benefit}</div>
<div class="ai-section">
<div class="ai-head">
<div class="ai-label"><span class="ai-led"></span><span id="ai-title-text">{ui["ai_title"]}</span></div>
<div class="ai-ctrls">
<button id="stop-btn" class="ctrl-btn stop-btn" onclick="stopAIGeneration()">⏹ {ui["stop"]}</button>
<button id="copy-btn" class="ctrl-btn copy-btn" onclick="copyAIResponse()">📋 {ui["copy"]}</button>
</div>
</div>
<div id="ai-content"><span class="initial-hint">💡 {ui["initial_msg"]}</span></div>
<div class="input-row">
<input type="text" id="userInput" placeholder="{ui["ph"]}">
<button id="ask-btn" class="ask-btn" onclick="handleUserQuestion()">✦ {ui["btn"]}</button>
</div>
</div>
<div class="stats">
<div class="stat"><div class="stat-n">1M+</div><div class="stat-l">{labels["students"]}</div></div>
<div class="stat"><div class="stat-n">4.8</div><div class="stat-l">⭐ {labels["rating"]}</div></div>
<div class="stat"><div class="stat-n">98%</div><div class="stat-l">{labels["accuracy"]}</div></div>
</div>
<div class="feats">{feats}</div>
<a href="https://play.google.com/store/apps/details?id=com.educareai.app" class="cta-link">▶ {tl["btn"]}</a>
<p class="subtext">{subtext}</p>
<div class="urgency">{cta}</div>
<p class="footer">© 2026 Educare AI — {tema}</p>
</div>
<script src="{BASE_STATIC}/edu.js"></script>
</body>
</html>'''
