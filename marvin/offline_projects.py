"""Deterministic *demo* recipe for one safe requested project when Gemini is down.

Not a generic offline AI nor an Android emulator. It does not overwrite files.
"""
from __future__ import annotations

import re
from .workspace import ProjectWorkspace

HTML = '''<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Celular Virtual | MARVIN</title><link rel="stylesheet" href="style.css"></head>
<body><main class="phone" aria-label="Celular virtual">
  <div class="status"><span id="clock">09:41</span><span>◉ Wi-Fi ▰</span></div>
  <section class="screen" id="screen"><div class="home" id="home">
    <h1>MARVIN OS</h1><p>Protótipo de celular virtual</p>
    <div class="apps">
      <button data-app="messages">💬<small>Mensagens</small></button>
      <button data-app="notes">📝<small>Notas</small></button>
      <button data-app="calculator">🧮<small>Calculadora</small></button>
      <button data-app="settings">⚙️<small>Ajustes</small></button>
    </div>
  </div><div id="app" hidden></div></section>
  <button class="nav" id="homeButton" aria-label="Voltar à tela inicial"><span></span></button>
</main><p class="hint">Protótipo HTML, CSS e JavaScript • sem Android real • tudo local</p>
<script src="app.js"></script></body></html>'''

CSS = '''*{box-sizing:border-box}body{min-height:100vh;margin:0;display:grid;place-content:center;justify-items:center;gap:15px;background:radial-gradient(circle at 50% 10%,#263a5b,#070c17 68%);font:15px system-ui,-apple-system,Segoe UI,sans-serif;color:#f7faff}
.phone{width:min(340px,94vw);height:min(700px,88vh);min-height:490px;border:9px solid #0e1119;border-radius:48px;background:linear-gradient(165deg,#235ea4,#121d48 45%,#1b1c3e);box-shadow:0 30px 65px #0009,0 0 0 2px #43506e;overflow:hidden;display:flex;flex-direction:column}.status{display:flex;justify-content:space-between;padding:19px 24px 12px;font-size:13px;font-weight:700}.screen{flex:1;overflow:auto;padding:16px}.home h1{font-size:33px;letter-spacing:.2em;margin:72px 0 8px;text-align:center}.home p{text-align:center;color:#c8d7fb}.apps{display:grid;grid-template-columns:repeat(2,1fr);gap:18px;margin:80px 18px 0}button{cursor:pointer;color:inherit}.apps button{background:#ffffff25;border:1px solid #ffffff34;border-radius:24px;height:110px;font-size:36px;display:grid;align-content:center;justify-items:center;gap:6px;transition:transform .2s}.apps button:hover{transform:translateY(-3px);background:#ffffff40}.apps small{font-size:12px}.nav{align-self:center;width:110px;height:27px;border:0;background:transparent}.nav span{display:block;width:80px;height:5px;margin:auto;border-radius:10px;background:white}.panel{background:#0b18359c;padding:20px 14px;border-radius:22px;min-height:85%;}.panel h2{margin:4px 0 20px}.back{border:0;background:#ffffff25;border-radius:10px;padding:9px 14px;margin-bottom:20px}.entry,.area{display:block;width:100%;border:1px solid #88b0ef;background:#071931;color:white;padding:12px;border-radius:10px;font:inherit;margin:10px 0}.area{height:180px;resize:vertical}.primary{border:0;border-radius:12px;padding:12px;background:#448ff1;font-weight:700}.card{padding:13px;border-radius:12px;background:#ffffff18;margin:10px 0}.calc{display:grid;grid-template-columns:repeat(4,1fr);gap:8px}.calc button{background:#ffffff2b;border:0;border-radius:11px;padding:13px;font-size:20px}.hint{color:#b9c5db;font-size:12px;text-align:center;margin:0 20px}body.light{background:radial-gradient(circle,#cde8ff,#586a8b)}body.light .phone{background:linear-gradient(#53b4e9,#4c6597)}'''

JS = '''// MARVIN OS - interface virtual offline, sem bibliotecas externas.
const app = document.querySelector('#app'); const home = document.querySelector('#home');
const $ = (id)=>document.getElementById(id);
const escapeHTML=(value)=>String(value).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
setInterval(()=>{$('clock').textContent=new Date().toLocaleTimeString('pt-BR',{hour:'2-digit',minute:'2-digit'});},1000);
function goHome(){app.hidden=true;home.hidden=false;app.innerHTML='';}
function shell(title,content){home.hidden=true;app.hidden=false;app.innerHTML=`<div class="panel"><button class="back" id="back">← Voltar</button><h2>${title}</h2>${content}</div>`;$('back').onclick=goHome;}
const apps={
 messages(){shell('💬 Mensagens',`<div class="card">MARVIN: Bem-vindo ao seu celular virtual!</div><div id="msgList"></div><input class="entry" id="msg" placeholder="Digite uma mensagem"><button class="primary" id="send">Enviar</button>`);$('send').onclick=()=>{const text=$('msg').value.trim();if(!text)return;const p=document.createElement('div');p.className='card';p.textContent='Você: '+text;$('msgList').appendChild(p);$('msg').value='';};},
 notes(){shell('📝 Notas',`<label>Suas anotações<textarea class="area" id="notes" placeholder="Escreva uma anotação..."></textarea></label><button class="primary" id="save">Salvar neste navegador</button><p id="saved"></p>`);$('notes').value=localStorage.getItem('marvin_notes')||'';$('save').onclick=()=>{localStorage.setItem('marvin_notes',$('notes').value);$('saved').textContent='✓ Anotação salva neste navegador.';};},
 calculator(){shell('🧮 Calculadora',`<input class="entry" id="display" readonly value="0"><div class="calc" id="keys"></div>`);let value='';for(const key of ['7','8','9','/','4','5','6','*','1','2','3','-','C','0','.','+','=']){let b=document.createElement('button');b.textContent=key;$('keys').appendChild(b);b.onclick=()=>{if(key==='C'){value='';}else if(key==='='){if(!/^[0-9+*/.() -]+$/.test(value)){value='Erro';}else{try{value=String(Function('"use strict";return ('+value+')')());}catch{value='Erro';}}}else{value+=key;} $('display').value=value||'0';};}},
 settings(){shell('⚙️ Ajustes',`<p>Aparência da tela</p><button class="primary" id="theme">Alternar tema</button><div class="card">Protótipo local gratuito desenvolvido pelo MARVIN.</div>`);$('theme').onclick=()=>document.body.classList.toggle('light');}
};
document.querySelectorAll('[data-app]').forEach(el=>el.addEventListener('click',()=>apps[el.dataset.app]()));
$('homeButton').addEventListener('click',goHome);
'''

def try_generate_offline(workspace: ProjectWorkspace, question: str) -> str | None:
    """Generate the specific virtual-phone demo offline after all AI models fail.

    Never overwrite existing project files or claim a generic LLM wrote them.
    """
    phrase = question.lower()
    if not (re.search(r"\b(celular virtual|simulador de celular|smartphone virtual)\b", phrase)
            and re.search(r"\b(crie|criar|cria|monte|montar|construa|construir|faça|faca)\b", phrase)):
        return None
    project = 'Celular Virtual'
    workspace.create_project(project)
    created, existing = [], []
    for filename, content in [('index.html', HTML), ('style.css', CSS), ('app.js', JS)]:
        try:
            workspace.write_project_file(project, filename, content)
            created.append(filename)
        except FileExistsError:
            existing.append(filename)
    path = workspace.project_path(project, 'index.html')
    if not created:
        return (f"O Gemini não respondeu (503). Não substituí arquivos existentes em {path.parent}. "
                "Abra o projeto e confira os arquivos antes de tentar novamente.")
    try:
        workspace.open_project(project, 'index.html')
        launched = ' Tentei abrir index.html no navegador.'
    except (OSError, RuntimeError) as exc:
        launched = f' Não consegui abrir automaticamente ({type(exc).__name__}); abra index.html manualmente.'
    return (f"O Gemini ficou indisponível (503). Criei um **protótipo offline pré-programado** "
            f"de celular virtual em {path.parent}. Arquivos criados: {', '.join(created)}. "
            + (f"Arquivos preservados: {', '.join(existing)}. " if existing else '')
            + launched + ' Ele não é um emulador Android e não usa inteligência artificial para gerar designs diferentes.')
