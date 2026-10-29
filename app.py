import json
from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Happy Birthday", page_icon="💗", layout="wide", initial_sidebar_state="collapsed")

DATA_PATH = Path(__file__).parent / "birthday_data.json"
DEFAULT = {
    "name": "Srinivas",
    "sender": "Your best friend",
    "letter_greeting": "Dear You,",
    "letter_text": "Happy Birthday!\n\nI hope your day is filled with love, laughter, and all the little things that make you smile.\n\nThank you for being such a special person. I’m wishing you a beautiful year ahead, full of happiness and wonderful memories.\n\nWith love,",
    "letter_signoff": "Your best friend",
    "bouquet_messages": ["Forever yours ♡", "My favourite, always", "I'd choose you again & again", "My world feels better with you"],
    "balloon_words": ["You", "are", "so", "loved"],
}
try:
    data = {**DEFAULT, **json.loads(DATA_PATH.read_text(encoding="utf-8"))}
except Exception:
    data = DEFAULT

def js_string(value):
    return json.dumps(value, ensure_ascii=False).replace("</", "<\\/")

html = r"""
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600&family=Playfair+Display:ital,wght@0,500;0,600;1,500;1,600&display=swap" rel="stylesheet">
<style>
:root{--pink:#d94d79;--deep:#9c385c;--ink:#704956;--muted:#a77f8d;--white:#fffdfd}
*{box-sizing:border-box}
html,body{margin:0;width:100%;min-height:100%;font-family:'DM Sans',sans-serif;color:var(--ink)}
body{overflow:hidden;background:linear-gradient(155deg,#fffdf8 0%,#fff8f6 36%,#fbe0eb 100%)}
#app{height:100vh;min-height:570px;position:relative;overflow:hidden;background:
radial-gradient(ellipse at 20% 75%,rgba(250,183,208,.28),transparent 38%),
radial-gradient(ellipse at 80% 25%,rgba(255,238,198,.48),transparent 35%),
linear-gradient(160deg,#fffdf9 0%,#fff8f5 42%,#f9ddea 100%)}
.scene{position:absolute;inset:0;display:none;align-items:center;justify-content:center;text-align:center;padding:28px 18px 54px;opacity:0;transform:translateY(10px);transition:opacity .5s ease,transform .5s ease}
.scene.active{display:flex;opacity:1;transform:translateY(0)}
.inner{width:min(780px,100%);position:relative;margin:auto}
.script{font-family:'Playfair Display',serif;font-style:italic;font-weight:500;color:#6e4050}
h1{font:italic 500 clamp(2rem,5vw,3.2rem)/1.16 'Playfair Display',serif;margin:0 0 5px;color:#744557}
h2{font:italic 500 clamp(1.2rem,3vw,1.7rem)/1.3 'Playfair Display',serif;color:#98455f;margin:0 0 22px}
p{font-size:.9rem;line-height:1.7}
button{font-family:'DM Sans',sans-serif;cursor:pointer}
.primary{border:0;background:var(--pink);color:#fff;border-radius:7px;padding:11px 24px;min-width:96px;font-size:.84rem;box-shadow:0 5px 13px #d94d792b;transition:transform .2s,background .2s}
.primary:hover{background:#c9406c;transform:translateY(-2px)}
.secondary{border:1px solid #e6d9dd;background:#fff;color:#7b5b66;border-radius:7px;padding:10px 22px;font-size:.84rem}
.hearts{position:absolute;inset:0;pointer-events:none;overflow:hidden}
.heart{position:absolute;color:#ed83a5;opacity:.55;font-size:16px;animation:drift 7s ease-in-out infinite}
.heart:nth-child(1){left:10%;top:18%;font-size:13px;animation-delay:-2s}.heart:nth-child(2){left:24%;top:32%;font-size:19px;animation-delay:-4s}.heart:nth-child(3){right:16%;top:20%;font-size:15px;animation-delay:-1s}.heart:nth-child(4){right:25%;top:43%;font-size:11px;animation-delay:-3s}.heart:nth-child(5){left:17%;bottom:22%;font-size:20px;animation-delay:-5s}.heart:nth-child(6){right:11%;bottom:24%;font-size:17px;animation-delay:-2s}.heart:nth-child(7){left:40%;top:12%;font-size:12px;animation-delay:-1s}.heart:nth-child(8){right:40%;bottom:13%;font-size:14px;animation-delay:-4s}
@keyframes drift{0%,100%{transform:translateY(0) rotate(-8deg)}50%{transform:translateY(-13px) rotate(8deg)}}
.birthday-art{position:relative;width:180px;height:160px;margin:8px auto 14px;display:flex;align-items:center;justify-content:center}
.birthday-art .bear{font-size:77px;filter:drop-shadow(0 4px 2px #00000010)}
.birthday-art .cake-mini{position:absolute;font-size:40px;bottom:7px;left:calc(50% - 21px)}
.bunting{font-size:20px;letter-spacing:3px;color:#d95a80;margin-bottom:-8px}
.question{font:500 1rem 'Playfair Display',serif;margin:5px 0 12px;color:#734457}
.choice-row{display:flex;gap:10px;justify-content:center;flex-wrap:wrap}
#noBtn{position:relative;transition:left .15s,top .15s}
.bouquet-layout{min-height:380px;display:grid;grid-template-columns:1fr 220px 1fr;align-items:center;gap:10px}
.bouquet{font-size:112px;line-height:1.3;filter:drop-shadow(0 8px 7px #a5445c24);animation:sway 4s ease-in-out infinite}
@keyframes sway{0%,100%{transform:rotate(-3deg)}50%{transform:rotate(3deg)}}
.bubble{font-size:.78rem;background:#ffffffc9;border:1px solid #f2dbe3;padding:9px 12px;border-radius:14px;box-shadow:0 4px 12px #c17d9620;margin:16px auto;width:max-content;max-width:150px;color:#8c6473}
.bubble:nth-child(2){transform:translateX(10px)}.bubble:nth-child(3){transform:translateX(-6px)}
.tree{position:absolute;bottom:26px;font-size:65px;opacity:.62;filter:saturate(.8)}
.tree.left{left:4%}.tree.right{right:4%}
.continue-wrap{margin-top:10px}
.balloons{display:flex;justify-content:center;align-items:center;gap:18px;margin:22px auto 10px;flex-wrap:wrap}
.balloon{width:54px;height:68px;border:0;border-radius:50% 50% 47% 47%;color:#fff;font-size:1rem;position:relative;box-shadow:inset -7px -7px 0 #0000000d, inset 7px 7px 0 #ffffff35;animation:float 2.6s ease-in-out infinite}
.balloon:after{content:"";position:absolute;left:50%;bottom:-11px;transform:translateX(-50%);border-left:5px solid transparent;border-right:5px solid transparent;border-top:9px solid currentColor;filter:brightness(.9)}
.balloon:before{content:"";position:absolute;left:50%;bottom:-33px;width:1px;height:23px;background:#b8a2ab}
.balloon.popped{animation:pop .25s forwards;pointer-events:none}
@keyframes float{0%,100%{transform:translateY(0)}50%{transform:translateY(-8px)}}
@keyframes pop{to{transform:scale(1.7);opacity:0}}
.balloon-note{height:30px;margin:15px auto 0;font:italic 1.1rem 'Playfair Display',serif;color:#8b5368}
.cake{font-size:112px;line-height:1.4;filter:drop-shadow(0 8px 7px #ad54701c);animation:float 3s ease-in-out infinite}
.cake-sub{font:italic 1rem 'Playfair Display',serif;color:#9b5c70;margin:0 0 24px}
.envelope{width:180px;height:116px;position:relative;margin:28px auto 24px;background:#f1c9d7;border-radius:5px;box-shadow:0 13px 28px #bd7c9224;cursor:pointer;transition:transform .25s}
.envelope:hover{transform:translateY(-5px)}
.envelope:before{content:"";position:absolute;inset:0;background:#f8dce5;clip-path:polygon(0 0,50% 57%,100% 0);border-radius:5px 5px 0 0}
.envelope:after{content:"";position:absolute;inset:0;background:#eab2c6;clip-path:polygon(0 100%,0 0,50% 55%,100% 0,100% 100%)}
.seal{position:absolute;z-index:2;left:calc(50% - 13px);top:50%;font-size:23px;transform:translateY(-15%);color:#b73f69}
.letter-card{width:min(350px,92%);min-height:220px;background:#fffefa;border:1px solid #f1e5e8;border-radius:5px;box-shadow:0 12px 30px #a86c8126;margin:0 auto;padding:22px 23px;text-align:left;position:relative;animation:letterIn .65s ease both}
@keyframes letterIn{from{opacity:0;transform:translateY(20px) scale(.97)}to{opacity:1;transform:translateY(0) scale(1)}}
.letter-heart{position:absolute;right:12px;top:12px;background:#c94f77;color:#fff;border-radius:50%;width:23px;height:23px;display:grid;place-items:center;font-size:12px}
.letter-card p{font:italic .86rem/1.8 'Playfair Display',serif;color:#6e5860;white-space:pre-line;margin:0}
.tiny-photo{position:absolute;right:12px;bottom:9px;font-size:19px}
#back{position:absolute;top:18px;left:20px;border:0;background:transparent;color:#ad6b83;font-size:.8rem;display:none;z-index:10}
#back.show{display:block}
@media(max-width:620px){
 #app{min-height:540px}
 .scene{padding:48px 16px 40px}
 .bouquet-layout{grid-template-columns:1fr;gap:0;min-height:auto}
 .bouquet{font-size:92px;grid-row:1;margin:4px 0}
 .messages-left,.messages-right{display:flex;justify-content:center;gap:5px;flex-wrap:wrap}
 .bubble{margin:4px 2px;font-size:.68rem;padding:7px 9px}
 .tree{font-size:42px;bottom:18px}.tree.left{left:0}.tree.right{right:0}
 .balloons{gap:12px}.balloon{width:47px;height:60px}
}
</style>
</head>
<body>
<div id="app">
  <div class="hearts"><span class="heart">♥</span><span class="heart">♥</span><span class="heart">♥</span><span class="heart">♥</span><span class="heart">♥</span><span class="heart">♥</span><span class="heart">♥</span><span class="heart">♥</span></div>
  <button id="back" onclick="previous()">‹ Back</button>

  <section class="scene active" id="s0">
    <div class="inner">
      <h1>Happy Birthday,<br><span id="friendTitle">Srinivas</span></h1>
      <div class="bunting">✦ △ ▽ △ ▽ ✦</div>
      <div class="birthday-art"><span class="bear">🐻‍❄️</span><span class="cake-mini">🎂</span></div>
      <p class="question">Are you excited for what's next?</p>
      <div class="choice-row">
        <button class="primary" onclick="next()">Yes</button>
        <button class="secondary" id="noBtn" onmouseenter="dodge()" ontouchstart="dodge(event)" onclick="dodge(event)">No</button>
      </div>
    </div>
  </section>

  <section class="scene" id="s1">
    <div class="inner">
      <h2>Your Rose Bouquet 🌹</h2>
      <div class="bouquet-layout">
        <div class="messages-left" id="leftMessages"></div>
        <div class="bouquet">💐</div>
        <div class="messages-right" id="rightMessages"></div>
      </div>
      <div class="tree left">🌸</div><div class="tree right">🌸</div>
      <div class="continue-wrap"><button class="primary" onclick="next()">Continue →</button></div>
    </div>
  </section>

  <section class="scene" id="s2">
    <div class="inner">
      <h2>Pop all 4 balloons</h2>
      <div class="balloon-note" id="balloonWords"></div>
      <div class="balloons" id="balloons"></div>
      <p class="tiny" id="balloonHint">Tap each balloon to reveal your message.</p>
      <div class="continue-wrap" id="balloonContinue" style="visibility:hidden"><button class="primary" onclick="next()">Continue →</button></div>
    </div>
  </section>

  <section class="scene" id="s3">
    <div class="inner">
      <h2>A little birthday wish</h2>
      <div class="cake">🎂</div>
      <p class="cake-sub">Make a wish and keep it close to your heart.</p>
      <button class="primary" onclick="next()">Continue →</button>
    </div>
  </section>

  <section class="scene" id="s4">
    <div class="inner">
      <h2>A Message From My Heart</h2>
      <div id="envelopeWrap" onclick="openLetter()">
        <div class="envelope"><span class="seal">♥</span></div>
        <p class="tiny">Tap the envelope to open your letter</p>
      </div>
      <div id="letterWrap" style="display:none">
        <div class="letter-card"><span class="letter-heart">♥</span><p id="letterText"></p><span class="tiny-photo">💐</span></div>
        <div class="continue-wrap"><button class="primary" onclick="next()">Continue →</button></div>
      </div>
    </div>
  </section>

  <section class="scene" id="s5">
    <div class="inner">
      <div class="letter-card" style="width:min(190px,80%);min-height:145px;text-align:center;padding:20px 12px;margin-bottom:16px;">
        <div style="font-size:3.3rem;line-height:1.3;">🐰 🧸</div>
        <div style="color:#d94d79;letter-spacing:.16em;font-size:.8rem;">♡ LOVE ♡</div>
      </div>
      <h2>Lots of love for you 💗</h2>
      <p class="cake-sub" id="finalSignature">With love, your best friend</p>
      <button class="primary" onclick="replay()">↻ Replay</button>
      <p id="finalConfetti" style="font-size:1.5rem;min-height:30px"></p>
    </div>
  </section>
</div>
<script>
const DATA = __DATA__;
let current=0;
function showScene(n){
 document.querySelectorAll('.scene').forEach((s,i)=>{s.classList.remove('active');if(i===n){s.style.display='flex';requestAnimationFrame(()=>s.classList.add('active'));}else{s.style.display='none';}});
 current=n;document.getElementById('back').classList.toggle('show',n>0);
}
function next(){showScene(Math.min(5,current+1));}
function previous(){showScene(Math.max(0,current-1));}
function dodge(e){
 if(e){e.preventDefault();}
 const b=document.getElementById('noBtn'); const parent=b.parentElement; const maxX=120; const maxY=36;
 b.style.position='relative';b.style.left=(Math.random()*maxX-maxX/2)+'px';b.style.top=(Math.random()*maxY-maxY/2)+'px';
}
document.getElementById('friendTitle').textContent=DATA.name||'Your Best Friend';
document.getElementById('finalSignature').textContent='With love, '+(DATA.sender||'your best friend');
function makeBubble(text){const d=document.createElement('div');d.className='bubble';d.textContent=text;return d;}
const msgs=DATA.bouquet_messages||[];
(msgs.slice(0,2)).forEach(t=>document.getElementById('leftMessages').appendChild(makeBubble(t)));
(msgs.slice(2,4)).forEach(t=>document.getElementById('rightMessages').appendChild(makeBubble(t)));
const balloonWords=DATA.balloon_words||['You','are','so','loved'];
let popped=0;
balloonWords.slice(0,4).forEach((word,i)=>{
 const b=document.createElement('button');b.className='balloon';b.textContent='♡';b.style.background=['#9bd5c4','#b9b3e6','#efadc4','#f2ce8d'][i];b.style.color=['#72bba6','#9188c6','#dd83a5','#d5aa5d'][i];b.style.animationDelay=(i*.25)+'s';
 b.addEventListener('click',()=>{if(b.classList.contains('popped'))return;b.classList.add('popped');b.textContent='';popped++;const revealed=document.createElement('span');revealed.textContent=word;revealed.style.margin='0 5px';document.getElementById('balloonWords').appendChild(revealed);if(popped===4){document.getElementById('balloonHint').textContent='You are so loved. ♡';document.getElementById('balloonContinue').style.visibility='visible';}});
 document.getElementById('balloons').appendChild(b);
});
document.getElementById('letterText').textContent=(DATA.letter_greeting||'Dear You,')+'\n\n'+(DATA.letter_text||'Happy Birthday!')+'\n\n'+(DATA.letter_signoff||'Your best friend');
function openLetter(){document.getElementById('envelopeWrap').style.display='none';document.getElementById('letterWrap').style.display='block';}
function celebrate(){document.getElementById('finalConfetti').textContent='🎉 💗 🎊 🌸 🎉';}
function replay(){document.getElementById('letterWrap').style.display='none';document.getElementById('envelopeWrap').style.display='block';document.getElementById('balloons').innerHTML='';document.getElementById('balloonWords').innerHTML='';popped=0;balloonWords.slice(0,4).forEach((word,i)=>{const b=document.createElement('button');b.className='balloon';b.textContent='♡';b.style.background=['#9bd5c4','#b9b3e6','#efadc4','#f2ce8d'][i];b.style.color=['#72bba6','#9188c6','#dd83a5','#d5aa5d'][i];b.addEventListener('click',()=>{if(b.classList.contains('popped'))return;b.classList.add('popped');b.textContent='';popped++;const revealed=document.createElement('span');revealed.textContent=word;revealed.style.margin='0 5px';document.getElementById('balloonWords').appendChild(revealed);if(popped===4){document.getElementById('balloonHint').textContent='You are so loved. ♡';document.getElementById('balloonContinue').style.visibility='visible';}});document.getElementById('balloons').appendChild(b);});document.getElementById('balloonHint').textContent='Tap each balloon to reveal your message.';document.getElementById('balloonContinue').style.visibility='hidden';showScene(0);}
</script>
</body>
</html>
"""
html = html.replace("__DATA__", js_string(data))
components.html(html, height=760, scrolling=False)
