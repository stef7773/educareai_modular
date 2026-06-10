import os
import json

def generar_frontend_impactante(base_dir):
    with open('config/frontend_texts.json', 'r') as f:
        textos = json.load(f)
    
    logo_url = "https://stef7773.github.io/EducareAI_Modular/static/images/logo-nuevo.png"
    idiomas_badge = "Español • English • Français • Deutsch • Italiano • Português • 日本語 • 한국어 • 中文 • Русский • العربية • हिन्दी • Nederlands • Polski • Türkçe • Svenska • Tiếng Việt • Українська • Български • Slovenčina • Slovenščina • Hrvatski • Lietuvių • Latviešu • Eesti • Indonesia • עברית • Azərbaycanca • Беларуская • Galego • Hausa • Հայերեն • فارسی"
    
    # URL del Worker de Cloudflare
    worker_url = "https://educare-gemini-api.stefanodelmoro7773.workers.dev"
    
    # Textos UI traducidos
    UI_TEXTS = {
        'es': {'placeholder': '✨ Escribe tu pregunta aquí...', 'button': 'Preguntar →', 'thinking': '🧠 Pensando', 'error': '⚠️ Error de conexión', 'alert': '✏️ Escribe una pregunta primero'},
        'en': {'placeholder': '✨ Write your question here...', 'button': 'Ask →', 'thinking': '🧠 Thinking', 'error': '⚠️ Connection error', 'alert': '✏️ Write a question first'},
        'fr': {'placeholder': '✨ Écrivez votre question ici...', 'button': 'Demander →', 'thinking': '🧠 Réflexion', 'error': '⚠️ Erreur de connexion', 'alert': '✏️ Écrivez d\'abord une question'},
        'de': {'placeholder': '✨ Schreiben Sie Ihre Frage hier...', 'button': 'Fragen →', 'thinking': '🧠 Denke nach', 'error': '⚠️ Verbindungsfehler', 'alert': '✏️ Schreiben Sie zuerst eine Frage'},
        'it': {'placeholder': '✨ Scrivi la tua domanda qui...', 'button': 'Chiedi →', 'thinking': '🧠 Sto pensando', 'error': '⚠️ Errore di connessione', 'alert': '✏️ Scrivi prima una domanda'},
        'pt': {'placeholder': '✨ Escreva sua pergunta aqui...', 'button': 'Perguntar →', 'thinking': '🧠 Pensando', 'error': '⚠️ Erro de conexão', 'alert': '✏️ Escreva uma pergunta primeiro'},
        'nl': {'placeholder': '✨ Schrijf uw vraag hier...', 'button': 'Vragen →', 'thinking': '🧠 Denken', 'error': '⚠️ Verbindingsfout', 'alert': '✏️ Schrijf eerst een vraag'},
        'pl': {'placeholder': '✨ Napisz swoje pytanie tutaj...', 'button': 'Zapytaj →', 'thinking': '🧠 Myślenie', 'error': '⚠️ Błąd połączenia', 'alert': '✏️ Najpierw napisz pytanie'},
        'ru': {'placeholder': '✨ Напишите свой вопрос здесь...', 'button': 'Спросить →', 'thinking': '🧠 Думаю', 'error': '⚠️ Ошибка соединения', 'alert': '✏️ Сначала напишите вопрос'},
        'ja': {'placeholder': '✨ ここに質問を書いてください...', 'button': '質問する →', 'thinking': '🧠 考え中', 'error': '⚠️ 接続エラー', 'alert': '✏️ まず質問を書いてください'},
        'zh': {'placeholder': '✨ 在这里写下你的问题...', 'button': '提问 →', 'thinking': '🧠 思考中', 'error': '⚠️ 连接错误', 'alert': '✏️ 请先写一个问题'},
        'ar': {'placeholder': '✨ اكتب سؤالك هنا...', 'button': 'اسأل →', 'thinking': '🧠 جاري التفكير', 'error': '⚠️ خطأ في الاتصال', 'alert': '✏️ اكتب سؤالاً أولاً'},
        'hi': {'placeholder': '✨ अपना प्रश्न यहाँ लिखें...', 'button': 'पूछें →', 'thinking': '🧠 सोच रहा हूँ', 'error': '⚠️ कनेक्शन त्रुटि', 'alert': '✏️ पहले एक प्रश्न लिखें'},
    }
    
    js_chat = f"""
    <script>
        const worker_url = '{worker_url}';
        
        function markdownToHtml(text) {{
            text = text.replace(/\\*\\*([^*]+)\\*\\*/g, '<strong>$1</strong>');
            text = text.replace(/\\*([^*]+)\\*/g, '<em>$1</em>');
            text = text.replace(/\\n/g, '<br>');
            return text;
        }}
        
        async function typeText(element, text, speed = 8) {{
            element.innerHTML = '';
            const htmlText = markdownToHtml(text);
            let i = 0, inTag = false, tagBuffer = '';
            while (i < htmlText.length) {{
                if (htmlText[i] === '<') {{
                    inTag = true;
                    tagBuffer = '';
                }}
                if (inTag) {{
                    tagBuffer += htmlText[i];
                    if (htmlText[i] === '>') {{
                        element.innerHTML += tagBuffer;
                        inTag = false;
                    }}
                    i++;
                }} else {{
                    element.innerHTML += htmlText[i];
                    i++;
                    await new Promise(resolve => setTimeout(resolve, speed));
                }}
            }}
        }}
        
        async function fetchAIContent(promptText, lang) {{
            const div = document.querySelector('#ai-response');
            if (!div) return;
            
            const uiTexts = {{
                thinking: '{UI_TEXTS.get("es", {}).get("thinking", "Pensando")}',
                error: '{UI_TEXTS.get("es", {}).get("error", "Error")}'
            }};
            
            let dots = 0;
            const loadingInterval = setInterval(() => {{
                dots = (dots + 1) % 4;
                div.innerHTML = '<span style="background: linear-gradient(135deg, #5a67d8, #9f7aea); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: bold;">' + uiTexts.thinking + '.'.repeat(dots) + '</span>';
            }}, 300);
            
            try {{
                const response = await fetch(worker_url, {{
                    method: 'POST',
                    headers: {{ 'Content-Type': 'application/json' }},
                    body: JSON.stringify({{ prompt: promptText }})
                }});
                const data = await response.json();
                clearInterval(loadingInterval);
                if(data.text) {{
                    await typeText(div, data.text, 8);
                }} else {{
                    div.innerHTML = '<span style="color:#ff6b6b;">⚠️ No se pudo generar respuesta</span>';
                }}
            }} catch (e) {{
                clearInterval(loadingInterval);
                div.innerHTML = '<span style="color:#ff6b6b;">💡 Error de conexión</span>';
            }}
        }}
        
        async function handleUserQuestion(lang) {{
            const input = document.getElementById('userInput');
            const question = input.value.trim();
            if (question === "") {{
                alert("Escribe una pregunta primero");
                return;
            }}
            await fetchAIContent(question, lang);
            input.value = "";
        }}
        
        document.addEventListener('DOMContentLoaded', () => {{
            const input = document.getElementById('userInput');
            if (input) {{
                input.addEventListener('keypress', (e) => {{
                    if (e.key === 'Enter') handleUserQuestion('es');
                }});
            }}
            fetchAIContent("Preséntate como Educare AI y ofrece ayuda educativa en pocas líneas", 'es');
        }});
    </script>
    """
    
    for lang, t in textos.items():
        ui = UI_TEXTS.get(lang, UI_TEXTS.get('es', {'placeholder': '✨ Write your question...', 'button': 'Ask →'}))
        
        # Determinar si es español para el JS
        js_lang = 'es' if lang == 'es' else 'en'
        
        html = f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">
    <title>{t["title"]}</title>
    <meta name="description" content="{t["description"]}">
    <meta property="og:title" content="{t["title"]}">
    <meta property="og:description" content="{t["description"]}">
    <meta property="og:image" content="{logo_url}">
    <meta property="og:type" content="website">
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800;900&display=swap" rel="stylesheet">
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: 'Montserrat', sans-serif;
            background: linear-gradient(135deg, #0a0a1a 0%, #1a1a3a 100%);
            color: white;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            position: relative;
            overflow-x: hidden;
        }}
        
        .particle {{
            position: fixed;
            width: 12px;
            height: 12px;
            background: rgba(102, 126, 234, 0.25);
            border-radius: 50%;
            pointer-events: none;
            z-index: 0;
            animation: floatParticle 35s infinite linear;
        }}
        
        @keyframes floatParticle {{
            0% {{ transform: translateY(0) translateX(0) scale(1); opacity: 0.15; }}
            50% {{ transform: translateY(-250px) translateX(200px) scale(2.5); opacity: 0.5; }}
            100% {{ transform: translateY(-500px) translateX(400px) scale(0.8); opacity: 0; }}
        }}
        
        .particle:nth-child(1) {{ top: 2%; left: 5%; animation-duration: 32s; width: 18px; height: 18px; }}
        .particle:nth-child(2) {{ top: 8%; left: 92%; animation-duration: 40s; width: 22px; height: 22px; }}
        .particle:nth-child(3) {{ top: 15%; left: 15%; animation-duration: 35s; width: 14px; height: 14px; }}
        .particle:nth-child(4) {{ top: 22%; left: 78%; animation-duration: 42s; width: 20px; height: 20px; }}
        .particle:nth-child(5) {{ top: 30%; left: 25%; animation-duration: 30s; width: 16px; height: 16px; }}
        .particle:nth-child(6) {{ top: 38%; left: 65%; animation-duration: 45s; width: 24px; height: 24px; }}
        .particle:nth-child(7) {{ top: 45%; left: 35%; animation-duration: 33s; width: 15px; height: 15px; }}
        .particle:nth-child(8) {{ top: 52%; left: 55%; animation-duration: 38s; width: 21px; height: 21px; }}
        .particle:nth-child(9) {{ top: 60%; left: 10%; animation-duration: 36s; width: 19px; height: 19px; }}
        .particle:nth-child(10) {{ top: 68%; left: 85%; animation-duration: 43s; width: 25px; height: 25px; }}
        .particle:nth-child(11) {{ top: 75%; left: 20%; animation-duration: 31s; width: 17px; height: 17px; }}
        .particle:nth-child(12) {{ top: 82%; left: 70%; animation-duration: 37s; width: 23px; height: 23px; }}
        .particle:nth-child(13) {{ top: 88%; left: 40%; animation-duration: 39s; width: 20px; height: 20px; }}
        .particle:nth-child(14) {{ top: 94%; left: 60%; animation-duration: 34s; width: 18px; height: 18px; }}
        .particle:nth-child(15) {{ top: 5%; left: 45%; animation-duration: 41s; width: 22px; height: 22px; }}
        .particle:nth-child(16) {{ top: 12%; left: 30%; animation-duration: 44s; width: 26px; height: 26px; }}
        .particle:nth-child(17) {{ top: 19%; left: 50%; animation-duration: 32s; width: 16px; height: 16px; }}
        .particle:nth-child(18) {{ top: 26%; left: 95%; animation-duration: 38s; width: 20px; height: 20px; }}
        .particle:nth-child(19) {{ top: 33%; left: 8%; animation-duration: 35s; width: 24px; height: 24px; }}
        .particle:nth-child(20) {{ top: 40%; left: 75%; animation-duration: 36s; width: 18px; height: 18px; }}
        
        .container {{
            position: relative;
            z-index: 1;
            max-width: 1200px;
            margin: 0 auto;
            padding: 40px;
            text-align: center;
        }}
        
        .robot-icon {{
            font-size: 8em;
            background: linear-gradient(135deg, #5a67d8 0%, #9f7aea 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            filter: drop-shadow(0 20px 40px rgba(90, 103, 216, 0.6));
            animation: floatRobot 5s ease-in-out infinite;
            margin-bottom: 20px;
        }}
        
        @keyframes floatRobot {{
            0%, 100% {{ transform: translateY(0) rotate(0deg); }}
            25% {{ transform: translateY(-15px) rotate(5deg); }}
            75% {{ transform: translateY(-5px) rotate(-3deg); }}
        }}
        
        .main-title {{
            font-size: 4em;
            font-weight: 900;
            background: linear-gradient(135deg, #5a67d8 0%, #9f7aea 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin: 20px 0;
            letter-spacing: -2px;
        }}
        
        .main-title span {{
            background: linear-gradient(135deg, #9f7aea 0%, #5a67d8 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        
        .slogan {{
            font-size: 1.5em;
            margin: 20px 0;
            color: rgba(255,255,255,0.95);
            line-height: 1.5;
        }}
        
        .language-badge {{
            background: rgba(255,255,255,0.15);
            padding: 12px 25px;
            border-radius: 50px;
            display: inline-block;
            margin: 20px 0;
            backdrop-filter: blur(5px);
            border: 1px solid rgba(255,255,255,0.3);
        }}
        
        /* CHAT SECTION - INPUT Y RESPUESTA */
        .chat-section {{
            margin: 40px 0;
            padding: 30px;
            background: rgba(255,255,255,0.08);
            border-radius: 40px;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255,255,255,0.15);
        }}
        
        .chat-title {{
            font-size: 1.3em;
            margin-bottom: 20px;
            color: rgba(255,255,255,0.9);
        }}
        
        #ai-response {{
            background: rgba(0,0,0,0.3);
            padding: 20px;
            border-radius: 25px;
            margin-bottom: 20px;
            text-align: left;
            line-height: 1.6;
            min-height: 100px;
            color: #e2e8f0;
        }}
        
        #ai-response strong {{
            color: #9f7aea;
        }}
        
        .input-group {{
            display: flex;
            gap: 15px;
            flex-wrap: wrap;
        }}
        
        #userInput {{
            flex: 1;
            padding: 16px 24px;
            border-radius: 60px;
            border: 2px solid rgba(255,255,255,0.2);
            background: rgba(255,255,255,0.1);
            color: white;
            font-size: 1em;
            outline: none;
        }}
        
        #userInput::placeholder {{
            color: rgba(255,255,255,0.6);
        }}
        
        #userInput:focus {{
            border-color: #9f7aea;
        }}
        
        .ask-btn {{
            padding: 16px 36px;
            border-radius: 60px;
            border: none;
            background: linear-gradient(135deg, #5a67d8, #9f7aea);
            color: white;
            cursor: pointer;
            font-weight: 700;
            font-size: 1em;
            transition: transform 0.3s;
        }}
        
        .ask-btn:hover {{
            transform: scale(1.05);
        }}
        
        .stats {{
            display: flex;
            justify-content: center;
            gap: 60px;
            margin: 40px 0;
            flex-wrap: wrap;
        }}
        
        .stat-item {{
            text-align: center;
            background: rgba(255,255,255,0.08);
            padding: 20px 30px;
            border-radius: 30px;
            backdrop-filter: blur(5px);
            min-width: 140px;
        }}
        
        .stat-number {{
            font-size: 3em;
            font-weight: 900;
            background: linear-gradient(135deg, #5a67d8 0%, #9f7aea 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            line-height: 1;
        }}
        
        .stat-label {{
            font-size: 1em;
            color: rgba(255,255,255,0.8);
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-top: 5px;
        }}
        
        .features-preview {{
            display: flex;
            justify-content: center;
            gap: 30px;
            margin: 40px 0;
            flex-wrap: wrap;
        }}
        
        .feature-item {{
            background: rgba(255,255,255,0.08);
            padding: 20px 30px;
            border-radius: 20px;
            text-align: center;
            transition: transform 0.3s;
            border: 1px solid rgba(255,255,255,0.15);
            min-width: 160px;
        }}
        
        .feature-item:hover {{
            transform: translateY(-5px);
            background: rgba(255,255,255,0.15);
        }}
        
        .download-btn {{
            display: inline-flex;
            align-items: center;
            gap: 15px;
            background: linear-gradient(135deg, #5a67d8 0%, #9f7aea 100%);
            color: white;
            padding: 20px 60px;
            border-radius: 80px;
            text-decoration: none;
            font-weight: 800;
            font-size: 1.8em;
            margin: 20px 0;
            transition: all 0.4s;
            box-shadow: 0 20px 40px rgba(90, 103, 216, 0.5);
            border: 2px solid rgba(255,255,255,0.3);
            animation: pulse 2s infinite;
        }}
        
        .download-btn::before {{
            content: "";
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
            transition: left 0.6s;
        }}
        
        .download-btn:hover::before {{
            left: 100%;
        }}
        
        .download-btn:hover {{
            transform: scale(1.05);
            box-shadow: 0 30px 60px rgba(90, 103, 216, 0.8);
            animation: none;
        }}
        
        @keyframes pulse {{
            0%, 100% {{ transform: scale(1); }}
            50% {{ transform: scale(1.02); }}
        }}
        
        .btn-sub {{
            color: rgba(255,255,255,0.7);
            font-size: 1.1em;
            margin-top: 10px;
        }}
        
        .footer {{
            margin-top: 60px;
            padding: 20px;
            border-top: 1px solid rgba(255,255,255,0.1);
            font-size: 0.9em;
            color: rgba(255,255,255,0.4);
        }}
        
        @media (max-width: 768px) {{
            .robot-icon {{ font-size: 5em; }}
            .main-title {{ font-size: 2.5em; }}
            .slogan {{ font-size: 1.2em; }}
            .download-btn {{ font-size: 1.2em; padding: 15px 30px; }}
            .stats {{ gap: 20px; }}
            .stat-number {{ font-size: 2em; }}
            .feature-item {{ padding: 15px 20px; min-width: 120px; }}
            .input-group {{ flex-direction: column; }}
            .ask-btn {{ width: 100%; }}
            .chat-section {{ padding: 20px; }}
        }}
    </style>
</head>
<body>
    <div class="particle"></div><div class="particle"></div><div class="particle"></div><div class="particle"></div>
    <div class="particle"></div><div class="particle"></div><div class="particle"></div><div class="particle"></div>
    <div class="particle"></div><div class="particle"></div><div class="particle"></div><div class="particle"></div>
    <div class="particle"></div><div class="particle"></div><div class="particle"></div><div class="particle"></div>
    <div class="particle"></div><div class="particle"></div><div class="particle"></div><div class="particle"></div>

    <div class="container">
        <i class="fas fa-robot robot-icon"></i>
        <div class="main-title">Educare <span>AI</span></div>
        <div class="slogan">{t["slogan"]}</div>
        <div class="language-badge">🌍 {t["badge"]} {idiomas_badge}</div>
        
        <!-- SECCIÓN DE CHAT -->
        <div class="chat-section">
            <div class="chat-title">💬 {t.get("chat_title", "Pregunta a Educare AI")}</div>
            <div id="ai-response">🤖 ¡Hola! Soy Educare AI. ¿En qué puedo ayudarte hoy?</div>
            <div class="input-group">
                <input type="text" id="userInput" placeholder="{ui['placeholder']}">
                <button class="ask-btn" onclick="handleUserQuestion('{js_lang}')">{ui['button']}</button>
            </div>
        </div>
        
        <div class="stats">
            <div class="stat-item"><div class="stat-number">1M+</div><div class="stat-label">{t["students"]}</div></div>
            <div class="stat-item"><div class="stat-number">4.8</div><div class="stat-label">⭐ {t["rating"]}</div></div>
            <div class="stat-item"><div class="stat-number">50+</div><div class="stat-label">{t["countries"]}</div></div>
        </div>
        <div class="features-preview">
            <div class="feature-item"><i class="fas fa-camera"></i><br>{t["features"]["camera"]}</div>
            <div class="feature-item"><i class="fas fa-language"></i><br>{t["features"]["languages"]}</div>
            <div class="feature-item"><i class="fas fa-chart-line"></i><br>{t["features"]["steps"]}</div>
            <div class="feature-item"><i class="fas fa-mobile-alt"></i><br>{t["features"]["offline"]}</div>
        </div>
        <a href="https://play.google.com/store/apps/details?id=com.educareai.app" class="download-btn">{t["download"]}</a>
        <div class="btn-sub">{t["sub"]}</div>
        <div class="footer">{t["copyright"]}</div>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/js/all.min.js"></script>
    {js_chat}
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
        
        print(f"   ✅ Index {lang.upper()}: {ruta} (con chat incluido)")
