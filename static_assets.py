"""
static_assets.py — Generador de archivos CSS y JS externos compartidos
Cada página los carga desde /static/ — reduciendo de 42KB a ~3KB por página
"""

SHARED_CSS = """/* Educare AI — Shared Styles v5.0 */
*,*::before,*::after{margin:0;padding:0;box-sizing:border-box}
:root{
  --b1:#1d4ed8;--b2:#2563eb;--b3:#3b82f6;--b4:#60a5fa;--b5:#93c5fd;
  --glow:rgba(37,99,235,.4);
  --bg:#050c18;--bg2:#080f1e;--card:rgba(5,12,24,.92);
  --border:rgba(37,99,235,.2);--bh:rgba(59,130,246,.48);
  --text:#e2e8f0;--muted:#475569;
}
html{scroll-behavior:smooth}
body{font-family:'Inter','Poppins',sans-serif;background:linear-gradient(140deg,var(--bg) 0%,var(--bg2) 60%,#060e1c 100%);min-height:100vh;display:flex;align-items:center;justify-content:center;padding:28px 16px;position:relative;overflow-x:hidden;color:var(--text)}
body::before{content:'';position:fixed;inset:0;background:radial-gradient(ellipse 90% 60% at 10% 10%,rgba(29,78,216,.09) 0%,transparent 55%),radial-gradient(ellipse 70% 50% at 90% 90%,rgba(96,165,250,.06) 0%,transparent 55%);pointer-events:none;z-index:0}
.grid{position:fixed;inset:0;background-image:linear-gradient(rgba(37,99,235,.022) 1px,transparent 1px),linear-gradient(90deg,rgba(37,99,235,.022) 1px,transparent 1px);background-size:56px 56px;pointer-events:none;z-index:0}
.pd{position:fixed;border-radius:50%;background:var(--b4);pointer-events:none;z-index:0;opacity:0;animation:tw linear infinite}
@keyframes tw{0%,100%{opacity:0;transform:scale(.4)}50%{opacity:.6;transform:scale(1.2)}}
.pg{position:fixed;border-radius:50%;background:radial-gradient(circle,rgba(37,99,235,.18) 0%,transparent 70%);filter:blur(1px);pointer-events:none;z-index:0;animation:gf 20s ease-in-out infinite alternate}
@keyframes gf{0%{transform:translate(0,0)}100%{transform:translate(50px,-65px) scale(1.1)}}
.card{background:var(--card);backdrop-filter:blur(32px);-webkit-backdrop-filter:blur(32px);border-radius:28px;padding:44px 52px;max-width:860px;width:100%;text-align:center;position:relative;z-index:1;border:1px solid var(--border);box-shadow:0 0 0 1px rgba(37,99,235,.06),0 30px 80px rgba(0,0,0,.7),inset 0 1px 0 rgba(255,255,255,.035);transition:border-color .4s,box-shadow .4s}
.card:hover{border-color:var(--bh)}
.card::before{content:'';position:absolute;top:0;left:15%;right:15%;height:1px;background:linear-gradient(90deg,transparent,rgba(59,130,246,.5),transparent)}
.badge{display:inline-flex;align-items:center;gap:7px;background:rgba(37,99,235,.09);border:1px solid rgba(37,99,235,.22);padding:5px 16px;border-radius:50px;font-size:.7rem;color:var(--b4);letter-spacing:1.5px;text-transform:uppercase;font-weight:700;margin-bottom:18px}
.live{width:6px;height:6px;background:#22c55e;border-radius:50%;box-shadow:0 0 6px #22c55e;animation:blink 1.5s ease-in-out infinite}
@keyframes blink{0%,100%{opacity:1}50%{opacity:.15}}
.rw{position:relative;display:inline-block;margin:6px auto 16px}
.ri{font-size:clamp(58px,8vw,82px);display:block;animation:bob 3.5s ease-in-out infinite;filter:drop-shadow(0 0 20px rgba(37,99,235,.6));position:relative;z-index:1}
@keyframes bob{0%,100%{transform:translateY(0) rotate(0deg)}33%{transform:translateY(-9px) rotate(2deg)}66%{transform:translateY(-4px) rotate(-1deg)}}
.ring{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);border-radius:50%;border:1px solid rgba(37,99,235,.22);animation:rp 2.5s ease-out infinite}
.ring1{width:95px;height:95px}.ring2{width:135px;height:135px;animation-delay:.6s;border-color:rgba(96,165,250,.15)}.ring3{width:175px;height:175px;animation-delay:1.2s;border-color:rgba(59,130,246,.08)}
@keyframes rp{0%{transform:translate(-50%,-50%) scale(.88);opacity:.55}100%{transform:translate(-50%,-50%) scale(1.06);opacity:.06}}
.brand{font-size:clamp(2rem,5vw,3.4rem);font-weight:900;background:linear-gradient(120deg,var(--b4) 0%,#38bdf8 25%,var(--b3) 50%,var(--b5) 75%,var(--b4) 100%);background-size:250% auto;-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;letter-spacing:-2px;animation:neon-shift 4s linear infinite;filter:drop-shadow(0 0 12px rgba(37,99,235,.4))}
@keyframes neon-shift{0%{background-position:0% center;filter:drop-shadow(0 0 8px rgba(37,99,235,.3))}50%{background-position:100% center;filter:drop-shadow(0 0 18px rgba(96,165,250,.7))}100%{background-position:200% center;filter:drop-shadow(0 0 8px rgba(37,99,235,.3))}}
h1{font-size:clamp(1.2rem,2.8vw,2rem);font-weight:800;color:#f0f9ff;margin:14px 0 10px;line-height:1.25;letter-spacing:-.4px}
.desc{font-size:clamp(.86rem,1.7vw,.98rem);color:#94a3b8;margin-bottom:24px;line-height:1.8;max-width:640px;margin-left:auto;margin-right:auto}
.benefit-block{background:linear-gradient(135deg,rgba(37,99,235,.07),rgba(96,165,250,.04));border:1px solid rgba(37,99,235,.16);border-radius:18px;padding:22px 26px;margin:0 0 20px;text-align:left;font-size:.9rem;color:#cbd5e1;line-height:1.9;position:relative;overflow:hidden}
.benefit-block::before{content:'';position:absolute;top:0;left:0;width:3px;height:100%;background:linear-gradient(180deg,var(--b2),var(--b4));border-radius:3px 0 0 3px}
.benefit-block p{margin:0 0 10px}.benefit-block p:last-child{margin:0}.benefit-block strong{color:var(--b4)}
.ai-section{background:rgba(5,12,24,.55);border:1px solid var(--border);border-radius:22px;padding:22px 26px;margin:0 0 24px;text-align:left;position:relative;overflow:hidden}
.ai-section::after{content:'';position:absolute;top:0;left:0;right:0;height:1px;background:linear-gradient(90deg,transparent,rgba(37,99,235,.38),transparent)}
.ai-head{display:flex;align-items:center;justify-content:space-between;margin-bottom:14px;flex-wrap:wrap;gap:8px}
.ai-label{display:flex;align-items:center;gap:8px;font-size:.78rem;font-weight:700;color:var(--b4);letter-spacing:.8px;text-transform:uppercase}
.ai-led{width:8px;height:8px;background:var(--b3);border-radius:50%;box-shadow:0 0 8px var(--b3);animation:blink 1.5s ease-in-out infinite}
.ai-ctrls{display:flex;gap:7px}
.ctrl-btn{display:inline-flex;align-items:center;gap:5px;padding:4px 12px;border-radius:50px;border:1px solid rgba(37,99,235,.22);background:rgba(37,99,235,.07);color:var(--b4);font-size:.7rem;font-weight:600;cursor:pointer;font-family:inherit;white-space:nowrap;transition:all .2s}
.ctrl-btn:hover{background:rgba(37,99,235,.16);border-color:rgba(59,130,246,.45)}
.ctrl-btn.stop-btn{border-color:rgba(239,68,68,.28);background:rgba(239,68,68,.06);color:#f87171;display:none}
.ctrl-btn.stop-btn:hover{background:rgba(239,68,68,.15)}
.ctrl-btn.copy-btn{display:none}
#ai-content{min-height:56px;color:var(--text);font-size:.91rem;line-height:1.8;margin-bottom:14px;word-wrap:break-word}
.input-row{display:flex;gap:10px;flex-wrap:wrap}
#userInput{flex:1;min-width:160px;padding:12px 20px;border-radius:50px;border:1px solid rgba(37,99,235,.2);background:rgba(255,255,255,.04);color:white;font-size:.91rem;font-family:inherit;outline:none;transition:border-color .25s,background .25s,box-shadow .25s}
#userInput::placeholder{color:rgba(255,255,255,.26)}
#userInput:focus{border-color:var(--b3);background:rgba(37,99,235,.06);box-shadow:0 0 0 3px rgba(37,99,235,.11)}
.ask-btn{display:inline-flex;align-items:center;gap:7px;padding:12px 26px;border-radius:50px;border:none;background:linear-gradient(135deg,var(--b1),var(--b3));color:white;cursor:pointer;font-weight:700;font-size:.91rem;font-family:inherit;transition:opacity .2s,box-shadow .2s,transform .1s;white-space:nowrap}
.ask-btn:hover{opacity:.88;box-shadow:0 8px 26px var(--glow)}
.ask-btn:active{transform:scale(.97)}
.ask-btn:disabled{opacity:.5;cursor:not-allowed}
.stats{display:flex;justify-content:center;gap:12px;margin:24px 0;flex-wrap:wrap}
.stat{background:rgba(5,12,24,.55);border:1px solid var(--border);border-radius:18px;padding:16px 20px;min-width:100px;transition:border-color .25s,transform .25s}
.stat:hover{border-color:rgba(59,130,246,.38);transform:translateY(-4px)}
.stat-n{font-size:clamp(1.5rem,3.2vw,2.3rem);font-weight:900;background:linear-gradient(135deg,var(--b3),var(--b4));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;line-height:1}
.stat-l{font-size:.65rem;color:var(--muted);text-transform:uppercase;letter-spacing:1.5px;margin-top:5px}
.feats{background:rgba(5,12,24,.4);border:1px solid rgba(37,99,235,.1);border-radius:14px;padding:14px 20px;margin:0 0 20px;color:#475569;font-size:.83rem;line-height:1.7}
.cta-link{display:inline-flex;align-items:center;gap:8px;background:linear-gradient(135deg,var(--b1),var(--b3));color:white;padding:14px 42px;border-radius:50px;text-decoration:none;font-weight:700;font-size:clamp(.88rem,1.8vw,1rem);margin:6px 0 10px;transition:opacity .2s,box-shadow .2s;box-shadow:0 10px 26px var(--glow)}
.cta-link:hover{opacity:.9;box-shadow:0 14px 34px var(--glow)}
.subtext{color:var(--muted);font-size:.8rem;margin:7px 0}
.urgency{display:inline-block;background:rgba(251,191,36,.08);border:1px solid rgba(251,191,36,.18);color:#fbbf24;padding:8px 24px;border-radius:50px;font-size:.8rem;font-weight:500;margin:12px 0 8px}
.footer{margin-top:24px;padding-top:14px;border-top:1px solid rgba(37,99,235,.07);font-size:.7rem;color:#1e293b}
/* Markdown & Code */
.sh-kw{color:#60a5fa;font-weight:700}.sh-fn{color:#fbbf24}.sh-str{color:#86efac}.sh-num{color:#f9a8d4}.sh-cmt{color:#64748b;font-style:italic}.sh-type{color:#c084fc}.sh-tag{color:#60a5fa}.sh-key{color:#93c5fd}.sh-line{display:block}
.md-code-block{background:#0a0f1e;border:1px solid rgba(37,99,235,.25);border-radius:14px;margin:14px 0;overflow:hidden;font-size:.82rem}
.code-header{display:flex;align-items:center;justify-content:space-between;background:#111827;padding:7px 14px;border-bottom:1px solid rgba(37,99,235,.18);gap:8px}
.code-lang-label{font-size:.68rem;font-weight:700;color:#64748b;letter-spacing:1px;font-family:monospace}
.code-copy-btn{background:none;border:1px solid rgba(37,99,235,.3);color:#60a5fa;border-radius:6px;padding:2px 8px;cursor:pointer;font-size:.78rem;transition:all .2s;font-family:monospace}
.code-copy-btn:hover{background:rgba(37,99,235,.15)}
.code-scroll{overflow-x:auto}
.code-pre{margin:0;padding:16px;font-family:'Fira Code','Courier New',monospace;font-size:.82rem;line-height:1.65;color:#e2e8f0;white-space:pre;min-width:max-content}
.inline-code{background:rgba(37,99,235,.12);border:1px solid rgba(37,99,235,.2);color:#86efac;padding:2px 6px;border-radius:5px;font-family:monospace;font-size:.85em}
.md-table-wrap{overflow-x:auto;margin:14px 0;border-radius:12px;border:1px solid rgba(37,99,235,.2)}
.md-table{width:100%;border-collapse:collapse;font-size:.85rem;min-width:400px}
.md-table th{background:rgba(37,99,235,.18);color:#93c5fd;padding:10px 14px;text-align:left;font-weight:700;font-size:.78rem;letter-spacing:.5px;text-transform:uppercase;border-bottom:1px solid rgba(37,99,235,.25)}
.md-table td{padding:9px 14px;color:#cbd5e1;border-bottom:1px solid rgba(37,99,235,.08);vertical-align:top;line-height:1.55}
.md-table tr.alt td{background:rgba(37,99,235,.04)}
.md-table tr:last-child td{border-bottom:none}
.md-table tr:hover td{background:rgba(37,99,235,.08)}
.md-h1{font-size:1.35rem;font-weight:800;color:#60a5fa;margin:16px 0 8px;padding-bottom:6px;border-bottom:1px solid rgba(37,99,235,.2)}
.md-h2{font-size:1.15rem;font-weight:700;color:#93c5fd;margin:14px 0 6px}
.md-h3{font-size:1rem;font-weight:600;color:#7dd3fc;margin:12px 0 5px}
.md-h4{font-size:.95rem;font-weight:600;color:#bae6fd;margin:10px 0 4px}
.md-p{margin:7px 0;line-height:1.8;color:#cbd5e1}
.md-p strong,strong{color:#93c5fd;font-weight:700}
.md-p em,em{color:#c084fc;font-style:italic}
.md-ul{padding-left:36px;margin:4px 0 8px 0;list-style-type:disc}
.md-ol{padding-left:22px;margin:8px 0;list-style-type:decimal}
.md-ul li,.md-ol li{margin-bottom:6px;line-height:1.7;color:#cbd5e1}
.md-ul li::marker{color:#3b82f6;font-weight:bold}
.md-ol li::marker{color:#3b82f6;font-weight:bold}
.md-blockquote{border-left:3px solid #3b82f6;padding:10px 18px;margin:12px 0;background:rgba(37,99,235,.06);border-radius:0 10px 10px 0;color:#94a3b8;font-style:italic;line-height:1.7}
.md-hr{border:none;border-top:1px solid rgba(37,99,235,.2);margin:18px 0}
a{color:#60a5fa;text-decoration:underline;text-underline-offset:3px}
.thinking-anim{display:inline-flex;align-items:center;gap:8px;color:#60a5fa;font-weight:600;font-size:.92rem}
.thinking-dots{display:inline-flex;gap:5px;margin-left:4px}
.dot-anim{width:6px;height:6px;background:#3b82f6;border-radius:50%;animation:db 1.2s ease-in-out infinite}
.dot-anim:nth-child(2){animation-delay:.2s}.dot-anim:nth-child(3){animation-delay:.4s}
@keyframes db{0%,80%,100%{transform:scale(.5);opacity:.4}40%{transform:scale(1.1);opacity:1}}
.error-msg{color:#f87171;font-size:.88rem;display:flex;align-items:center;gap:6px}
.initial-hint{color:#475569;font-style:italic;font-size:.88rem}
@media(max-width:768px){.card{padding:26px 15px;border-radius:22px}.benefit-block,.ai-section{padding:15px 16px}.input-row{flex-direction:column}.ask-btn{width:100%;justify-content:center}.stats{gap:10px}.stat{padding:13px 15px;min-width:82px}.ring1,.ring2,.ring3{display:none}.ai-head{flex-direction:column;align-items:flex-start}}
@media(max-width:480px){body{padding:14px 10px}.card{padding:20px 12px}.feats{font-size:.78rem;padding:12px 13px}}
"""

SHARED_JS = """
(function(){
'use strict';
var CPFX='edu_v5_';
var WORKER=window.EDUCARE_WORKER||'';
var LANG=window.EDUCARE_LANG||'es';
var UI=window.EDUCARE_UI||{};

/* ── Syntax Highlighting ── */
var KW={
  js:['function','var','let','const','if','else','for','while','do','switch','case','break','continue','return','try','catch','finally','throw','new','this','class','extends','import','export','async','await','typeof','instanceof'],
  py:['def','class','if','elif','else','for','while','try','except','finally','with','as','import','from','return','yield','pass','break','continue','lambda','True','False','None','and','or','not'],
  kt:['fun','val','var','class','interface','object','package','import','if','else','when','for','while','do','try','catch','finally','throw','return','break','continue','as','is','in','out','override','sealed','data','enum','suspend','null','true','false'],
  java:['public','private','protected','static','final','abstract','class','interface','extends','implements','void','int','long','float','double','boolean','if','else','for','while','do','switch','case','default','break','continue','return','try','catch','finally','throw','new','this','super','null','true','false'],
  ts:['interface','type','enum','declare','public','private','protected','readonly','abstract','any','unknown','never','void','number','string','boolean','function','var','let','const','class','extends','import','export','async','await']
};
var LM={'javascript':'js','js':'js','typescript':'ts','ts':'ts','python':'py','py':'py','kotlin':'kt','kt':'kt','java':'java','swift':'js','go':'js','rust':'js','css':'css','html':'html','xml':'html','json':'json','bash':'bash','sh':'bash'};

function esc(s){return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');}

function hlLine(line,lk){
  if(!lk)return esc(line);
  if(lk==='bash'){var t=line.replace(/^\\s+/,'');if(t.indexOf('#')===0)return '<span class="sh-cmt">'+esc(line)+'</span>';return line.replace(/(\\b(?:echo|ls|cd|mkdir|rm|cp|mv|cat|grep|git|npm|pip|python3?|node|curl|wget)\\b)/g,'<span class="sh-fn">$1</span>');}
  if(lk==='html'){return line.replace(/(&lt;\\/?)(\\w+)/g,'$1<span class="sh-tag">$2</span>').replace(/([\\w-]+)=(&quot;)/g,'<span class="sh-attr">$1</span>=$2');}
  if(lk==='json'){return line.replace(/(&quot;[^&]*&quot;)\\s*:/g,'<span class="sh-key">$1</span>:').replace(/:\\s*(&quot;[^&]*&quot;)/g,': <span class="sh-str">$1</span>').replace(/:\\s*(true|false|null)/g,': <span class="sh-kw">$1</span>').replace(/:\\s*(-?\\d+\\.?\\d*)/g,': <span class="sh-num">$1</span>');}
  var kws=KW[lk]||[];
  var result='';var i=0;
  while(i<line.length){
    var ch=line[i];
    if(ch==='"'||ch==="'"||ch==='`'){var q=ch;var str=ch;i++;while(i<line.length&&line[i]!==q){str+=line[i];i++;}str+=q;i++;result+='<span class="sh-str">'+esc(str)+'</span>';continue;}
    if(ch>='0'&&ch<='9'){var num='';while(i<line.length&&(line[i]>='0'&&line[i]<='9'||line[i]==='.'))num+=line[i++];result+='<span class="sh-num">'+esc(num)+'</span>';continue;}
    if((ch>='a'&&ch<='z')||(ch>='A'&&ch<='Z')||ch==='_'){var word='';while(i<line.length&&((line[i]>='a'&&line[i]<='z')||(line[i]>='A'&&line[i]<='Z')||(line[i]>='0'&&line[i]<='9')||line[i]==='_'))word+=line[i++];
      if(kws.indexOf(word)!==-1)result+='<span class="sh-kw">'+esc(word)+'</span>';
      else if(word[0]>='A'&&word[0]<='Z')result+='<span class="sh-type">'+esc(word)+'</span>';
      else result+=esc(word);continue;}
    if(ch==='/'&&i+1<line.length&&line[i+1]==='/'){result+='<span class="sh-cmt">'+esc(line.substring(i))+'</span>';break;}
    if(ch==='#'&&(lk==='py'||lk==='bash')){result+='<span class="sh-cmt">'+esc(line.substring(i))+'</span>';break;}
    result+=esc(ch);i++;
  }
  return result;
}

function hlCode(code,lang2){
  var lk=LM[lang2]||null;
  return code.split('\\n').map(function(l){return '<span class="sh-line">'+hlLine(l,lk)+'</span>';}).join('\\n');
}

/* ── Inline Markdown ── */
function inl(s){
  s=s.replace(/\\*\\*([^\\*\\n]+)\\*\\*/g,'<strong>$1</strong>');
  s=s.replace(/\\*([^\\*\\n]+)\\*/g,'<em>$1</em>');
  s=s.replace(/`([^`\\n]+)`/g,'<code class="inline-code">$1</code>');
  return s;
}

/* ── Table Parser ── */
function parseTbl(lines,start){
  var hds=lines[start].split('|').map(function(c){return c.trim();}).filter(Boolean);
  if(!hds.length)return null;
  var isSep=lines[start+1]&&/^[|:\\-\\s]+$/.test(lines[start+1]);
  var rs=isSep?start+2:start+1;
  var rows=[];var j=rs;
  while(j<lines.length&&lines[j].indexOf('|')!==-1){
    var cs=lines[j].split('|').map(function(c){return c.trim();}).filter(Boolean);
    if(cs.length)rows.push(cs);j++;
  }
  if(!rows.length)return null;
  var h='<div class="md-table-wrap"><table class="md-table"><thead><tr>';
  hds.forEach(function(hd){h+='<th>'+inl(hd)+'</th>';});
  h+='</tr></thead><tbody>';
  rows.forEach(function(row,ri){
    h+='<tr'+(ri%2===1?' class="alt"':')+'>';
    row.forEach(function(cell){h+='<td>'+inl(cell)+'</td>';});
    h+='</tr>';
  });
  return {html:h+'</tbody></table></div>',end:j};
}

/* ── Markdown Parser ── */
function md(text){
  if(!text)return '';
  var lines=text.split('\\n');var html='';var i=0;
  while(i<lines.length){
    var line=lines[i];var t=line.trim();
    if(t.indexOf('```')===0){
      var lg=t.substring(3).trim().toLowerCase();var code=[];i++;
      while(i<lines.length&&lines[i].trim().indexOf('```')!==0){code.push(lines[i]);i++;}
      var lbl=lg?'<div class="code-lang-label">'+esc(lg.toUpperCase())+'</div>':'';
      html+='<div class="md-code-block"><div class="code-header">'+lbl+'<button class="code-copy-btn" onclick="cpCode(this)">⧉</button></div><div class="code-scroll"><pre class="code-pre"><code>'+hlCode(code.join('\\n'),lg)+'</code></pre></div></div>';
      i++;continue;
    }
    if(t.indexOf('#### ')===0){html+='<h4 class="md-h4">'+inl(t.substring(5))+'</h4>';i++;continue;}
    if(t.indexOf('### ')===0){html+='<h3 class="md-h3">'+inl(t.substring(4))+'</h3>';i++;continue;}
    if(t.indexOf('## ')===0){html+='<h2 class="md-h2">'+inl(t.substring(3))+'</h2>';i++;continue;}
    if(t.indexOf('# ')===0){html+='<h1 class="md-h1">'+inl(t.substring(2))+'</h1>';i++;continue;}
    if(t==='---'||t==='***'){html+='<hr class="md-hr">';i++;continue;}
    if(t.indexOf('> ')===0){html+='<blockquote class="md-blockquote">'+inl(t.substring(2))+'</blockquote>';i++;continue;}
    if(t.indexOf('|')!==-1&&t.indexOf('|')!==t.length-1){var tr=parseTbl(lines,i);if(tr){html+=tr.html;i=tr.end;continue;}}
    if(t.indexOf('- ')===0||t.indexOf('* ')===0){
      html+='<ul class="md-ul">';
      while(i<lines.length&&(lines[i].trim().indexOf('- ')===0||lines[i].trim().indexOf('* ')===0)){html+='<li>'+inl(lines[i].trim().substring(2))+'</li>';i++;}
      html+='</ul>';continue;
    }
    if(/^\\d+\\.\\s/.test(t)){
      var fn=parseInt(t.match(/^(\\d+)\\.\\s/)[1],10);
      html+='<ol class="md-ol" start="'+fn+'">';
      while(i<lines.length&&/^\\d+\\.\\s/.test(lines[i].trim())){html+='<li>'+inl(lines[i].trim().replace(/^\\d+\\.\\s/,''))+'</li>';i++;}
      html+='</ol>';continue;
    }
    if(t===''){i++;continue;}
    var para=[];
    while(i<lines.length){
      var tt=lines[i].trim();
      if(!tt||tt.indexOf('```')===0||tt.indexOf('#')===0||tt.indexOf('-')===0||tt.indexOf('>')===0||tt.indexOf('|')!==-1||/^\\d+\\.\\s/.test(tt))break;
      para.push(tt);i++;
    }
    if(para.length)html+='<p class="md-p">'+inl(para.join(' '))+'</p>';
  }
  return html;
}

/* ── Copy Code ── */
window.cpCode=function(btn){
  var b=btn.closest('.md-code-block');if(!b)return;
  var c=b.querySelector('code');if(!c)return;
  navigator.clipboard.writeText(c.innerText||c.textContent).then(function(){
    var o=btn.textContent;btn.textContent='✓';btn.style.color='#22c55e';
    setTimeout(function(){btn.textContent=o;btn.style.color='';},2000);
  }).catch(function(){});
};

/* ── Typewriter ── */
var _stop=false;
async function typeHtml(el,html,spd){_stop=false;el.innerHTML='';var tmp=document.createElement('div');tmp.innerHTML=html;await typeNode(el,tmp,spd||3);}
async function typeNode(target,src,spd){
  for(var i=0;i<src.childNodes.length;i++){
    if(_stop){target.innerHTML+=src.innerHTML;return;}
    var node=src.childNodes[i];
    if(node.nodeType===3){
      var txt=node.textContent;var sp=document.createElement('span');target.appendChild(sp);
      for(var c=0;c<txt.length;c++){if(_stop){sp.textContent=txt;return;}sp.textContent+=txt[c];await new Promise(function(r){setTimeout(r,spd);});}
    }else{var cl=node.cloneNode(false);target.appendChild(cl);await typeNode(cl,node,spd);}
  }
}

/* ── AI Controls ── */
var aiEl,stopBtn,copyBtn,askBtn,inputEl;
function showCtrl(s,c){if(stopBtn)stopBtn.style.display=s?'inline-flex':'none';if(copyBtn)copyBtn.style.display=c?'inline-flex':'none';}

window.handleUserQuestion=async function(){
  if(!inputEl)return;
  var q=inputEl.value.trim();
  if(!q){alert(UI.alert||'Write a question first');return;}
  inputEl.value='';
  if(askBtn)askBtn.disabled=true;
  showCtrl(true,false);
  aiEl.innerHTML='<div class="thinking-anim">🧠 '+(UI.thinking||'Thinking')+'<span class="thinking-dots"><span class="dot-anim"></span><span class="dot-anim"></span><span class="dot-anim"></span></span></div>';
  var ck=CPFX+q.toLowerCase().substring(0,90);
  var cached=null;try{cached=sessionStorage.getItem(ck);}catch(e){}
  try{
    var raw;
    if(cached){raw=cached;}
    else{
      var resp=await fetch(WORKER,{method:'POST',headers:{'Content-Type':'application/json','User-Agent':'Mozilla/5.0 (compatible; EducareAI/5.0)'},body:JSON.stringify({prompt:q,lang:LANG})});
      var data=await resp.json();
      if(!data.text)throw new Error('empty');
      raw=data.text;
      try{sessionStorage.setItem(ck,raw);}catch(e){}
    }
    await typeHtml(aiEl,md(raw),3);
    showCtrl(false,true);
  }catch(e){
    aiEl.innerHTML='<div class="error-msg">⚠️ '+(UI.error||'Connection error')+'</div>';
    showCtrl(false,false);
  }
  if(askBtn)askBtn.disabled=false;
};

window.stopAIGeneration=function(){_stop=true;showCtrl(false,true);};
window.copyAIResponse=function(){
  if(!aiEl)return;
  var txt=aiEl.innerText||aiEl.textContent;if(!txt.trim())return;
  navigator.clipboard.writeText(txt).then(function(){
    if(copyBtn){var orig=copyBtn.innerHTML;copyBtn.innerHTML='✅ '+(UI.copied||'Copied');setTimeout(function(){copyBtn.innerHTML=orig;},2000);}
  }).catch(function(){});
};

document.addEventListener('DOMContentLoaded',function(){
  aiEl=document.getElementById('ai-content');
  stopBtn=document.getElementById('stop-btn');
  copyBtn=document.getElementById('copy-btn');
  askBtn=document.getElementById('ask-btn');
  inputEl=document.getElementById('userInput');
  if(inputEl){
    if(UI.ph)inputEl.placeholder=UI.ph;
    inputEl.addEventListener('keydown',function(e){if(e.key==='Enter'&&!e.shiftKey){e.preventDefault();handleUserQuestion();}});
  }
  if(askBtn&&UI.btn)askBtn.textContent='✦ '+UI.btn;
  var titleEl=document.getElementById('ai-title-text');
  if(titleEl&&UI.ai_title)titleEl.textContent=UI.ai_title;
  if(aiEl&&UI.initial_msg)aiEl.innerHTML='<span class="initial-hint">💡 '+UI.initial_msg+'</span>';
});
})();
"""

def crear_assets_estaticos(base_dir):
    """Crea los archivos CSS y JS compartidos en docs/static/"""
    import os
    static_dir = os.path.join(base_dir, 'static')
    os.makedirs(static_dir, exist_ok=True)

    css_path = os.path.join(static_dir, 'edu.css')
    js_path  = os.path.join(static_dir, 'edu.js')

    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(SHARED_CSS)
    with open(js_path, 'w', encoding='utf-8') as f:
        f.write(SHARED_JS)

    print(f"   ✅ CSS: {css_path} ({len(SHARED_CSS.encode())//1024}KB)")
    print(f"   ✅ JS:  {js_path} ({len(SHARED_JS.encode())//1024}KB)")
    return css_path, js_path
