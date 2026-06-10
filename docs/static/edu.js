
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
  if(lk==='bash'){var t=line.replace(/^\s+/,'');if(t.indexOf('#')===0)return '<span class="sh-cmt">'+esc(line)+'</span>';return line.replace(/(\b(?:echo|ls|cd|mkdir|rm|cp|mv|cat|grep|git|npm|pip|python3?|node|curl|wget)\b)/g,'<span class="sh-fn">$1</span>');}
  if(lk==='html'){return line.replace(/(&lt;\/?)(\w+)/g,'$1<span class="sh-tag">$2</span>').replace(/([\w-]+)=(&quot;)/g,'<span class="sh-attr">$1</span>=$2');}
  if(lk==='json'){return line.replace(/(&quot;[^&]*&quot;)\s*:/g,'<span class="sh-key">$1</span>:').replace(/:\s*(&quot;[^&]*&quot;)/g,': <span class="sh-str">$1</span>').replace(/:\s*(true|false|null)/g,': <span class="sh-kw">$1</span>').replace(/:\s*(-?\d+\.?\d*)/g,': <span class="sh-num">$1</span>');}
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
  return code.split('\n').map(function(l){return '<span class="sh-line">'+hlLine(l,lk)+'</span>';}).join('\n');
}

/* ── Inline Markdown ── */
function inl(s){
  s=s.replace(/\*\*([^\*\n]+)\*\*/g,'<strong>$1</strong>');
  s=s.replace(/\*([^\*\n]+)\*/g,'<em>$1</em>');
  s=s.replace(/`([^`\n]+)`/g,'<code class="inline-code">$1</code>');
  return s;
}

/* ── Table Parser ── */
function parseTbl(lines,start){
  var hds=lines[start].split('|').map(function(c){return c.trim();}).filter(Boolean);
  if(!hds.length)return null;
  var isSep=lines[start+1]&&/^[|:\-\s]+$/.test(lines[start+1]);
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
  var lines=text.split('\n');var html='';var i=0;
  while(i<lines.length){
    var line=lines[i];var t=line.trim();
    if(t.indexOf('```')===0){
      var lg=t.substring(3).trim().toLowerCase();var code=[];i++;
      while(i<lines.length&&lines[i].trim().indexOf('```')!==0){code.push(lines[i]);i++;}
      var lbl=lg?'<div class="code-lang-label">'+esc(lg.toUpperCase())+'</div>':'';
      html+='<div class="md-code-block"><div class="code-header">'+lbl+'<button class="code-copy-btn" onclick="cpCode(this)">⧉</button></div><div class="code-scroll"><pre class="code-pre"><code>'+hlCode(code.join('\n'),lg)+'</code></pre></div></div>';
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
    if(/^\d+\.\s/.test(t)){
      var fn=parseInt(t.match(/^(\d+)\.\s/)[1],10);
      html+='<ol class="md-ol" start="'+fn+'">';
      while(i<lines.length&&/^\d+\.\s/.test(lines[i].trim())){html+='<li>'+inl(lines[i].trim().replace(/^\d+\.\s/,''))+'</li>';i++;}
      html+='</ol>';continue;
    }
    if(t===''){i++;continue;}
    var para=[];
    while(i<lines.length){
      var tt=lines[i].trim();
      if(!tt||tt.indexOf('```')===0||tt.indexOf('#')===0||tt.indexOf('-')===0||tt.indexOf('>')===0||tt.indexOf('|')!==-1||/^\d+\.\s/.test(tt))break;
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
