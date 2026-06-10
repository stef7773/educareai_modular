import os, json, random, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from shared_js import get_landing_js, get_shared_css

OG_IMAGE  = "https://stef7773.github.io/EducareAI_Modular/static/images/logo-nuevo.png"
WORKER    = "https://educare-gemini-api.stefanodelmoro7773.workers.dev"
BASE_URL  = "https://stef7773.github.io/EducareAI_Modular"
LANGS_BADGE = "ES · EN · FR · DE · IT · PT · JA · KO · ZH · RU · AR · HI · NL · PL · TR · SV · VI · UK · +32"

UI = {
    'es':{'ph':'Escribe tu pregunta aqui...','btn':'Preguntar','stop':'Detener','copy':'Copiar','copied':'Copiado','thinking':'Pensando','error':'Error de conexion.','alert':'Escribe una pregunta primero','initial':'Hola! Soy Educare AI. Escribe tu pregunta para empezar.','chat_title':'Pregunta a Educare AI'},
    'en':{'ph':'Write your question here...','btn':'Ask','stop':'Stop','copy':'Copy','copied':'Copied','thinking':'Thinking','error':'Connection error.','alert':'Write a question first','initial':'Hello! I am Educare AI. Write your question to get started.','chat_title':'Ask Educare AI'},
    'fr':{'ph':'Ecrivez votre question ici...','btn':'Demander','stop':'Arreter','copy':'Copier','copied':'Copie','thinking':'Reflexion','error':'Erreur de connexion.','alert':'Ecrivez une question maintenant','initial':'Bonjour! Je suis Educare AI. Ecrivez votre question pour commencer.','chat_title':'Demandez a Educare AI'},
    'de':{'ph':'Schreiben Sie Ihre Frage hier...','btn':'Fragen','stop':'Stoppen','copy':'Kopieren','copied':'Kopiert','thinking':'Denke nach','error':'Verbindungsfehler.','alert':'Schreiben Sie zuerst eine Frage','initial':'Hallo! Ich bin Educare AI. Schreiben Sie Ihre Frage.','chat_title':'Fragen Sie Educare AI'},
    'it':{'ph':'Scrivi la tua domanda qui...','btn':'Chiedi','stop':'Ferma','copy':'Copia','copied':'Copiato','thinking':'Sto pensando','error':'Errore di connessione.','alert':'Scrivi prima una domanda','initial':'Ciao! Sono Educare AI. Scrivi la tua domanda per iniziare.','chat_title':'Chiedi a Educare AI'},
    'pt':{'ph':'Escreva sua pergunta aqui...','btn':'Perguntar','stop':'Parar','copy':'Copiar','copied':'Copiado','thinking':'Pensando','error':'Erro de conexao.','alert':'Escreva uma pergunta primeiro','initial':'Ola! Sou Educare AI. Escreva sua pergunta para comecar.','chat_title':'Pergunte a Educare AI'},
    'ja':{'ph':'ここに質問を書いてください...','btn':'質問する','stop':'停止','copy':'コピー','copied':'コピー済み','thinking':'考え中','error':'接続エラー。','alert':'まず質問を書いてください','initial':'こんにちは！Educare AIです。質問を書いてください。','chat_title':'Educare AIに質問する'},
    'zh':{'ph':'在这里写下你的问题...','btn':'提问','stop':'停止','copy':'复制','copied':'已复制','thinking':'思考中','error':'连接错误。','alert':'请先写一个问题','initial':'你好！我是Educare AI。写下你的问题开始吧。','chat_title':'向Educare AI提问'},
    'ru':{'ph':'Napishite vopros zdes...','btn':'Sprosit','stop':'Ostanovit','copy':'Kopirovat','copied':'Skopirovano','thinking':'Dumayu','error':'Oshibka soedineniya.','alert':'Snachala napishite vopros','initial':'Privet! Ya Educare AI. Napishite vopros.','chat_title':'Sprosit Educare AI'},
    'ar':{'ph':'اكتب سؤالك هنا...','btn':'اسأل','stop':'ايقاف','copy':'نسخ','copied':'تم النسخ','thinking':'جاري التفكير','error':'خطأ في الاتصال.','alert':'اكتب سؤالا اولا','initial':'مرحبا! انا Educare AI. اكتب سؤالك للبدء.','chat_title':'اسأل Educare AI'},
    'hi':{'ph':'apna prashn yahan likhen...','btn':'Puchhen','stop':'Rokein','copy':'Copy','copied':'Copied','thinking':'Soch raha hun','error':'Connection error.','alert':'Pehle ek prashn likhen','initial':'Namaste! Main Educare AI hun. Apna prashn likhen.','chat_title':'Educare AI se Puchhen'},
    'ko':{'ph':'질문을 여기에 작성하세요...','btn':'질문하기','stop':'중지','copy':'복사','copied':'복사됨','thinking':'생각 중','error':'연결 오류.','alert':'먼저 질문을 작성하세요','initial':'안녕하세요! Educare AI입니다. 질문을 작성하세요.','chat_title':'Educare AI에게 질문하기'},
    'tr':{'ph':'Sorunuzu buraya yazin...','btn':'Sor','stop':'Durdur','copy':'Kopyala','copied':'Kopyalandi','thinking':'Dusunuyor','error':'Baglanti hatasi.','alert':'Once bir soru yazin','initial':'Merhaba! Ben Educare AI. Sorunuzu yazin.','chat_title':'Educare AI ya Sor'},
    'nl':{'ph':'Schrijf uw vraag hier...','btn':'Vragen','stop':'Stoppen','copy':'Kopieren','copied':'Gekopieerd','thinking':'Denken','error':'Verbindingsfout.','alert':'Schrijf eerst een vraag','initial':'Hallo! Ik ben Educare AI. Schrijf uw vraag.','chat_title':'Vraag Educare AI'},
    'pl':{'ph':'Napisz swoje pytanie tutaj...','btn':'Zapytaj','stop':'Zatrzymaj','copy':'Kopiuj','copied':'Skopiowano','thinking':'Myslenie','error':'Blad polaczenia.','alert':'Najpierw napisz pytanie','initial':'Czesc! Jestem Educare AI. Napisz swoje pytanie.','chat_title':'Zapytaj Educare AI'},
    'sv':{'ph':'Skriv din fraga har...','btn':'Fraga','stop':'Stoppa','copy':'Kopiera','copied':'Kopierat','thinking':'Tanker','error':'Anslutningsfel.','alert':'Skriv en fraga forst','initial':'Hej! Jag ar Educare AI. Skriv din fraga.','chat_title':'Fraga Educare AI'},
    'vi':{'ph':'Viet cau hoi cua ban o day...','btn':'Hoi','stop':'Dung','copy':'Sao chep','copied':'Da sao chep','thinking':'Dang suy nghi','error':'Loi ket noi.','alert':'Viet cau hoi truoc','initial':'Xin chao! Toi la Educare AI. Hay viet cau hoi.','chat_title':'Hoi Educare AI'},
    'uk':{'ph':'Napishit vashe zapytannya tut...','btn':'Zapytaty','stop':'Zupynyty','copy':'Skopiyuvaty','copied':'Skopiyovano','thinking':'Dumayu','error':'Pomylka zvyazku.','alert':'Spochatku napishit zapytannya','initial':'Pryvit! Ya Educare AI. Napishit zapytannya.','chat_title':'Zapytaty Educare AI'},
}

LANDING_CSS = """
<style>
*,*::before,*::after{margin:0;padding:0;box-sizing:border-box}
:root{
    --b1:#1d4ed8;--b2:#2563eb;--b3:#3b82f6;--b4:#60a5fa;--b5:#93c5fd;
    --glow:rgba(37,99,235,.4);
    --bg:#050c18;--bg2:#080f1e;--card:rgba(5,12,24,.9);
    --border:rgba(37,99,235,.18);--text:#e2e8f0;--muted:#475569;
}
html{scroll-behavior:smooth}
body{font-family:'Montserrat','Inter',sans-serif;background:linear-gradient(140deg,var(--bg) 0%,var(--bg2) 60%,#060e1c 100%);color:var(--text);min-height:100vh;display:flex;align-items:center;justify-content:center;position:relative;overflow-x:hidden}
body::before{content:'';position:fixed;inset:0;background:radial-gradient(ellipse 80% 55% at 10% 15%,rgba(29,78,216,.09) 0%,transparent 55%),radial-gradient(ellipse 70% 45% at 90% 85%,rgba(96,165,250,.06) 0%,transparent 55%);pointer-events:none;z-index:0}
.grid{position:fixed;inset:0;background-image:linear-gradient(rgba(37,99,235,.022) 1px,transparent 1px),linear-gradient(90deg,rgba(37,99,235,.022) 1px,transparent 1px);background-size:56px 56px;pointer-events:none;z-index:0}
.particle{position:fixed;border-radius:50%;pointer-events:none;z-index:0}
.pd{background:var(--b4);opacity:0;animation:tw linear infinite}
@keyframes tw{0%,100%{opacity:0;transform:scale(.4)}50%{opacity:.6;transform:scale(1.2)}}
.pg{background:radial-gradient(circle,rgba(37,99,235,.18) 0%,transparent 70%);filter:blur(1px);animation:gf 20s ease-in-out infinite alternate}
@keyframes gf{0%{transform:translate(0,0)}100%{transform:translate(50px,-65px) scale(1.1)}}

.container{position:relative;z-index:1;max-width:1080px;margin:0 auto;padding:48px 24px;text-align:center}

/* Top badge */
.top-badge{display:inline-flex;align-items:center;gap:8px;background:rgba(37,99,235,.09);border:1px solid rgba(37,99,235,.25);padding:5px 18px;border-radius:50px;font-size:.7rem;color:var(--b4);letter-spacing:1.5px;text-transform:uppercase;font-weight:700;margin-bottom:22px}
.live-dot{width:6px;height:6px;background:#22c55e;border-radius:50%;box-shadow:0 0 8px #22c55e;animation:blink 1.5s ease-in-out infinite}
@keyframes blink{0%,100%{opacity:1}50%{opacity:.15}}

/* Robot */
.robot-wrap{position:relative;display:inline-block;margin:4px auto 18px}
.robot-icon{font-size:clamp(62px,9vw,90px);display:block;position:relative;z-index:1;animation:bob 4s ease-in-out infinite;filter:drop-shadow(0 0 26px rgba(37,99,235,.65))}
@keyframes bob{0%,100%{transform:translateY(0) rotate(0deg)}33%{transform:translateY(-11px) rotate(2deg)}66%{transform:translateY(-5px) rotate(-1deg)}}
.ring{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);border-radius:50%;border:1px solid rgba(37,99,235,.22);animation:rp 2.5s ease-out infinite}
.r1{width:108px;height:108px}.r2{width:152px;height:152px;animation-delay:.7s;border-color:rgba(96,165,250,.15)}.r3{width:196px;height:196px;animation-delay:1.4s;border-color:rgba(59,130,246,.08)}
@keyframes rp{0%{transform:translate(-50%,-50%) scale(.88);opacity:.55}100%{transform:translate(-50%,-50%) scale(1.07);opacity:.06}}

/* Title */
.main-title{font-size:clamp(2.4rem,6.5vw,5rem);font-weight:900;background:linear-gradient(120deg,var(--b4) 0%,#38bdf8 20%,var(--b3) 45%,var(--b5) 70%,var(--b4) 100%);background-size:250% auto;-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;letter-spacing:-3px;line-height:1;animation:neon 4s linear infinite;margin:6px 0 8px;filter:drop-shadow(0 0 14px rgba(37,99,235,.4))}
@keyframes neon{0%{background-position:0% center;filter:drop-shadow(0 0 8px rgba(37,99,235,.3))}50%{background-position:100% center;filter:drop-shadow(0 0 20px rgba(96,165,250,.8))}100%{background-position:200% center;filter:drop-shadow(0 0 8px rgba(37,99,235,.3))}}

.slogan{font-size:clamp(.98rem,2.3vw,1.4rem);color:rgba(255,255,255,.76);line-height:1.55;margin:8px 0 14px;font-weight:400}
.lang-badge{background:rgba(255,255,255,.035);border:1px solid rgba(255,255,255,.07);padding:9px 20px;border-radius:50px;display:inline-block;margin:10px 0 28px;font-size:.7rem;color:rgba(255,255,255,.38);line-height:1.7;max-width:680px}

/* Chat card */
.chat-card{background:var(--card);backdrop-filter:blur(24px);-webkit-backdrop-filter:blur(24px);border-radius:22px;padding:24px 28px;margin:0 0 26px;border:1px solid var(--border);text-align:left;box-shadow:0 0 0 1px rgba(37,99,235,.06),0 26px 60px rgba(0,0,0,.6),inset 0 1px 0 rgba(255,255,255,.03);position:relative;overflow:hidden}
.chat-card::before{content:'';position:absolute;top:0;left:10%;right:10%;height:1px;background:linear-gradient(90deg,transparent,rgba(37,99,235,.42),transparent)}
.chat-head{display:flex;align-items:center;justify-content:space-between;margin-bottom:14px;flex-wrap:wrap;gap:8px}
.chat-label{display:flex;align-items:center;gap:8px;font-size:.75rem;font-weight:700;color:var(--b4);letter-spacing:.8px;text-transform:uppercase}
.ctdot{width:8px;height:8px;background:var(--b3);border-radius:50%;box-shadow:0 0 8px var(--b3);animation:blink 1.5s ease-in-out infinite}
.ai-ctrls{display:flex;gap:7px}
.ctrl{display:inline-flex;align-items:center;gap:5px;padding:4px 11px;border-radius:50px;border:1px solid rgba(37,99,235,.22);background:rgba(37,99,235,.07);color:var(--b4);font-size:.7rem;font-weight:600;cursor:pointer;font-family:inherit;white-space:nowrap;transition:all .2s}
.ctrl:hover{background:rgba(37,99,235,.15);border-color:rgba(59,130,246,.44)}
.ctrl.stop{border-color:rgba(239,68,68,.26);background:rgba(239,68,68,.06);color:#f87171;display:none}
.ctrl.stop:hover{background:rgba(239,68,68,.14)}
.ctrl.copy{display:none}

#ai-response{min-height:68px;color:var(--text);font-size:.9rem;line-height:1.8;margin-bottom:14px;word-wrap:break-word}

/* Input */
.input-group{display:flex;gap:10px;flex-wrap:wrap}
#userInput{flex:1;min-width:160px;padding:12px 20px;border-radius:50px;border:1px solid rgba(37,99,235,.2);background:rgba(255,255,255,.04);color:white;font-size:.9rem;font-family:inherit;outline:none;transition:border-color .25s,background .25s,box-shadow .25s}
#userInput::placeholder{color:rgba(255,255,255,.26)}
#userInput:focus{border-color:var(--b3);background:rgba(37,99,235,.06);box-shadow:0 0 0 3px rgba(37,99,235,.11)}
.ask-btn{display:inline-flex;align-items:center;gap:7px;padding:12px 26px;border-radius:50px;border:none;background:linear-gradient(135deg,var(--b1),var(--b3));color:white;cursor:pointer;font-weight:700;font-size:.9rem;font-family:inherit;transition:opacity .2s,box-shadow .2s,transform .1s;white-space:nowrap}
.ask-btn:hover{opacity:.88;box-shadow:0 8px 26px var(--glow)}
.ask-btn:active{transform:scale(.97)}
.ask-btn:disabled{opacity:.5;cursor:not-allowed}

/* Stats */
.stats{display:flex;justify-content:center;gap:12px;margin:0 0 26px;flex-wrap:wrap}
.stat{background:var(--card);backdrop-filter:blur(12px);padding:17px 22px;border-radius:18px;min-width:108px;border:1px solid var(--border);transition:border-color .25s,transform .25s}
.stat:hover{border-color:rgba(59,130,246,.38);transform:translateY(-5px)}
.stat-n{font-size:clamp(1.7rem,3.8vw,2.7rem);font-weight:900;background:linear-gradient(135deg,var(--b3),var(--b4));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;line-height:1}
.stat-l{font-size:.65rem;color:var(--muted);text-transform:uppercase;letter-spacing:1.5px;margin-top:5px}

/* Features */
.features-grid{display:flex;justify-content:center;gap:11px;margin:0 0 26px;flex-wrap:wrap}
.feat{background:var(--card);backdrop-filter:blur(12px);padding:15px 17px;border-radius:15px;min-width:125px;border:1px solid rgba(37,99,235,.11);font-size:.8rem;color:#94a3b8;line-height:1.55;transition:border-color .25s,background .25s,transform .25s;text-align:center}
.feat:hover{border-color:rgba(37,99,235,.28);background:rgba(37,99,235,.06);transform:translateY(-3px)}
.feat-icon{font-size:1.4rem;display:block;margin-bottom:6px}

/* Download CTA */
.download-btn{display:inline-flex;align-items:center;gap:10px;background:linear-gradient(135deg,var(--b1),var(--b3));color:white;padding:17px 52px;border-radius:80px;text-decoration:none;font-weight:800;font-size:clamp(.92rem,2.3vw,1.4rem);transition:opacity .2s,box-shadow .2s;box-shadow:0 15px 38px var(--glow);position:relative;overflow:hidden;animation:pulse 3s ease-in-out infinite}
.download-btn:hover{opacity:.9;box-shadow:0 20px 48px var(--glow);animation:none}
@keyframes pulse{0%,100%{box-shadow:0 15px 38px var(--glow)}50%{box-shadow:0 15px 38px rgba(37,99,235,.7),0 0 50px rgba(37,99,235,.2)}}

.btn-sub{color:rgba(255,255,255,.36);font-size:.8rem;margin-top:10px}
.footer{margin-top:40px;padding-top:15px;border-top:1px solid rgba(37,99,235,.07);font-size:.7rem;color:#1e293b}

@media(max-width:768px){.container{padding:30px 14px}.chat-card{padding:18px 15px}.input-group{flex-direction:column}.ask-btn{width:100%;justify-content:center}.stats{gap:10px}.stat{padding:13px 15px;min-width:86px}.feat{padding:12px 13px;min-width:108px}.download-btn{font-size:.95rem;padding:14px 30px}.r1,.r2,.r3{display:none}.chat-head{flex-direction:column;align-items:flex-start}}
</style>"""


def generar_frontend_impactante(base_dir):
    with open('config/frontend_texts.json', 'r', encoding='utf-8') as f:
        textos = json.load(f)

    js_block     = get_landing_js(WORKER)
    shared_css   = get_shared_css()

    for lang, t in textos.items():
        ui  = UI.get(lang, UI['en'])
        can = f"{BASE_URL}/index.html" if lang == 'es' else f"{BASE_URL}/{lang}/index.html"

        pdots = "".join([
            f'<div class="particle pd" style="top:{random.randint(2,95)}%;left:{random.randint(2,95)}%;'
            f'width:{random.randint(3,6)}px;height:{random.randint(3,6)}px;'
            f'animation-duration:{random.randint(2,5)}s;animation-delay:{round(random.uniform(0,4),1)}s"></div>'
            for _ in range(18)
        ])
        pglows = "".join([
            f'<div class="particle pg" style="top:{random.randint(5,80)}%;left:{random.randint(2,85)}%;'
            f'width:{random.randint(140,250)}px;height:{random.randint(140,250)}px;'
            f'animation-delay:{random.randint(0,12)}s"></div>'
            for _ in range(4)
        ])

        html = f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width,initial-scale=1.0,user-scalable=yes">
    <title>{t["title"]}</title>
    <meta name="description" content="{t["description"]}">
    <link rel="canonical" href="{can}">
    <meta property="og:title" content="{t["title"]}">
    <meta property="og:description" content="{t["description"]}">
    <meta property="og:image" content="{OG_IMAGE}">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta property="og:type" content="website">
    <meta property="og:url" content="{can}">
    <meta property="og:site_name" content="Educare AI">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{t["title"]}">
    <meta name="twitter:description" content="{t["description"]}">
    <meta name="twitter:image" content="{OG_IMAGE}">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800;900&family=Fira+Code:wght@400;500&display=swap" rel="stylesheet">
    {LANDING_CSS}
    {shared_css}
</head>
<body>
    <div class="grid"></div>
    {pdots}{pglows}
    <div class="container">
        <div class="top-badge"><span class="live-dot"></span>Educare AI &nbsp;·&nbsp; Powered by Gemini</div>
        <div class="robot-wrap">
            <div class="ring r1"></div><div class="ring r2"></div><div class="ring r3"></div>
            <span class="robot-icon">🤖</span>
        </div>
        <div class="main-title">Educare AI</div>
        <div class="slogan">{t["slogan"]}</div>
        <div class="lang-badge">🌍 {t["badge"]} &nbsp;—&nbsp; {LANGS_BADGE}</div>
        <div class="chat-card">
            <div class="chat-head">
                <div class="chat-label"><span class="ctdot"></span>{ui["chat_title"]}</div>
                <div class="ai-ctrls">
                    <button id="stop-btn" class="ctrl stop" onclick="stopGen()">⏹ {ui["stop"]}</button>
                    <button id="copy-btn" class="ctrl copy" onclick="copyResp('{ui["copied"]}')" >📋 {ui["copy"]}</button>
                </div>
            </div>
            <div id="ai-response"><span class="initial-hint">💡 {ui["initial"]}</span></div>
            <div class="input-group">
                <input type="text" id="userInput" placeholder="{ui["ph"]}">
                <button id="ask-btn" class="ask-btn"
                    onclick="handleQuestion('{ui["thinking"]}','{ui["alert"]}','{ui["error"]}')"
                >✦ {ui["btn"]}</button>
            </div>
        </div>
        <div class="stats">
            <div class="stat"><div class="stat-n">1M+</div><div class="stat-l">{t["students"]}</div></div>
            <div class="stat"><div class="stat-n">4.8</div><div class="stat-l">⭐ {t["rating"]}</div></div>
            <div class="stat"><div class="stat-n">50+</div><div class="stat-l">{t["countries"]}</div></div>
        </div>
        <div class="features-grid">
            <div class="feat"><span class="feat-icon">📷</span>{t["features"]["camera"]}</div>
            <div class="feat"><span class="feat-icon">🌐</span>{t["features"]["languages"]}</div>
            <div class="feat"><span class="feat-icon">📈</span>{t["features"]["steps"]}</div>
            <div class="feat"><span class="feat-icon">📱</span>{t["features"]["offline"]}</div>
        </div>
        <a href="https://play.google.com/store/apps/details?id=com.educareai.app" class="download-btn">▶ {t["download"]}</a>
        <div class="btn-sub">{t["sub"]}</div>
        <div class="footer">{t["copyright"]}</div>
    </div>
    {js_block}
</body>
</html>'''

        if lang == "es":
            ruta = os.path.join(base_dir, 'index.html')
        else:
            ruta_idioma = os.path.join(base_dir, lang)
            os.makedirs(ruta_idioma, exist_ok=True)
            ruta = os.path.join(ruta_idioma, 'index.html')

        with open(ruta, 'w', encoding='utf-8') as f:
            f.write(html)

        print(f"   ✅ Landing {lang.upper()}: {ruta}")
