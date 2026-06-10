"""
shared_js.py — Motor JS compartido para Educare AI
- Parser Markdown completo sin regex problemáticos
- Resaltado de sintaxis para código
- Tablas responsive
- Typewriter efecto
- Botones Stop y Copy
- Sin SyntaxError en ningún idioma
"""


def get_markdown_js(worker_url, lang, ui):
    """JS para páginas secundarias (html_builder)."""
    return f"""
<script>
(function(){{
    'use strict';

    var WORKER = '{worker_url}';
    var LANG   = '{lang}';
    var CPFX   = 'edu_v4_';

    var T = {{
        ph:      '{ui["ph"]}',
        btn:     '{ui["btn"]}',
        stop:    '{ui["stop"]}',
        copy:    '{ui["copy"]}',
        copied:  '{ui["copied"]}',
        thinking:'{ui["thinking"]}',
        error:   '{ui["error"]}',
        alert:   '{ui["alert"]}',
        aiTitle: '{ui["ai_title"]}',
        initial: '{ui["initial_msg"]}'
    }};

    /* ─────────────────────────────────────────
       SYNTAX HIGHLIGHTER
    ───────────────────────────────────────── */
    var KEYWORDS = {{
        js:  ['function','var','let','const','if','else','for','while','do','switch','case','break','continue','return','try','catch','finally','throw','new','this','class','extends','import','export','async','await','typeof','instanceof'],
        ts:  ['interface','type','enum','namespace','declare','public','private','protected','readonly','abstract','implements','any','unknown','never','void','number','string','boolean','function','var','let','const','class','extends','import','export','async','await'],
        py:  ['def','class','if','elif','else','for','while','try','except','finally','with','as','import','from','return','yield','pass','break','continue','lambda','True','False','None','and','or','not','in','is'],
        kt:  ['fun','val','var','class','interface','object','package','import','if','else','when','for','while','do','try','catch','finally','throw','return','break','continue','as','is','in','out','by','get','set','constructor','init','this','super','null','true','false','override','sealed','data','enum','companion','suspend','coroutine'],
        java:['public','private','protected','static','final','abstract','class','interface','extends','implements','void','int','long','float','double','boolean','char','if','else','for','while','do','switch','case','default','break','continue','return','try','catch','finally','throw','new','this','super','import','package','null','true','false'],
        swift:['func','var','let','class','struct','enum','protocol','extension','if','else','for','while','switch','case','default','guard','defer','return','throw','try','catch','in','where','self','super','import','public','private','internal','static','mutating','override','init','deinit','nil','true','false'],
        go:  ['func','var','const','type','struct','interface','if','else','for','range','switch','case','default','break','continue','return','defer','go','chan','map','package','import','nil','true','false'],
        rust:['fn','let','mut','const','static','struct','enum','impl','trait','if','else','for','while','loop','match','break','continue','return','use','mod','pub','async','await','true','false'],
        css: ['color','background','font','margin','padding','border','width','height','display','position','flex','grid','animation','transition','transform','opacity','overflow','cursor']
    }};

    var LANG_MAP = {{
        'javascript':'js','js':'js','typescript':'ts','ts':'ts',
        'python':'py','py':'py','kotlin':'kt','kt':'kt',
        'java':'java','swift':'swift','go':'go','rust':'rust',
        'css':'css','html':'html','xml':'html','json':'json',
        'bash':'bash','sh':'bash','shell':'bash'
    }};

    function escHtml(s){{
        return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
    }}

    function highlightToken(token, langKey){{
        if(!token) return '';
        var kws = KEYWORDS[langKey] || [];
        if(kws.indexOf(token) !== -1) return '<span class="sh-kw">' + escHtml(token) + '</span>';
        return escHtml(token);
    }}

    function highlightLine(line, langKey){{
        if(langKey === 'html' || langKey === 'xml'){{
            return line
                .replace(/(&lt;\/?)([\w\-]+)/g,'$1<span class="sh-tag">$2</span>')
                .replace(/([\w\-]+)=(&quot;)/g,'<span class="sh-attr">$1</span>=$2')
                .replace(/(&lt;!--[\s\S]*?--&gt;)/g,'<span class="sh-cmt">$1</span>');
        }}
        if(langKey === 'json'){{
            return line
                .replace(/(&quot;[^&]*&quot;)\s*:/g,'<span class="sh-key">$1</span>:')
                .replace(/:\s*(&quot;[^&]*&quot;)/g,': <span class="sh-str">$1</span>')
                .replace(/:\s*(true|false|null)/g,': <span class="sh-kw">$1</span>')
                .replace(/:\s*(-?\d+\.?\d*)/g,': <span class="sh-num">$1</span>');
        }}
        if(langKey === 'bash'){{
            var trimmed = line.trimLeft ? line.trimLeft() : line.replace(/^\s+/,'');
            if(trimmed.indexOf('#') === 0) return '<span class="sh-cmt">' + line + '</span>';
            return line.replace(/(\b(?:echo|ls|cd|mkdir|rm|cp|mv|cat|grep|chmod|git|npm|pip|python|python3|node|curl|wget)\b)/g,'<span class="sh-fn">$1</span>');
        }}
        var lk = langKey || 'js';
        var kws = KEYWORDS[lk] || [];
        /* Comment detection */
        var commentIdx = -1;
        var commentStyle = '';
        var singleComments = ['//','#','--'];
        for(var ci = 0; ci < singleComments.length; ci++){{
            var idx = line.indexOf(singleComments[ci]);
            if(idx !== -1 && (commentIdx === -1 || idx < commentIdx)){{
                commentIdx = idx;
                commentStyle = singleComments[ci];
            }}
        }}
        var codePart = commentIdx !== -1 ? line.substring(0, commentIdx) : line;
        var commentPart = commentIdx !== -1 ? line.substring(commentIdx) : '';
        var result = '';
        var i = 0;
        while(i < codePart.length){{
            var ch = codePart[i];
            /* Strings */
            if(ch === '"' || ch === "'" || ch === '`'){{
                var q = ch; var str = ch; i++;
                while(i < codePart.length && codePart[i] !== q){{
                    str += codePart[i]; i++;
                }}
                str += q; i++;
                result += '<span class="sh-str">' + escHtml(str) + '</span>';
                continue;
            }}
            /* Numbers */
            if(ch >= '0' && ch <= '9'){{
                var num = '';
                while(i < codePart.length && ((codePart[i] >= '0' && codePart[i] <= '9') || codePart[i] === '.')){{
                    num += codePart[i]; i++;
                }}
                result += '<span class="sh-num">' + escHtml(num) + '</span>';
                continue;
            }}
            /* Words/keywords */
            if((ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z') || ch === '_'){{
                var word = '';
                while(i < codePart.length && ((codePart[i] >= 'a' && codePart[i] <= 'z') || (codePart[i] >= 'A' && codePart[i] <= 'Z') || (codePart[i] >= '0' && codePart[i] <= '9') || codePart[i] === '_')){{
                    word += codePart[i]; i++;
                }}
                /* Check next char for function call */
                var nextCh = codePart[i] || '';
                while(nextCh === ' ') nextCh = codePart[++i] || '';
                if(nextCh === '('){{
                    if(kws.indexOf(word) !== -1){{
                        result += '<span class="sh-kw">' + escHtml(word) + '</span>';
                    }} else {{
                        result += '<span class="sh-fn">' + escHtml(word) + '</span>';
                    }}
                }} else if(kws.indexOf(word) !== -1){{
                    result += '<span class="sh-kw">' + escHtml(word) + '</span>';
                }} else if(word[0] >= 'A' && word[0] <= 'Z'){{
                    result += '<span class="sh-type">' + escHtml(word) + '</span>';
                }} else {{
                    result += escHtml(word);
                }}
                continue;
            }}
            result += escHtml(ch);
            i++;
        }}
        if(commentPart) result += '<span class="sh-cmt">' + escHtml(commentPart) + '</span>';
        return result;
    }}

    function highlightCode(code, lang2){{
        var lk = LANG_MAP[lang2] || null;
        var lines = code.split('\\n');
        var html = '';
        for(var i = 0; i < lines.length; i++){{
            var hl = lk ? highlightLine(lines[i], lk) : escHtml(lines[i]);
            html += '<span class="sh-line">' + hl + '</span>';
            if(i < lines.length - 1) html += '\\n';
        }}
        return html;
    }}

    /* ─────────────────────────────────────────
       MARKDOWN PARSER
    ───────────────────────────────────────── */
    function processInline(s){{
        s = s.replace(/\\*\\*([^\\*\\n]+)\\*\\*/g,'<strong>$1</strong>');
        s = s.replace(/\\*([^\\*\\n]+)\\*/g,'<em>$1</em>');
        s = s.replace(/__([^_\\n]+)__/g,'<strong>$1</strong>');
        s = s.replace(/_([^_\\n]+)_/g,'<em>$1</em>');
        s = s.replace(/`([^`\\n]+)`/g,'<code class="inline-code">$1</code>');
        s = s.replace(/\\[([^\\]]+)\\]\\(([^)]+)\\)/g,'<a href="$2" target="_blank" rel="noopener">$1</a>');
        return s;
    }}

    function parseTable(lines, start){{
        var headers = lines[start].split('|').map(function(c){{return c.trim();}}).filter(function(c){{return c.length > 0;}});
        if(!headers.length) return null;
        var isSep = lines[start+1] && /^[|:\\-\\s]+$/.test(lines[start+1]);
        var rowStart = isSep ? start + 2 : start + 1;
        var rows = [];
        var j = rowStart;
        while(j < lines.length && lines[j].indexOf('|') !== -1){{
            var cells = lines[j].split('|').map(function(c){{return c.trim();}}).filter(function(c){{return c.length > 0;}});
            if(cells.length) rows.push(cells);
            j++;
        }}
        if(!rows.length) return null;

        var html = '<div class="md-table-wrap"><table class="md-table"><thead><tr>';
        headers.forEach(function(h){{ html += '<th>' + processInline(h) + '</th>'; }});
        html += '</tr></thead><tbody>';
        rows.forEach(function(row, ri){{
            html += '<tr' + (ri % 2 === 1 ? ' class="alt"' : '') + '>';
            row.forEach(function(cell){{ html += '<td>' + processInline(cell) + '</td>'; }});
            html += '</tr>';
        }});
        html += '</tbody></table></div>';
        return {{html: html, end: j}};
    }}

    function md(text){{
        if(!text) return '';
        var lines = text.split('\\n');
        var html  = '';
        var i = 0;

        while(i < lines.length){{
            var line = lines[i];
            var trimmed = line.trim();

            /* Code block */
            if(trimmed.indexOf('```') === 0){{
                var lang2 = trimmed.substring(3).trim().toLowerCase();
                var code  = [];
                i++;
                while(i < lines.length && lines[i].trim().indexOf('```') !== 0){{
                    code.push(lines[i]);
                    i++;
                }}
                var codeStr = code.join('\\n');
                var highlighted = highlightCode(codeStr, lang2);
                var langLabel = lang2 ? '<div class="code-lang-label">' + escHtml(lang2.toUpperCase()) + '</div>' : '';
                var lineCount = code.length;
                var lineInfo = lineCount > 1 ? '<span class="code-line-count">' + lineCount + ' lines</span>' : '';
                html += '<div class="md-code-block">';
                html += '<div class="code-header">' + langLabel + lineInfo + '<button class="code-copy-btn" onclick="copyCode(this)" title="Copy">⧉</button></div>';
                html += '<div class="code-scroll"><pre class="code-pre"><code>' + highlighted + '</code></pre></div>';
                html += '</div>';
                i++;
                continue;
            }}

            /* Headings */
            if(trimmed.indexOf('#### ') === 0){{ html += '<h4 class="md-h4">' + processInline(trimmed.substring(5)) + '</h4>'; i++; continue; }}
            if(trimmed.indexOf('### ') === 0){{ html += '<h3 class="md-h3">' + processInline(trimmed.substring(4)) + '</h3>'; i++; continue; }}
            if(trimmed.indexOf('## ')  === 0){{ html += '<h2 class="md-h2">' + processInline(trimmed.substring(3)) + '</h2>'; i++; continue; }}
            if(trimmed.indexOf('# ')   === 0){{ html += '<h1 class="md-h1">' + processInline(trimmed.substring(2)) + '</h1>'; i++; continue; }}

            /* HR */
            if(trimmed === '---' || trimmed === '***' || trimmed === '___'){{ html += '<hr class="md-hr">'; i++; continue; }}

            /* Blockquote */
            if(trimmed.indexOf('> ') === 0){{
                html += '<blockquote class="md-blockquote">' + processInline(trimmed.substring(2)) + '</blockquote>';
                i++; continue;
            }}

            /* Table */
            if(trimmed.indexOf('|') !== -1 && trimmed.indexOf('|') !== trimmed.length - 1){{
                var tableResult = parseTable(lines, i);
                if(tableResult){{
                    html += tableResult.html;
                    i = tableResult.end;
                    continue;
                }}
            }}

            /* Unordered list */
            if(trimmed.indexOf('- ') === 0 || trimmed.indexOf('* ') === 0){{
                html += '<ul class="md-ul">';
                while(i < lines.length && (lines[i].trim().indexOf('- ') === 0 || lines[i].trim().indexOf('* ') === 0)){{
                    html += '<li>' + processInline(lines[i].trim().substring(2)) + '</li>';
                    i++;
                }}
                html += '</ul>';
                continue;
            }}

            /* Ordered list */
            if(/^\\d+\\.\\s/.test(trimmed)){{
                var firstNum = parseInt(trimmed.match(/^(\\d+)\\.\\s/)[1], 10);
                html += '<ol class="md-ol" start="' + firstNum + '">';
                while(i < lines.length && /^\\d+\\.\\s/.test(lines[i].trim())){{
                    html += '<li>' + processInline(lines[i].trim().replace(/^\\d+\\.\\s/,'')) + '</li>';
                    i++;
                }}
                html += '</ol>';
                continue;
            }}

            /* Empty line */
            if(trimmed === ''){{ i++; continue; }}

            /* Paragraph */
            var para = [];
            while(i < lines.length){{
                var t = lines[i].trim();
                if(t === '') break;
                if(t.indexOf('```') === 0) break;
                if(t.indexOf('# ') === 0 || t.indexOf('## ') === 0 || t.indexOf('### ') === 0) break;
                if(t.indexOf('- ') === 0 || t.indexOf('* ') === 0) break;
                if(/^\\d+\\.\\s/.test(t)) break;
                if(t.indexOf('> ') === 0) break;
                if(t.indexOf('|') !== -1) break;
                para.push(t);
                i++;
            }}
            if(para.length) html += '<p class="md-p">' + processInline(para.join(' ')) + '</p>';
        }}
        return html;
    }}

    /* Copy code button */
    window.copyCode = function(btn){{
        var block = btn.closest('.md-code-block');
        if(!block) return;
        var code = block.querySelector('code');
        if(!code) return;
        var text = code.innerText || code.textContent;
        navigator.clipboard.writeText(text).then(function(){{
            var orig = btn.textContent;
            btn.textContent = '✓';
            btn.style.color = '#22c55e';
            setTimeout(function(){{ btn.textContent = orig; btn.style.color = ''; }}, 2000);
        }}).catch(function(){{}});
    }};

    /* ─────────────────────────────────────────
       TYPEWRITER
    ───────────────────────────────────────── */
    var _stop = false;

    async function typeHtml(el, html, spd){{
        _stop = false;
        el.innerHTML = '';
        var tmp = document.createElement('div');
        tmp.innerHTML = html;
        await typeNode(el, tmp, spd || 3);
    }}

    async function typeNode(target, src, spd){{
        for(var i = 0; i < src.childNodes.length; i++){{
            if(_stop){{ target.innerHTML += src.innerHTML; return; }}
            var node = src.childNodes[i];
            if(node.nodeType === 3){{
                var txt = node.textContent;
                var sp = document.createElement('span');
                target.appendChild(sp);
                for(var c = 0; c < txt.length; c++){{
                    if(_stop){{ sp.textContent = txt; return; }}
                    sp.textContent += txt[c];
                    await new Promise(function(r){{ setTimeout(r, spd); }});
                }}
            }} else {{
                var cl = node.cloneNode(false);
                target.appendChild(cl);
                await typeNode(cl, node, spd);
            }}
        }}
    }}

    /* ─────────────────────────────────────────
       DOM REFS & CONTROLS
    ───────────────────────────────────────── */
    var aiContent, stopBtn, copyBtn, askBtn, userInput;

    function showCtrl(s, c){{
        if(stopBtn) stopBtn.style.display = s ? 'inline-flex' : 'none';
        if(copyBtn) copyBtn.style.display = c ? 'inline-flex' : 'none';
    }}

    /* ─────────────────────────────────────────
       MAIN ASK FUNCTION
    ───────────────────────────────────────── */
    window.handleUserQuestion = async function(){{
        if(!userInput) return;
        var q = userInput.value.trim();
        if(!q){{ alert(T.alert); return; }}
        userInput.value = '';
        if(askBtn) askBtn.disabled = true;
        showCtrl(true, false);

        aiContent.innerHTML =
            '<div class="thinking-anim">🧠 ' + T.thinking +
            '<span class="thinking-dots">' +
            '<span class="dot-anim"></span>' +
            '<span class="dot-anim"></span>' +
            '<span class="dot-anim"></span>' +
            '</span></div>';

        var ck = CPFX + q.toLowerCase().substring(0, 90);
        var cached = null;
        try{{ cached = sessionStorage.getItem(ck); }} catch(e){{}}

        try{{
            var raw;
            if(cached){{
                raw = cached;
            }} else {{
                var resp = await fetch(WORKER, {{
                    method:'POST',
                    headers:{{'Content-Type':'application/json'}},
                    body: JSON.stringify({{prompt: q, lang: LANG}})
                }});
                var data = await resp.json();
                if(!data.text) throw new Error('empty');
                raw = data.text;
                try{{ sessionStorage.setItem(ck, raw); }} catch(e){{}}
            }}
            await typeHtml(aiContent, md(raw), 3);
            showCtrl(false, true);
        }} catch(e){{
            aiContent.innerHTML = '<div class="error-msg">⚠️ ' + T.error + '</div>';
            showCtrl(false, false);
        }}
        if(askBtn) askBtn.disabled = false;
    }};

    window.stopAIGeneration = function(){{ _stop = true; showCtrl(false, true); }};

    window.copyAIResponse = function(){{
        if(!aiContent) return;
        var txt = aiContent.innerText || aiContent.textContent;
        if(!txt.trim()) return;
        navigator.clipboard.writeText(txt).then(function(){{
            if(copyBtn){{
                var orig = copyBtn.innerHTML;
                copyBtn.innerHTML = '✅ ' + T.copied;
                setTimeout(function(){{ copyBtn.innerHTML = orig; }}, 2000);
            }}
        }}).catch(function(){{}});
    }};

    /* ─────────────────────────────────────────
       INIT
    ───────────────────────────────────────── */
    document.addEventListener('DOMContentLoaded', function(){{
        aiContent = document.getElementById('ai-content');
        stopBtn   = document.getElementById('stop-btn');
        copyBtn   = document.getElementById('copy-btn');
        askBtn    = document.getElementById('ask-btn');
        userInput = document.getElementById('userInput');

        if(userInput){{
            userInput.placeholder = T.ph;
            userInput.addEventListener('keydown', function(e){{
                if(e.key === 'Enter' && !e.shiftKey){{ e.preventDefault(); handleUserQuestion(); }}
            }});
        }}
        var btn = document.getElementById('ask-btn');
        if(btn) btn.textContent = '✦ ' + T.btn;
        var titleEl = document.getElementById('ai-title-text');
        if(titleEl) titleEl.textContent = T.aiTitle;
        if(aiContent) aiContent.innerHTML = '<span class="initial-hint">💡 ' + T.initial + '</span>';
    }});
}})();
</script>"""


def get_landing_js(worker_url):
    """JS para las landings principales (frontend_builder)."""
    return f"""
<script>
(function(){{
    'use strict';
    var WORKER = '{worker_url}';
    var CPFX   = 'edu_land_v4_';

    var LANG_MAP = {{
        'javascript':'js','js':'js','typescript':'ts','ts':'ts',
        'python':'py','py':'py','kotlin':'kt','kt':'kt',
        'java':'java','swift':'swift','go':'go','rust':'rust',
        'css':'css','html':'html','xml':'html','json':'json',
        'bash':'bash','sh':'bash','shell':'bash'
    }};

    var KEYWORDS = {{
        js:  ['function','var','let','const','if','else','for','while','do','switch','case','break','continue','return','try','catch','finally','throw','new','this','class','extends','import','export','async','await','typeof','instanceof'],
        py:  ['def','class','if','elif','else','for','while','try','except','finally','with','as','import','from','return','yield','pass','break','continue','lambda','True','False','None','and','or','not'],
        kt:  ['fun','val','var','class','interface','object','package','import','if','else','when','for','while','do','try','catch','finally','throw','return','break','continue','as','is','in','out','override','sealed','data','enum','suspend','null','true','false'],
        java:['public','private','protected','static','final','abstract','class','interface','extends','implements','void','int','long','float','double','boolean','if','else','for','while','do','switch','case','default','break','continue','return','try','catch','finally','throw','new','this','super','null','true','false'],
        ts:  ['interface','type','enum','declare','public','private','protected','readonly','abstract','any','unknown','never','void','number','string','boolean','function','var','let','const','class','extends','import','export','async','await']
    }};

    function escH(s){{ return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;'); }}

    function hlLine(line, lk){{
        if(!lk) return escH(line);
        var kws = KEYWORDS[lk] || [];
        if(lk === 'bash'){{
            var t = line.replace(/^\s+/,'');
            if(t.indexOf('#') === 0) return '<span class="sh-cmt">' + escH(line) + '</span>';
            return line.replace(/(\b(?:echo|ls|cd|mkdir|rm|cp|mv|cat|grep|git|npm|pip|python3?|node|curl|wget)\b)/g,'<span class="sh-fn">$1</span>');
        }}
        var result = '';
        var i = 0;
        while(i < line.length){{
            var ch = line[i];
            if(ch === '"' || ch === "'" || ch === '`'){{
                var q = ch; var str = ch; i++;
                while(i < line.length && line[i] !== q){{ str += line[i]; i++; }}
                str += q; i++;
                result += '<span class="sh-str">' + escH(str) + '</span>';
                continue;
            }}
            if(ch >= '0' && ch <= '9'){{
                var num = '';
                while(i < line.length && ((line[i] >= '0' && line[i] <= '9') || line[i] === '.')){{ num += line[i]; i++; }}
                result += '<span class="sh-num">' + escH(num) + '</span>';
                continue;
            }}
            if((ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z') || ch === '_'){{
                var word = '';
                while(i < line.length && ((line[i] >= 'a' && line[i] <= 'z') || (line[i] >= 'A' && line[i] <= 'Z') || (line[i] >= '0' && line[i] <= '9') || line[i] === '_')){{ word += line[i]; i++; }}
                if(kws.indexOf(word) !== -1){{ result += '<span class="sh-kw">' + escH(word) + '</span>'; }}
                else if(word[0] >= 'A' && word[0] <= 'Z'){{ result += '<span class="sh-type">' + escH(word) + '</span>'; }}
                else{{ result += escH(word); }}
                continue;
            }}
            if(ch === '/' && i+1 < line.length && line[i+1] === '/'){{
                result += '<span class="sh-cmt">' + escH(line.substring(i)) + '</span>';
                break;
            }}
            if(ch === '#' && (lk === 'py' || lk === 'bash')){{
                result += '<span class="sh-cmt">' + escH(line.substring(i)) + '</span>';
                break;
            }}
            result += escH(ch); i++;
        }}
        return result;
    }}

    function hlCode(code, lang2){{
        var lk = LANG_MAP[lang2] || null;
        return code.split('\\n').map(function(l){{ return '<span class="sh-line">' + hlLine(l, lk) + '</span>'; }}).join('\\n');
    }}

    function inl(s){{
        s = s.replace(/\\*\\*([^\\*\\n]+)\\*\\*/g,'<strong>$1</strong>');
        s = s.replace(/\\*([^\\*\\n]+)\\*/g,'<em>$1</em>');
        s = s.replace(/`([^`\\n]+)`/g,'<code class="inline-code">$1</code>');
        return s;
    }}

    function parseTbl(lines, start){{
        var hds = lines[start].split('|').map(function(c){{return c.trim();}}).filter(Boolean);
        if(!hds.length) return null;
        var isSep = lines[start+1] && /^[|:\\-\\s]+$/.test(lines[start+1]);
        var rs = isSep ? start+2 : start+1;
        var rows = [];
        var j = rs;
        while(j < lines.length && lines[j].indexOf('|') !== -1){{
            var cs = lines[j].split('|').map(function(c){{return c.trim();}}).filter(Boolean);
            if(cs.length) rows.push(cs);
            j++;
        }}
        if(!rows.length) return null;
        var h = '<div class="md-table-wrap"><table class="md-table"><thead><tr>';
        hds.forEach(function(hd){{ h += '<th>' + inl(hd) + '</th>'; }});
        h += '</tr></thead><tbody>';
        rows.forEach(function(row, ri){{
            h += '<tr' + (ri%2===1?' class="alt"':'') + '>';
            row.forEach(function(cell){{ h += '<td>' + inl(cell) + '</td>'; }});
            h += '</tr>';
        }});
        return {{html: h + '</tbody></table></div>', end: j}};
    }}

    function md(text){{
        if(!text) return '';
        var lines = text.split('\\n');
        var html = ''; var i = 0;
        while(i < lines.length){{
            var line = lines[i]; var t = line.trim();
            if(t.indexOf('```') === 0){{
                var lg = t.substring(3).trim().toLowerCase();
                var code = []; i++;
                while(i < lines.length && lines[i].trim().indexOf('```') !== 0){{ code.push(lines[i]); i++; }}
                var lbl = lg ? '<div class="code-lang-label">' + escH(lg.toUpperCase()) + '</div>' : '';
                html += '<div class="md-code-block"><div class="code-header">' + lbl +
                    '<button class="code-copy-btn" onclick="cpCode(this)">⧉</button></div>' +
                    '<div class="code-scroll"><pre class="code-pre"><code>' + hlCode(code.join('\\n'), lg) + '</code></pre></div></div>';
                i++; continue;
            }}
            if(t.indexOf('### ') === 0){{ html += '<h3 class="md-h3">' + inl(t.substring(4)) + '</h3>'; i++; continue; }}
            if(t.indexOf('## ')  === 0){{ html += '<h2 class="md-h2">' + inl(t.substring(3)) + '</h2>'; i++; continue; }}
            if(t.indexOf('# ')   === 0){{ html += '<h1 class="md-h1">' + inl(t.substring(2)) + '</h1>'; i++; continue; }}
            if(t === '---' || t === '***'){{ html += '<hr class="md-hr">'; i++; continue; }}
            if(t.indexOf('> ') === 0){{ html += '<blockquote class="md-blockquote">' + inl(t.substring(2)) + '</blockquote>'; i++; continue; }}
            if(t.indexOf('|') !== -1 && t.indexOf('|') !== t.length-1){{
                var tr = parseTbl(lines, i);
                if(tr){{ html += tr.html; i = tr.end; continue; }}
            }}
            if(t.indexOf('- ') === 0 || t.indexOf('* ') === 0){{
                html += '<ul class="md-ul">';
                while(i < lines.length && (lines[i].trim().indexOf('- ') === 0 || lines[i].trim().indexOf('* ') === 0)){{
                    html += '<li>' + inl(lines[i].trim().substring(2)) + '</li>'; i++;
                }}
                html += '</ul>'; continue;
            }}
            if(/^\\d+\\.\\s/.test(t)){{
                var fn = parseInt(t.match(/^(\\d+)\\.\\s/)[1], 10);
                html += '<ol class="md-ol" start="' + fn + '">';
                while(i < lines.length && /^\\d+\\.\\s/.test(lines[i].trim())){{
                    html += '<li>' + inl(lines[i].trim().replace(/^\\d+\\.\\s/,'')) + '</li>'; i++;
                }}
                html += '</ol>'; continue;
            }}
            if(t === ''){{ i++; continue; }}
            var para = []; 
            while(i < lines.length){{
                var tt = lines[i].trim();
                if(!tt || tt.indexOf('```')===0 || tt.indexOf('#')===0 || tt.indexOf('-')===0 || tt.indexOf('>')===0 || tt.indexOf('|')!==-1 || /^\\d+\\.\\s/.test(tt)) break;
                para.push(tt); i++;
            }}
            if(para.length) html += '<p class="md-p">' + inl(para.join(' ')) + '</p>';
        }}
        return html;
    }}

    window.cpCode = function(btn){{
        var b = btn.closest('.md-code-block');
        if(!b) return;
        var c = b.querySelector('code');
        if(!c) return;
        navigator.clipboard.writeText(c.innerText||c.textContent).then(function(){{
            var o = btn.textContent; btn.textContent = '✓'; btn.style.color='#22c55e';
            setTimeout(function(){{ btn.textContent=o; btn.style.color=''; }},2000);
        }}).catch(function(){{}});
    }};

    var _stop = false;
    async function typeHtml(el, html, spd){{
        _stop=false; el.innerHTML='';
        var tmp=document.createElement('div'); tmp.innerHTML=html;
        await typeNode(el,tmp,spd||3);
    }}
    async function typeNode(target,src,spd){{
        for(var i=0;i<src.childNodes.length;i++){{
            if(_stop){{target.innerHTML+=src.innerHTML;return;}}
            var node=src.childNodes[i];
            if(node.nodeType===3){{
                var txt=node.textContent;
                var sp=document.createElement('span');target.appendChild(sp);
                for(var c=0;c<txt.length;c++){{
                    if(_stop){{sp.textContent=txt;return;}}
                    sp.textContent+=txt[c];
                    await new Promise(function(r){{setTimeout(r,spd);}});
                }}
            }} else {{
                var cl=node.cloneNode(false);target.appendChild(cl);
                await typeNode(cl,node,spd);
            }}
        }}
    }}

    var _aiDiv,_stopBtn,_copyBtn,_askBtn,_input;
    function showCtrl(s,c){{
        if(_stopBtn) _stopBtn.style.display=s?'inline-flex':'none';
        if(_copyBtn) _copyBtn.style.display=c?'inline-flex':'none';
    }}

    window.handleQuestion = async function(thinking,alertTxt,errorTxt){{
        if(!_input) return;
        var q=_input.value.trim();
        if(!q){{alert(alertTxt);return;}}
        _input.value='';
        if(_askBtn) _askBtn.disabled=true;
        showCtrl(true,false);
        _aiDiv.innerHTML='<div class="thinking-anim">🧠 '+thinking+'<span class="tdots"><span class="da"></span><span class="da"></span><span class="da"></span></span></div>';
        var ck=CPFX+q.toLowerCase().substring(0,90);
        var cached=null;
        try{{cached=sessionStorage.getItem(ck);}}catch(e){{}}
        try{{
            var raw;
            if(cached){{raw=cached;}}
            else{{
                var resp=await fetch(WORKER,{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{prompt:q}})}});
                var data=await resp.json();
                if(!data.text) throw new Error('empty');
                raw=data.text;
                try{{sessionStorage.setItem(ck,raw);}}catch(e){{}}
            }}
            await typeHtml(_aiDiv,md(raw),3);
            showCtrl(false,true);
        }}catch(e){{
            _aiDiv.innerHTML='<div class="error-msg">⚠️ '+errorTxt+'</div>';
            showCtrl(false,false);
        }}
        if(_askBtn) _askBtn.disabled=false;
    }};

    window.stopGen=function(){{_stop=true;showCtrl(false,true);}};
    window.copyResp=function(copiedTxt){{
        if(!_aiDiv) return;
        var txt=_aiDiv.innerText||_aiDiv.textContent;
        if(!txt.trim()) return;
        navigator.clipboard.writeText(txt).then(function(){{
            if(_copyBtn){{
                var orig=_copyBtn.innerHTML;
                _copyBtn.innerHTML='✅ '+copiedTxt;
                setTimeout(function(){{_copyBtn.innerHTML=orig;}},2000);
            }}
        }}).catch(function(){{}});
    }};

    document.addEventListener('DOMContentLoaded',function(){{
        _aiDiv  =document.getElementById('ai-response');
        _stopBtn=document.getElementById('stop-btn');
        _copyBtn=document.getElementById('copy-btn');
        _askBtn =document.getElementById('ask-btn');
        _input  =document.getElementById('userInput');
        if(_input){{
            _input.addEventListener('keydown',function(e){{
                if(e.key==='Enter'&&!e.shiftKey){{e.preventDefault();if(_askBtn)_askBtn.click();}}
            }});
        }}
    }});
}})();
</script>"""


def get_shared_css():
    """CSS compartido para markdown, código y tablas."""
    return """
<style>
/* ── Syntax Highlighting ── */
.sh-kw   { color:#60a5fa; font-weight:700 }
.sh-fn   { color:#fbbf24 }
.sh-str  { color:#86efac }
.sh-num  { color:#f9a8d4 }
.sh-cmt  { color:#64748b; font-style:italic }
.sh-type { color:#c084fc }
.sh-attr { color:#fbbf24 }
.sh-tag  { color:#60a5fa }
.sh-key  { color:#93c5fd }
.sh-line { display:block }

/* ── Code Block ── */
.md-code-block {
    background:#0a0f1e;
    border:1px solid rgba(37,99,235,.25);
    border-radius:14px;
    margin:14px 0;
    overflow:hidden;
    font-size:.82rem;
}
.code-header {
    display:flex;
    align-items:center;
    justify-content:space-between;
    background:#111827;
    padding:7px 14px;
    border-bottom:1px solid rgba(37,99,235,.18);
    gap:8px;
}
.code-lang-label {
    font-size:.68rem;
    font-weight:700;
    color:#64748b;
    letter-spacing:1px;
    font-family:monospace;
}
.code-line-count {
    font-size:.65rem;
    color:#475569;
    font-family:monospace;
    margin-left:auto;
}
.code-copy-btn {
    background:none;
    border:1px solid rgba(37,99,235,.3);
    color:#60a5fa;
    border-radius:6px;
    padding:2px 8px;
    cursor:pointer;
    font-size:.78rem;
    transition:all .2s;
    font-family:monospace;
}
.code-copy-btn:hover {
    background:rgba(37,99,235,.15);
    border-color:rgba(37,99,235,.6);
}
.code-scroll { overflow-x:auto }
.code-pre {
    margin:0;
    padding:16px;
    font-family:'Fira Code','Courier New',monospace;
    font-size:.82rem;
    line-height:1.65;
    color:#e2e8f0;
    white-space:pre;
    min-width:max-content;
}

/* ── Inline code ── */
.inline-code {
    background:rgba(37,99,235,.12);
    border:1px solid rgba(37,99,235,.2);
    color:#86efac;
    padding:2px 6px;
    border-radius:5px;
    font-family:'Fira Code','Courier New',monospace;
    font-size:.85em;
}

/* ── Table ── */
.md-table-wrap {
    overflow-x:auto;
    margin:14px 0;
    border-radius:12px;
    border:1px solid rgba(37,99,235,.2);
}
.md-table {
    width:100%;
    border-collapse:collapse;
    font-size:.85rem;
    min-width:400px;
}
.md-table th {
    background:rgba(37,99,235,.18);
    color:#93c5fd;
    padding:10px 14px;
    text-align:left;
    font-weight:700;
    font-size:.78rem;
    letter-spacing:.5px;
    text-transform:uppercase;
    border-bottom:1px solid rgba(37,99,235,.25);
}
.md-table td {
    padding:9px 14px;
    color:#cbd5e1;
    border-bottom:1px solid rgba(37,99,235,.08);
    vertical-align:top;
    line-height:1.55;
}
.md-table tr.alt td { background:rgba(37,99,235,.04) }
.md-table tr:last-child td { border-bottom:none }
.md-table tr:hover td { background:rgba(37,99,235,.08) }

/* ── Markdown elements ── */
.md-h1 { font-size:1.35rem;font-weight:800;color:#60a5fa;margin:16px 0 8px;padding-bottom:6px;border-bottom:1px solid rgba(37,99,235,.2) }
.md-h2 { font-size:1.15rem;font-weight:700;color:#93c5fd;margin:14px 0 6px }
.md-h3 { font-size:1rem;font-weight:600;color:#7dd3fc;margin:12px 0 5px }
.md-h4 { font-size:.95rem;font-weight:600;color:#bae6fd;margin:10px 0 4px }
.md-p  { margin:7px 0;line-height:1.8;color:#cbd5e1 }
.md-p strong, strong { color:#93c5fd;font-weight:700 }
.md-p em, em { color:#c084fc;font-style:italic }
.md-ul { padding-left:36px;margin:4px 0 8px 0;list-style-type:disc }
.md-ol { padding-left:22px;margin:8px 0;list-style-type:decimal }
.md-ol .md-ul { padding-left:20px;margin:4px 0 }
.md-ul li, .md-ol li { margin-bottom:6px;line-height:1.7;color:#cbd5e1 }
.md-ul li::marker { color:#3b82f6;font-weight:bold }
.md-ol li::marker { color:#3b82f6;font-weight:bold }
.md-blockquote {
    border-left:3px solid #3b82f6;
    padding:10px 18px;
    margin:12px 0;
    background:rgba(37,99,235,.06);
    border-radius:0 10px 10px 0;
    color:#94a3b8;
    font-style:italic;
    line-height:1.7;
}
.md-hr { border:none;border-top:1px solid rgba(37,99,235,.2);margin:18px 0 }
a { color:#60a5fa;text-decoration:underline;text-underline-offset:3px }
a:hover { color:#93c5fd }

/* ── States ── */
.thinking-anim {
    display:inline-flex;align-items:center;gap:8px;
    color:#60a5fa;font-weight:600;font-size:.92rem;
}
.thinking-dots, .tdots { display:inline-flex;gap:5px;margin-left:4px }
.dot-anim, .da {
    width:6px;height:6px;
    background:#3b82f6;border-radius:50%;
    animation:db 1.2s ease-in-out infinite;
}
.dot-anim:nth-child(2),.da:nth-child(2) { animation-delay:.2s }
.dot-anim:nth-child(3),.da:nth-child(3) { animation-delay:.4s }
@keyframes db { 0%,80%,100%{transform:scale(.5);opacity:.4} 40%{transform:scale(1.1);opacity:1} }
.error-msg { color:#f87171;font-size:.88rem;display:flex;align-items:center;gap:6px }
.initial-hint { color:#475569;font-style:italic;font-size:.88rem }
</style>"""
