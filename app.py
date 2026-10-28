import base64
import pathlib

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Tamizh Azhagan -- Full-Stack Developer", layout="wide")

GITHUB_URL = "https://github.com/Tamizh06-azhagan"
EMAIL = "azhagantamizh47@gmail.com"
PHONE = "+91 93609 52696"
PHONE_LINK = "tel:+919360952696"
RESUME_URL = "https://drive.google.com/file/d/10f8xmdLbX5Q69-pT8jKAi_S1g_fBiit6/view?usp=drive_link"

FRAME_HEIGHT = 1000

ASSETS = pathlib.Path(__file__).parent / "assets"

def img_uri(name: str) -> str:
    path = ASSETS / name
    if not path.exists():
        return ""
    mime = "image/png" if path.suffix.lower() == ".png" else "image/jpg"
    return f"data:{mime};base64,{base64.b64encode(path.read_bytes()).decode()}"

TICKET = img_uri("cineverse_ticket.png")
HOME = img_uri("cineverse_home.png")
AXON = img_uri("axon_chat.png")
PORTRAIT = img_uri("portrait.png")
DRIVER_ROUTE = img_uri("driver_route.png")
DRIVER_DRIVER = img_uri("driver_driver.jpg")
DRIVER_USER = img_uri("driver_user.jpg")
FOOD_ORPHANAGE = img_uri("food_orphanage.png")
FOOD_ACTIVITY = img_uri("food_activity.png")
FOOD_DONATION = img_uri("food_donation.png")
FOOD_LOGIN = img_uri("food_login.png")

if PORTRAIT:
    portrait_html = f'<img src="{PORTRAIT}" alt="Tamizh Azhagan" />'
    bg_html = '<img class="bgphoto" alt="" />'
else:
    portrait_html = '<div class="disc">TA</div>'
    bg_html = ''

st.markdown(
    """
    <style>
    #MainMenu, footer, header {visibility: hidden;}
    .stApp, [data-testid="stAppViewContainer"], .main {background: #0C0C0C !important;}
    .block-container {padding: 0 !important; max-width: 100% !important;}
    iframe {border: 0 !important; display: block;}
    </style>
    """,
    unsafe_allow_html=True,
)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Tamizh Azhagan -- Full-Stack Developer</title>
<link href="https://fonts.googleapis.com/css2?family=Kanit:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet" />
<style>
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { background: #0C0C0C; overflow-x: hidden; }
body { background: #0C0C0C; font-family: 'Kanit', sans-serif; color: #D7E2EA; }
a { color: inherit; text-decoration: none; }
.hero-heading {
  background: linear-gradient(180deg, #646973 0%, #BBCCD7 100%);
  -webkit-background-clip: text; background-clip: text;
  -webkit-text-fill-color: transparent;
}

/* reveal */
.fi {
  opacity: 0;
  transform: translate(var(--x, 0px), var(--y, 30px));
  transition: opacity .8s cubic-bezier(.25,.1,.25,1), transform .8s cubic-bezier(.25,.1,.25,1);
  transition-delay: var(--d, 0s);
}
.fi.in { opacity: 1; transform: none; }

/* buttons */
.cbtn {
  display: inline-block; border-radius: 999px; color: #fff; font-family: inherit; font-weight: 500;
  text-transform: uppercase; letter-spacing: .1em; border: 0; cursor: pointer;
  padding: 12px 32px; font-size: 12px;
  background: linear-gradient(123deg, #18011F 7%, #B600A8 37%, #7621B0 72%, #BE4C00 100%);
  box-shadow: 0 4px 4px rgba(181,1,167,.25), 4px 4px 12px #7721B1 inset;
  outline: 2px solid #fff; outline-offset: -3px;
  transition: transform 0.2s, box-shadow 0.2s;
}
.cbtn:hover { transform: translateY(-2px); box-shadow: 0 8px 20px rgba(181,1,167,.4), 4px 4px 12px #7721B1 inset; }
@media (min-width: 640px) { .cbtn { padding: 14px 40px; font-size: 14px; } }
@media (min-width: 768px) { .cbtn { padding: 16px 48px; font-size: 16px; } }

/* Resume button - special styling */
.rbtn {
  display: inline-flex; align-items: center; gap: 8px;
  border-radius: 999px; color: #fff; font-family: inherit; font-weight: 600;
  text-transform: uppercase; letter-spacing: .1em;
  padding: 8px 20px; font-size: 11px;
  background: linear-gradient(135deg, #4DE1FF 0%, #7621B0 50%, #B600A8 100%);
  box-shadow: 0 4px 15px rgba(77,225,255,.3), 0 0 30px rgba(118,33,176,.2);
  border: 2px solid rgba(255,255,255,.3);
  cursor: pointer;
  transition: all 0.3s cubic-bezier(.25,.1,.25,1);
  position: relative;
  overflow: hidden;
  white-space: nowrap;
}
.rbtn::before {
  content: ''; position: absolute; inset: 0;
  background: linear-gradient(135deg, transparent 0%, rgba(255,255,255,.2) 50%, transparent 100%);
  transform: translateX(-100%);
  transition: transform 0.6s;
}
.rbtn:hover::before { transform: translateX(100%); }
.rbtn:hover {
  transform: translateY(-2px) scale(1.02);
  box-shadow: 0 8px 30px rgba(77,225,255,.5), 0 0 50px rgba(182,0,168,.3);
  border-color: #fff;
}
.rbtn svg { width: 14px; height: 14px; flex-shrink: 0; }
@media (min-width: 768px) { .rbtn { padding: 10px 24px; font-size: 13px; gap: 10px; } .rbtn svg { width: 16px; height: 16px; } }

.lbtn {
  display: inline-block; border-radius: 999px; border: 2px solid #D7E2EA; background: transparent; color: #D7E2EA;
  font-family: inherit; font-weight: 500; text-transform: uppercase; letter-spacing: .1em;
  padding: 12px 28px; font-size: 14px; cursor: pointer; transition: all .2s; white-space: nowrap;
}
.lbtn:hover { background: rgba(215,226,234,.1); transform: translateY(-2px); }
.lbtn.off { border-style: dashed; opacity: .6; cursor: default; }
.lbtn.off:hover { transform: none; background: transparent; }
@media (min-width: 640px) { .lbtn { padding: 14px 36px; font-size: 16px; } }

/* glass */
.glass {
  background: linear-gradient(145deg, rgba(255,255,255,.18) 0%, rgba(255,255,255,.04) 100%);
  border: 1px solid rgba(255,255,255,.22);
  backdrop-filter: blur(18px) saturate(140%);
  -webkit-backdrop-filter: blur(18px) saturate(140%);
  box-shadow: 0 30px 70px rgba(0,0,0,.5), inset 0 1px 0 rgba(255,255,255,.35);
}

/* HERO */
.hero { height: 100vh; position: relative; overflow: hidden; display: flex; flex-direction: column; isolation: isolate; }
.hero::before {
  content: ''; position: absolute; inset: 0; z-index: 0; pointer-events: none;
  background:
    radial-gradient(ellipse 50% 45% at 50% 42%, rgba(155,134,255,.14), transparent 70%),
    radial-gradient(ellipse 40% 40% at 88% 92%, rgba(255,77,94,.09), transparent 70%);
}
.bgphoto {
  position: absolute; inset: -4%; width: 108%; height: 108%; object-fit: cover; object-position: center 35%;
  filter: blur(40px) saturate(.9); opacity: .28; z-index: 0; pointer-events: none;
  -webkit-mask-image: radial-gradient(ellipse 60% 65% at 50% 45%, #000 25%, transparent 80%);
          mask-image: radial-gradient(ellipse 60% 65% at 50% 45%, #000 25%, transparent 80%);
}
.hero::after {
  content: ''; position: absolute; inset: 0; z-index: 1; pointer-events: none;
  background:
    radial-gradient(ellipse 38% 50% at 50% 50%, rgba(255,255,255,.14), transparent 70%),
    linear-gradient(180deg, rgba(255,255,255,.04), transparent 40%);
}

/* UPDATED NAV BAR */
.nav { 
  position: relative; z-index: 3; 
  display: flex; justify-content: space-between; align-items: center; 
  padding: 24px 24px 0; gap: 20px;
}
.nav-links { display: flex; align-items: center; gap: 16px; }
@media (min-width: 768px) { .nav-links { gap: 32px; } }
.nav a { 
  color: #D7E2EA; font-weight: 500; text-transform: uppercase; letter-spacing: .05em; 
  font-size: 12px; transition: opacity .2s; cursor: pointer; 
}
.nav a:hover { opacity: .7; }
@media (min-width: 768px) { 
  .nav { padding: 32px 40px 0; } 
  .nav a { font-size: 16px; } 
}
@media (min-width: 1024px) { .nav a { font-size: 1.2rem; } }

.nav-right { display: flex; align-items: center; gap: 20px; }

.hero-badge {
  display: none; align-items: center; gap: 8px;
  font-size: 11px; text-transform: uppercase; letter-spacing: .15em;
  opacity: .7; font-weight: 500;
}
@media (min-width: 900px) { .hero-badge { display: inline-flex; } }
.hero-badge::before {
  content: ''; width: 8px; height: 8px; border-radius: 50%;
  background: #4DE1FF; box-shadow: 0 0 10px #4DE1FF;
  animation: pulse 2s ease-in-out infinite;
}
@keyframes pulse { 0%, 100% { opacity: 1; } 50% { opacity: .4; } }

.stage {
  position: relative; z-index: 2; flex: 1; min-height: 0;
  display: flex; flex-direction: column; justify-content: center;
  padding: 0 clamp(16px, 3vw, 40px);
}

.hi {
  display: flex; align-items: center; gap: 14px;
  font-size: clamp(12px, 1.2vw, 18px); font-weight: 500;
  letter-spacing: .32em; text-transform: uppercase; color: #D7E2EA;
  margin-bottom: 4px;
}
.hi::before { content: ''; width: 56px; height: 2px; background: #D7E2EA; opacity: .6; }

.nm {
  font-weight: 900; text-transform: uppercase; letter-spacing: -.02em; line-height: 1;
  font-size: min(15vw, 16vh); white-space: nowrap;
  padding: .1em 0 .16em;
  position: relative; z-index: 1;
}
.nm-top-wrap { position: relative; z-index: 1; }

.nm-bot {
  text-align: right;
  margin-top: -.3em;
  position: relative;
  z-index: 3;
}

.row {
  position: relative; z-index: 2;
  display: grid; grid-template-columns: 1fr auto 1fr; align-items: center; gap: 20px;
}

.portrait-wrap {
  grid-column: 2;
  --ph: clamp(240px, 40vh, 500px);
  height: var(--ph); width: calc(var(--ph) * .8);
  position: relative;
  z-index: 2;
}

/* UNIQUE PHOTO DESIGN */
.photo {
  height: 100%; width: 100%; position: relative; overflow: hidden;
  border-radius: 999px 999px 26px 26px;
  box-shadow: 0 40px 90px rgba(0,0,0,.65), 0 0 0 1px rgba(255,255,255,.12), inset 0 0 60px rgba(255,255,255,.05);
  background: #141418;
}

.portrait-wrap::after {
  content: '';
  position: absolute; inset: -3px;
  border-radius: 1000px 1000px 28px 28px;
  padding: 2px;
  background: conic-gradient(from 0deg, #B600A8, #7621B0, #BE4C00, #B600A8, #7621B0, #BE4C00, #B600A8);
  -webkit-mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0);
          mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0);
  -webkit-mask-composite: xor;
          mask-composite: exclude;
  animation: spin 8s linear infinite;
  pointer-events: none; z-index: 2;
}
@keyframes spin { to { transform: rotate(360deg); } }

.photo img { width: 100%; height: 100%; object-fit: cover; object-position: center top; display: block; }

.photo::after {
  content: ''; position: absolute; inset: 0; pointer-events: none;
  background: linear-gradient(180deg, rgba(255,255,255,.12) 0%, transparent 35%, transparent 70%, rgba(12,12,12,.55) 100%);
}

.portrait-wrap::before {
  content: ''; position: absolute; left: 50%; top: 50%; width: 130%; height: 115%;
  transform: translate(-50%, -50%); z-index: -1; pointer-events: none;
  background: radial-gradient(ellipse at center, rgba(255,255,255,.38) 0%, rgba(255,255,255,.12) 40%, transparent 70%);
  filter: blur(28px);
}

.portrait-wrap .accent {
  position: absolute; border-radius: 50%; pointer-events: none; z-index: 3;
  animation: float 6s ease-in-out infinite;
}
.portrait-wrap .accent.a1 { width: 14px; height: 14px; background: #B600A8; top: 8%; right: -8%; box-shadow: 0 0 20px #B600A8; }
.portrait-wrap .accent.a2 { width: 10px; height: 10px; background: #4DE1FF; bottom: 18%; left: -10%; box-shadow: 0 0 16px #4DE1FF; animation-delay: 1.5s; }
.portrait-wrap .accent.a3 { width: 8px; height: 8px; background: #FFD60A; top: 40%; left: -12%; box-shadow: 0 0 14px #FFD60A; animation-delay: 3s; }
@keyframes float { 0%, 100% { transform: translateY(0) scale(1); opacity: .8; } 50% { transform: translateY(-12px) scale(1.15); opacity: 1; } }

.portrait-wrap .corner {
  position: absolute; width: 22px; height: 22px; border: 2px solid rgba(215,226,234,.55); pointer-events: none; z-index: 3;
}
.portrait-wrap .corner.tl { top: -6px; left: -6px; border-right: 0; border-bottom: 0; border-radius: 8px 0 0 0; }
.portrait-wrap .corner.tr { top: -6px; right: -6px; border-left: 0; border-bottom: 0; border-radius: 0 8px 0 0; }
.portrait-wrap .corner.bl { bottom: -6px; left: -6px; border-right: 0; border-top: 0; border-radius: 0 0 0 8px; }
.portrait-wrap .corner.br { bottom: -6px; right: -6px; border-left: 0; border-top: 0; border-radius: 0 0 8px 0; }

.disc {
  width: 100%; height: 100%; border-radius: 22px;
  background: linear-gradient(180deg, #646973 0%, #BBCCD7 100%);
  display: flex; align-items: center; justify-content: center;
  font-size: 90px; font-weight: 900; color: #0C0C0C;
}

.side {
  display: none; flex-direction: column; gap: 16px;
  width: clamp(190px, 18vw, 260px); padding: 22px; border-radius: 26px;
}
@media (min-width: 900px) { .side { display: flex; } }
.side.left { grid-column: 1; justify-self: end; }
.side.right { grid-column: 3; justify-self: start; }
.k { font-size: 11px; letter-spacing: .2em; text-transform: uppercase; opacity: .6; }
.v { font-weight: 600; font-size: clamp(16px, 1.6vw, 22px); line-height: 1.25; color: #fff; }
.chips { display: flex; flex-wrap: wrap; gap: 6px; }
.chips span {
  font-size: 11px; text-transform: uppercase; letter-spacing: .08em;
  border: 1px solid rgba(255,255,255,.25); border-radius: 999px; padding: 4px 10px;
}
.stat { display: flex; flex-direction: column; gap: 2px; padding-bottom: 12px; border-bottom: 1px solid rgba(255,255,255,.12); }
.stat:last-child { border-bottom: 0; padding-bottom: 0; }
.big { font-weight: 900; font-size: clamp(32px, 3.4vw, 52px); line-height: 1; color: #fff; }

.bottom { margin-top: auto; position: relative; z-index: 3; display: flex; justify-content: space-between; align-items: flex-end; padding: 0 24px 28px; gap: 16px; flex-wrap: wrap; }
@media (min-width: 640px) { .bottom { padding-bottom: 32px; } }
@media (min-width: 768px) { .bottom { padding: 0 40px 40px; } }
.tagline { font-weight: 300; text-transform: uppercase; letter-spacing: .05em; line-height: 1.35; max-width: 160px; font-size: clamp(.75rem, 1.4vw, 1.5rem); }
@media (min-width: 640px) { .tagline { max-width: 220px; } }
@media (min-width: 768px) { .tagline { max-width: 260px; } }
.bottom-actions { display: flex; gap: 12px; align-items: center; flex-wrap: wrap; }

/* MARQUEE */
.marquee { background: #0C0C0C; padding: 96px 0 40px; overflow: hidden; }
@media (min-width: 640px) { .marquee { padding-top: 128px; } }
@media (min-width: 768px) { .marquee { padding-top: 160px; } }
.mrows { display: flex; flex-direction: column; gap: 12px; }
.mrow { display: flex; gap: 12px; width: max-content; will-change: transform; }
.mrow img { width: 420px; height: 270px; border-radius: 16px; object-fit: cover; flex-shrink: 0; }

/* ABOUT */
.about {
  min-height: 100vh; display: flex; align-items: center; justify-content: center;
  padding: 80px 20px; position: relative; overflow: hidden; background: #0C0C0C;
}
@media (min-width: 640px) { .about { padding: 80px 32px; } }
@media (min-width: 768px) { .about { padding: 80px 40px; } }
.about-inner { position: relative; z-index: 10; display: flex; flex-direction: column; align-items: center; gap: 64px; }
@media (min-width: 768px) { .about-inner { gap: 96px; } }
.about-top { display: flex; flex-direction: column; align-items: center; gap: 40px; }
@media (min-width: 768px) { .about-top { gap: 64px; } }
.big-h {
  font-size: clamp(3rem, 12vw, 160px); font-weight: 900; text-transform: uppercase;
  line-height: 1.1; letter-spacing: -.02em; text-align: center; padding: .05em 0 .1em;
}
.about-text {
  text-align: center; font-weight: 500; line-height: 1.6; color: #D7E2EA;
  max-width: 620px; font-size: clamp(1rem, 2vw, 1.35rem);
}
.ch { opacity: .2; }

/* SKILLS */
.skills { background: #fff; color: #0C0C0C; border-radius: 40px 40px 0 0; padding: 80px 20px; }
@media (min-width: 640px) { .skills { border-radius: 50px 50px 0 0; padding: 96px 32px; } }
@media (min-width: 768px) { .skills { border-radius: 60px 60px 0 0; padding: 128px 40px; } }
.skills .big-h { margin-bottom: 64px; }
@media (min-width: 768px) { .skills .big-h { margin-bottom: 112px; } }
.svc-list { max-width: 1024px; margin: 0 auto; border-bottom: 1px solid rgba(12,12,12,.15); }
.svc { display: flex; align-items: flex-start; gap: 24px; border-top: 1px solid rgba(12,12,12,.15); padding: 32px 0; transition: padding-left 0.3s; }
.svc:hover { padding-left: 10px; }
@media (min-width: 640px) { .svc { padding: 40px 0; } }
@media (min-width: 768px) { .svc { gap: 48px; padding: 48px 0; } }
.svc .n { font-weight: 900; line-height: 1; font-size: clamp(3rem, 10vw, 140px); }
.svc h3 { font-weight: 500; text-transform: uppercase; font-size: clamp(1rem, 2.2vw, 2.1rem); margin-bottom: 12px; }
.svc p { font-weight: 300; line-height: 1.6; max-width: 672px; opacity: .6; font-size: clamp(.85rem, 1.6vw, 1.25rem); }

/* PROJECTS */
.projects {
  background: #0C0C0C; border-radius: 40px 40px 0 0; margin-top: -40px;
  position: relative; z-index: 10; padding: 80px 20px;
}
@media (min-width: 640px) { .projects { margin-top: -48px; border-radius: 50px 50px 0 0; padding: 96px 32px; } }
@media (min-width: 768px) { .projects { margin-top: -56px; border-radius: 60px 60px 0 0; padding: 128px 40px; } }
.projects .big-h { margin-bottom: 64px; }
@media (min-width: 768px) { .projects .big-h { margin-bottom: 112px; } }
.pwrap { height: 85vh; position: relative; }
.pcard {
  position: sticky; border: 2px solid #D7E2EA; background: #0C0C0C;
  border-radius: 40px; padding: 16px; display: flex; flex-direction: column; gap: 20px;
  transform-origin: top center; will-change: transform;
  box-shadow: 0 20px 40px rgba(0,0,0,0.5);
  transition: border-color 0.3s, box-shadow 0.3s;
}
.pcard:hover {
  border-color: #B600A8;
  box-shadow: 0 20px 50px rgba(182, 0, 168, 0.15);
}
@media (min-width: 640px) { .pcard { border-radius: 50px; padding: 24px; } }
@media (min-width: 768px) { .pcard { border-radius: 60px; padding: 32px; gap: 28px; } }
.phead { display: flex; flex-wrap: wrap; justify-content: space-between; align-items: flex-start; gap: 16px; }
.ptitle { display: flex; align-items: flex-end; gap: 16px; }
@media (min-width: 768px) { .ptitle { gap: 24px; } }
.pn { font-weight: 900; line-height: 1; font-size: clamp(3rem, 10vw, 140px); }
.pmeta { display: flex; flex-direction: column; gap: 4px; padding-bottom: 4px; }
.pcat { text-transform: uppercase; letter-spacing: .1em; font-size: 12px; opacity: .6; }
@media (min-width: 640px) { .pcat { font-size: 14px; } }
.pname { font-weight: 500; text-transform: uppercase; font-size: clamp(1.25rem, 3vw, 2.5rem); }
.pbody { display: grid; grid-template-columns: 1fr; gap: 20px; }
@media (min-width: 768px) { .pbody.has-media { grid-template-columns: 1.4fr 1fr; align-items: center; } }

.pgrid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }
@media (min-width: 768px) { .pgrid { gap: 16px; } }
.pgrid.one { grid-template-columns: 1fr; }
.pgrid.two { grid-template-columns: 1fr 1fr; }

.pgrid.phones { grid-template-columns: repeat(3, 1fr); align-items: stretch; }
.pgrid.phones img { 
  height: clamp(320px, 38vw, 480px); 
  object-fit: contain; 
  background: #141418;
  padding: 8px;
  border-radius: 20px;
  border: 1px solid #262a36;
}

.pgrid.web { grid-template-columns: 1fr 1fr; }
.pgrid.web img { 
  height: clamp(180px, 24vw, 320px); 
  object-fit: cover; 
  object-position: top; 
}

.pgrid img {
  width: 100%; height: clamp(180px, 24vw, 360px); object-fit: cover; object-position: top;
  border-radius: 28px; display: block; border: 1px solid #262a36;
  transition: transform 0.3s;
}
.pgrid img:hover { transform: scale(1.02); }
@media (min-width: 640px) { .pgrid img { border-radius: 40px; } }
@media (min-width: 768px) { .pgrid img { border-radius: 48px; } }

.pdetail ul { list-style: none; display: grid; gap: 12px; font-weight: 300; line-height: 1.5; opacity: .85; font-size: clamp(.9rem, 1.4vw, 1.1rem); }
.pdetail li::before { content: '— '; opacity: .6; }
.tags { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 18px; }
.tags span { border: 1px solid #D7E2EA; border-radius: 999px; padding: 4px 12px; font-size: 13px; text-transform: uppercase; letter-spacing: .08em; opacity: .85; transition: background 0.2s, color 0.2s; }
.tags span:hover { background: #D7E2EA; color: #0C0C0C; }

/* CONTACT */
.contact { background: #0C0C0C; padding: 96px 20px 48px; border-top: 1px solid #262a36; }
@media (min-width: 768px) { .contact { padding: 128px 40px 64px; } }
.contact .big-h { margin-bottom: 56px; }
.cgrid { max-width: 920px; margin: 0 auto; display: grid; grid-template-columns: 1fr; gap: 14px; }
@media (min-width: 640px) { .cgrid { grid-template-columns: 1fr 1fr; } }
.ccard {
  display: flex; align-items: center; gap: 16px; padding: 18px 22px; border-radius: 20px;
  background: #141418; border: 1px solid #262a36; color: #D7E2EA;
  transition: border-color .2s, background .2s, transform 0.2s;
}
a.ccard:hover { border-color: #BBCCD7; background: #1a1b22; transform: translateY(-2px); }
.ccard .ic {
  width: 44px; height: 44px; border-radius: 14px; flex: none;
  background: rgba(255,255,255,.06); display: flex; align-items: center; justify-content: center;
}
.ccard .ic svg { width: 20px; height: 20px; }
.ccard small { display: block; text-transform: uppercase; letter-spacing: .12em; font-size: 11px; opacity: .55; margin-bottom: 2px; }
.ccard strong { font-weight: 500; font-size: 16px; word-break: break-all; }

/* GAME */
.game { max-width: 920px; margin: 72px auto 0; }
.game-head { display: flex; justify-content: space-between; align-items: flex-end; flex-wrap: wrap; gap: 14px; margin-bottom: 16px; }
.game-head h3 { font-weight: 800; text-transform: uppercase; font-size: clamp(1.4rem, 3vw, 2.2rem); line-height: 1; }
.stats { display: flex; flex-wrap: wrap; gap: 10px; }
.stat-box {
  border: 1px solid #262a36; border-radius: 14px; padding: 8px 14px; background: #141418;
  font-size: 12px; text-transform: uppercase; letter-spacing: .08em; opacity: .9;
}
.stat-box b { font-size: 18px; font-weight: 700; color: #fff; margin-left: 8px; letter-spacing: 0; }
.arena {
  position: relative; border-radius: 24px; overflow: hidden; border: 1px solid #262a36;
  background: linear-gradient(180deg, #14161d 0%, #0C0C0C 100%);
}
#game { display: block; width: 100%; height: 240px; outline: none; cursor: pointer; touch-action: none; }
@media (max-width: 640px) { #game { height: 200px; } }
.hint { font-size: 12px; opacity: .55; margin-top: 14px; text-align: center; text-transform: uppercase; letter-spacing: .08em; }

.foot { margin-top: 64px; font-size: 13px; opacity: .5; text-transform: uppercase; letter-spacing: .1em; text-align: center; }
</style>
</head>
<body>
<div class="main">

  <!-- HERO -->
  <section class="hero" id="top">
    {{BG_HTML}}

    <nav class="nav fi" style="--d:0s;--x:0px;--y:-20px">
      <div class="nav-links">
        <a data-go="about">About</a>
        <a data-go="projects">Projects</a>
        <a data-go="skills">Skills</a>
        <a data-go="contact">Contact</a>
      </div>
      <div class="nav-right">
        <span class="hero-badge">Available for work</span>
        <a class="rbtn" href="{{RESUME_URL}}" target="_blank" rel="noopener">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
            <polyline points="14 2 14 8 20 8"/>
            <line x1="16" y1="13" x2="8" y2="13"/>
            <line x1="16" y1="17" x2="8" y2="17"/>
            <polyline points="10 9 9 9 8 9"/>
          </svg>
          View Resume
        </a>
      </div>
    </nav>

    <div class="stage">
      <div class="nm-top-wrap">
        <div class="hi fi" style="--d:.1s;--x:-30px;--y:0px">Hi, I&apos;m</div>
        <h1 id="nameTop" class="nm hero-heading fi" style="--d:.15s;--x:0px;--y:40px">Tamizh</h1>
      </div>

      <div class="row">
        <aside class="side left glass fi" style="--d:.35s;--x:-40px;--y:0px">
          <div class="k">Role</div>
          <div class="v">Full-stack developer &amp; AI agent builder</div>
          <div class="chips"><span>PHP</span><span>Kotlin</span><span>Swift</span><span>Python</span></div>
        </aside>

        <div class="portrait-wrap fi" style="--d:.6s;--x:0px;--y:30px">
          <div class="photo">{{PORTRAIT_HTML}}</div>
          <span class="accent a1"></span>
          <span class="accent a2"></span>
          <span class="accent a3"></span>
          <span class="corner tl"></span>
          <span class="corner tr"></span>
          <span class="corner bl"></span>
          <span class="corner br"></span>
        </div>

        <aside class="side right glass fi" style="--d:.45s;--x:40px;--y:0px">
          <div class="stat"><div class="big">04</div><div class="k">Projects</div></div>
          <div class="stat"><div class="big">02</div><div class="k">Live apps</div></div>
          <div class="stat"><div class="big">8.04</div><div class="k">MCA CGPA</div></div>
        </aside>
      </div>

      <h2 id="nameBottom" class="nm nm-bot hero-heading fi" style="--d:.25s;--x:0px;--y:40px">Azhagan</h2>
    </div>

    <div class="bottom">
      <p class="tagline fi" style="--d:.35s;--x:0px;--y:20px">a full-stack developer building apis, mobile apps and ai agents</p>
      <div class="bottom-actions fi" style="--d:.5s;--x:0px;--y:20px">
        <a class="rbtn" href="{{RESUME_URL}}" target="_blank" rel="noopener">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/>
            <polyline points="7 10 12 15 17 10"/>
            <line x1="12" y1="15" x2="12" y2="3"/>
          </svg>
          Resume
        </a>
        <button class="cbtn" data-go="contact">Contact Me</button>
      </div>
    </div>
  </section>

  <!-- MARQUEE -->
  <section class="marquee" id="marquee">
    <div class="mrows">
      <div class="mrow" id="r1"></div>
      <div class="mrow" id="r2"></div>
    </div>
  </section>

  <!-- ABOUT -->
  <section class="about" id="about">
    <div class="about-inner">
      <div class="about-top">
        <h2 class="big-h hero-heading fi" style="--d:0s;--x:0px;--y:40px">About me</h2>
        <p class="about-text" id="aboutText"></p>
      </div>
      <div class="fi" style="--d:.2s;--x:0px;--y:20px"><button class="cbtn" data-go="contact">Contact Me</button></div>
    </div>
  </section>

  <!-- SKILLS -->
  <section class="skills" id="skills">
    <h2 class="big-h fi" style="--d:0s;--x:0px;--y:40px">Skills</h2>
    <div class="svc-list" id="svc"></div>
  </section>

  <!-- PROJECTS -->
  <section class="projects" id="projects">
    <h2 class="big-h hero-heading fi" style="--d:0s;--x:0px;--y:40px">Projects</h2>
    <div id="cards"></div>
  </section>

  <!-- CONTACT -->
  <section class="contact" id="contact">
    <h2 class="big-h hero-heading fi" style="--d:0s;--x:0px;--y:40px">Contact</h2>

    <div class="cgrid">
      <a class="ccard fi" href="mailto:{{EMAIL}}" style="--d:0s">
        <span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 6-10 7L2 6"/></svg></span>
        <div><small>Email</small><strong>{{EMAIL}}</strong></div>
      </a>
      <a class="ccard fi" href="{{PHONE_LINK}}" style="--d:.1s">
        <span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/></svg></span>
        <div><small>Phone</small><strong>{{PHONE}}</strong></div>
      </a>
      <a class="ccard fi" href="{{GITHUB_URL}}" target="_blank" rel="noopener" style="--d:.2s">
        <span class="ic"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/></svg></span>
        <div><small>GitHub</small><strong>github.com/Tamizh06-azhagan</strong></div>
      </a>
      <div class="ccard fi" style="--d:.3s">
        <span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></span>
        <div><small>Location</small><strong>Chennai, India</strong></div>
      </div>
    </div>

    <!-- ROBOT RUNNER GAME -->
    <div class="game">
      <div class="game-head">
        <h3>Robot Runner</h3>
        <div class="stats">
          <div class="stat-box">Score<b id="gScore">00000</b></div>
          <div class="stat-box">Coins<b id="gCoins">0</b></div>
          <div class="stat-box">Level<b id="gLevel">1</b></div>
          <div class="stat-box">Best<b id="gBest">00000</b></div>
        </div>
      </div>
      <div class="arena"><canvas id="game" tabindex="0"></canvas></div>
      <p class="hint">Space / tap to jump · ↓ to duck · collect coins for bonus points</p>
    </div>

    <div class="foot">© 2026 Tamizh Azhagan</div>
  </section>

</div>

<script>
const clamp = (v, a = 0, b = 1) => Math.min(b, Math.max(a, v));

const TICKET = "{{TICKET}}";
const HOME = "{{HOME}}";
const AXON = "{{AXON}}";

(function () {
  const bg = document.querySelector('.bgphoto');
  const ph = document.querySelector('.photo img');
  if (bg && ph) bg.src = ph.src;
})();

const ABOUT = "MCA graduate from Chennai with hands-on experience across the full stack. I build RESTful APIs with PHP and MySQL, mobile apps with Kotlin and Swift, and AI agents with Python, Streamlit and Ollama. I care most about flows that feel simple enough for anyone to finish.";

const SKILLS = [
  { n: '01', name: 'AI Agents & Data', d: 'Python, Pandas, data visualization, dataset-driven chatbots and AI agents running on Ollama.' },
  { n: '02', name: 'Mobile Development', d: 'Cross-platform apps for Android and iOS with Kotlin and Swift, including real-time matching and booking flows.' },
  { n: '03', name: 'Frontend Development', d: 'JavaScript, HTML, CSS and responsive web design, built to work across screen sizes.' },
  { n: '04', name: 'Backend Development', d: 'PHP, REST API design, server-side architecture, authentication and authorization, MySQL databases.' }
];

const DRIVER_ROUTE = "{{DRIVER_ROUTE}}";
const DRIVER_DRIVER = "{{DRIVER_DRIVER}}";
const DRIVER_USER = "{{DRIVER_USER}}";
const FOOD_LOGIN = "{{FOOD_LOGIN}}";
const FOOD_ORPHANAGE = "{{FOOD_ORPHANAGE}}";
const FOOD_DONATION = "{{FOOD_DONATION}}";
const FOOD_ACTIVITY = "{{FOOD_ACTIVITY}}";

const PROJECTS = [
  {
    n: '01', cat: 'AI Agent · Sep–Oct 2026', name: 'Cineverse',
    live: 'https://ciniverse-ai-agent.streamlit.app/',
    imgs: [TICKET, HOME],
    bullets: [
      'Turns a simple chat message, such as a movie name, into a guided ticket-booking flow.',
      'Finds movie details, checks showtimes and seat availability, and calculates ticket prices.',
      'Ends with a tiltable e-ticket that downloads as a PNG.'
    ],
    stack: ['Python', 'Streamlit', 'SQLite', 'Ollama']
  },
  {
    n: '02', cat: 'Mental Health Support · Chatbot', name: 'Axon',
    live: 'https://axon-chatbot.streamlit.app/',
    imgs: [AXON],
    bullets: [
      'A calm, private space to talk through feelings by text or voice, without judgment.',
      'Replies come from a locally hosted language model, grounded in a mental health knowledge dataset.',
      'Google sign-in, chat history, optional mood check-ins and voice transcription.',
      'A supportive tool, not a replacement for professional care, diagnosis or emergency services.'
    ],
    stack: ['Local LLM', 'Google Sign-in', 'Voice Transcription', 'Mood Check-ins']
  },
  {
    n: '03', cat: 'Mobile + Backend · Dec 2024–Jun 2025', name: 'Driver Sync',
    live: null, grid: 'phones',
    imgs: [DRIVER_ROUTE, DRIVER_DRIVER, DRIVER_USER],
    bullets: [
      'Cross-platform iOS and Android app for real-time driver and user matching.',
      'PHP API handling driver availability updates, request matching and the full booking lifecycle.'
    ],
    stack: ['Kotlin', 'Swift', 'PHP', 'MySQL']
  },
  {
    n: '04', cat: 'Full-Stack · Internship, Sep 2025–Feb 2026', name: 'Food Serve',
    live: null, status: 'In testing on Netlify', grid: 'web',
    imgs: [FOOD_LOGIN, FOOD_ORPHANAGE, FOOD_DONATION, FOOD_ACTIVITY],
    bullets: [
      'Donation platform connecting food donors with orphanages, built during my internship at Oneyes Infotech.',
      'RESTful PHP and MySQL backend for donor registration, food inventory and orphanage matching.'
    ],
    stack: ['JavaScript', 'HTML5', 'CSS3', 'PHP', 'MySQL', 'Netlify']
  }
];

const ALL_SHOTS = [
  TICKET, HOME, AXON,
  DRIVER_ROUTE, DRIVER_DRIVER, DRIVER_USER,
  FOOD_LOGIN, FOOD_ORPHANAGE, FOOD_DONATION, FOOD_ACTIVITY
].filter(Boolean);
const SHOTS = [...new Set(ALL_SHOTS)];
const mkRow = list => [...list, ...list].map(s => `<img src="${s}" alt="Project screenshot" loading="lazy">`).join('');
document.getElementById('r1').innerHTML = mkRow(SHOTS);
document.getElementById('r2').innerHTML = mkRow([...SHOTS].reverse());

document.getElementById('svc').innerHTML = SKILLS.map((s, i) => `
  <div class="svc fi" style="--d:${(i * 0.1).toFixed(1)}s;--x:0px;--y:30px">
    <span class="n">${s.n}</span>
    <div><h3>${s.name}</h3><p>${s.d}</p></div>
  </div>`).join('');

document.getElementById('cards').innerHTML = PROJECTS.map((p, i) => {
  const imgs = (p.imgs || []).filter(Boolean);
  const gridCls = p.grid || (imgs.length === 1 ? 'one' : (imgs.length >= 2 ? 'two' : ''));
  const media = imgs.length
    ? `<div class="pgrid ${gridCls}">${imgs.map(s => `<img src="${s}" alt="${p.name} screenshot" loading="lazy">`).join('')}</div>`
    : '';
  const action = p.live
    ? `<a class="lbtn" href="${p.live}" target="_blank" rel="noopener">Live Project ↗</a>`
    : `<span class="lbtn off">${p.status || 'Private project'}</span>`;
  return `
  <div class="pwrap">
    <div class="pcard" style="top:${96 + i * 28}px">
      <div class="phead">
        <div class="ptitle">
          <span class="pn">${p.n}</span>
          <div class="pmeta"><span class="pcat">${p.cat}</span><h3 class="pname">${p.name}</h3></div>
        </div>
        ${action}
      </div>
      <div class="pbody ${media ? 'has-media' : ''}">
        ${media}
        <div class="pdetail">
          <ul>${p.bullets.map(b => `<li>${b}</li>`).join('')}</ul>
          <div class="tags">${p.stack.map(t => `<span>${t}</span>`).join('')}</div>
        </div>
      </div>
    </div>
  </div>`;
}).join('');

const aboutEl = document.getElementById('aboutText');
aboutEl.innerHTML = ABOUT.split(' ').map(w =>
  `<span style="display:inline-block;white-space:nowrap">${[...w].map(c => `<span class="ch">${c}</span>`).join('')}</span>`
).join(' ');
const chEls = [...aboutEl.querySelectorAll('.ch')];

const nameTop = document.getElementById('nameTop');
const nameBottom = document.getElementById('nameBottom');
function fitText(el) {
  el.style.fontSize = '';
  let fs = parseFloat(getComputedStyle(el).fontSize);
  while (el.scrollWidth > el.clientWidth && fs > 14) {
    fs -= 1;
    el.style.fontSize = fs + 'px';
  }
}
function fitAll() { fitText(nameTop); fitText(nameBottom); }
document.fonts && document.fonts.ready.then(fitAll);
window.addEventListener('resize', fitAll);
fitAll();

document.querySelectorAll('[data-go]').forEach(el => {
  el.addEventListener('click', e => {
    e.preventDefault();
    const target = document.getElementById(el.dataset.go);
    if (target) target.scrollIntoView({ behavior: 'smooth', block: 'start' });
  });
});

const io = new IntersectionObserver(entries => {
  entries.forEach(e => {
    if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
  });
}, { rootMargin: '0px 0px 50px 0px' });
document.querySelectorAll('.fi').forEach(el => io.observe(el));

const mq = document.getElementById('marquee');
const r1 = document.getElementById('r1');
const r2 = document.getElementById('r2');
const cards = [...document.querySelectorAll('.pcard')];

function updateMarquee() {
  const r = mq.getBoundingClientRect();
  const off = (-r.top + innerHeight) * 0.3;
  r1.style.transform = `translateX(${off - 200}px)`;
  r2.style.transform = `translateX(-${off - 200}px)`;
}

function updateText() {
  const vh = innerHeight;
  const r = aboutEl.getBoundingClientRect();
  const prog = clamp((0.8 * vh - r.top) / (r.height + 0.6 * vh));
  const total = chEls.length;
  chEls.forEach((c, i) => {
    const s = i / total, e = (i + 1) / total;
    c.style.opacity = 0.2 + 0.8 * clamp((prog - s) / (e - s));
  });
}

function updateCards() {
  cards.forEach((c, i) => {
    const r = c.parentElement.getBoundingClientRect();
    const prog = clamp(-r.top / r.height);
    const target = 1 - (cards.length - 1 - i) * 0.03;
    c.style.transform = `scale(${1 - prog * (1 - target)})`;
  });
}

function updateAll() { updateMarquee(); updateText(); updateCards(); }
window.addEventListener('scroll', updateAll, { passive: true });
window.addEventListener('resize', updateAll);
updateAll();

/* ================= ROBOT RUNNER ================= */
const cv = document.getElementById('game');
const ctx = cv.getContext('2d');
const hud = {
  score: document.getElementById('gScore'),
  coins: document.getElementById('gCoins'),
  level: document.getElementById('gLevel'),
  best: document.getElementById('gBest')
};

const GROUND_PAD = 36;
const GRAV = 0.62;
const JUMP = -11.8;
let W = 600, H = 240, DPR = 1;
let gameVisible = false;
let best = 0;
try { best = parseInt(localStorage.getItem('tp-robot-best') || '0', 10) || 0; } catch (e) {}

let stars = [];
function resize() {
  DPR = window.devicePixelRatio || 1;
  const r = cv.getBoundingClientRect();
  W = r.width; H = r.height;
  cv.width = Math.round(W * DPR);
  cv.height = Math.round(H * DPR);
  ctx.setTransform(DPR, 0, 0, DPR, 0, 0);
  stars = Array.from({ length: 36 }, () => ({
    x: Math.random() * W, y: Math.random() * (H - 80), s: 0.2 + Math.random() * 0.8
  }));
}
const groundY = () => H - GROUND_PAD;

function newState() {
  return {
    running: false, over: false, t: 0,
    speed: 6, dist: 0, coins: 0, score: 0, level: 1,
    nextObs: 80, nextCoin: 40,
    robot: { x: 60, y: 0, vy: 0, onGround: true, ducking: false, legT: 0 },
    obs: [], coinList: [], particles: []
  };
}
let S = newState();

function start() { S = newState(); S.running = true; }

function jump() {
  if (S.over || !S.running) { start(); return; }
  const r = S.robot;
  if (r.onGround) { r.vy = JUMP; r.onGround = false; }
}

function spawnObstacle() {
  const gy = groundY();
  if (Math.random() < 0.35) {
    S.obs.push({ type: 'drone', x: W + 20, w: 40, h: 22, y: gy - 58 });
  } else {
    const w = 26 + (Math.random() < 0.4 ? 16 : 0);
    S.obs.push({ type: 'spike', x: W + 20, w, h: 34, y: gy - 34 });
  }
}

function spawnCoins() {
  const gy = groundY();
  const n = 3 + Math.floor(Math.random() * 3);
  const baseY = gy - (50 + Math.random() * 50);
  for (let i = 0; i < n; i++) {
    const arc = Math.sin((i / Math.max(1, n - 1)) * Math.PI) * 22;
    S.coinList.push({ x: W + 20 + i * 26, y: baseY - arc, got: false });
  }
}

function robotRect() {
  const r = S.robot;
  const h = r.ducking ? 24 : 44;
  const w = r.ducking ? 44 : 34;
  const bottom = groundY() + r.y;
  return { x: r.x + 4, y: bottom - h + 4, w: w - 8, h: h - 8 };
}

function rectHit(a, b) {
  return a.x < b.x + b.w && a.x + a.w > b.x && a.y < b.y + b.h && a.y + a.h > b.y;
}

function gameOver() {
  S.over = true;
  if (S.score > best) {
    best = S.score;
    try { localStorage.setItem('tp-robot-best', String(best)); } catch (e) {}
  }
}

function update() {
  if (!S.running || S.over || !gameVisible) return;
  S.t++;
  S.speed = Math.min(15, 6 + S.dist / 1000);
  S.dist += S.speed;
  S.level = 1 + Math.floor(S.dist / 1500);

  const r = S.robot;
  r.legT += S.speed * 0.12;
  r.vy += GRAV + (r.ducking && !r.onGround ? 0.9 : 0);
  r.y += r.vy;
  if (r.y >= 0) { r.y = 0; r.vy = 0; r.onGround = true; }

  if (--S.nextObs <= 0) { spawnObstacle(); S.nextObs = 55 + Math.random() * 55 - S.speed * 1.5; }
  if (--S.nextCoin <= 0) { spawnCoins(); S.nextCoin = 70 + Math.random() * 60; }

  S.obs.forEach(o => o.x -= S.speed);
  S.coinList.forEach(c => c.x -= S.speed);

  const rr = robotRect();
  const cx = rr.x + rr.w / 2, cy = rr.y + rr.h / 2;
  S.coinList.forEach(c => {
    if (!c.got && Math.hypot(c.x - cx, c.y - cy) < 22) {
      c.got = true;
      S.coins++;
      S.particles.push({ x: c.x, y: c.y, life: 20 });
    }
  });

  for (const o of S.obs) {
    const box = o.type === 'drone'
      ? { x: o.x + 4, y: o.y + 4, w: o.w - 8, h: o.h - 8 }
      : { x: o.x + 4, y: o.y + 2, w: o.w - 8, h: o.h - 2 };
    if (rectHit(rr, box)) { gameOver(); return; }
  }

  S.obs = S.obs.filter(o => o.x + o.w > -10);
  S.coinList = S.coinList.filter(c => c.x > -20 && !c.got);
  S.particles.forEach(p => p.life--);
  S.particles = S.particles.filter(p => p.life > 0);
  S.score = Math.floor(S.dist / 10) + S.coins * 5;

  stars.forEach(s => {
    s.x -= s.s * 0.6;
    if (s.x < 0) { s.x = W; s.y = Math.random() * (H - 80); }
  });
}

function drawRobot() {
  const r = S.robot;
  const x = r.x;
  const bottom = groundY() + r.y;
  const body = '#D7E2EA', dark = '#262a36', eye = '#4DE1FF', red = '#ff4d5e';

  if (r.ducking) {
    ctx.fillStyle = body; ctx.fillRect(x, bottom - 24, 44, 18);
    ctx.fillStyle = eye; ctx.fillRect(x + 34, bottom - 18, 6, 4);
    ctx.fillStyle = dark; ctx.fillRect(x + 6, bottom - 6, 8, 6); ctx.fillRect(x + 30, bottom - 6, 8, 6);
    return;
  }

  const swing = r.onGround ? Math.sin(r.legT) * 4 : 0;
  ctx.fillStyle = dark;
  ctx.fillRect(x + 6, bottom - 10, 6, 10 + swing);
  ctx.fillRect(x + 22, bottom - 10, 6, 10 - swing);

  ctx.fillStyle = body;
  ctx.fillRect(x, bottom - 38, 34, 28);
  ctx.fillRect(x + 4, bottom - 44, 26, 10);

  ctx.fillStyle = eye; ctx.fillRect(x + 10, bottom - 42, 14, 4);
  ctx.fillStyle = red; ctx.fillRect(x + 14, bottom - 30, 6, 6);

  ctx.fillStyle = body; ctx.fillRect(x + 16, bottom - 50, 2, 6);
  ctx.fillStyle = red; ctx.beginPath(); ctx.arc(x + 17, bottom - 51, 3, 0, Math.PI * 2); ctx.fill();
}

function draw() {
  ctx.clearRect(0, 0, W, H);

  ctx.fillStyle = 'rgba(215,226,234,0.5)';
  stars.forEach(s => { ctx.globalAlpha = 0.25 + s.s * 0.5; ctx.fillRect(s.x, s.y, 2, 2); });
  ctx.globalAlpha = 1;

  const gy = groundY();
  ctx.fillStyle = '#262a36'; ctx.fillRect(0, gy, W, 2);
  ctx.fillStyle = '#3a3f4c';
  const off = S.dist % 40;
  for (let x = -off; x < W; x += 40) ctx.fillRect(x, gy + 8, 16, 2);

  S.obs.forEach(o => {
    if (o.type === 'spike') {
      ctx.fillStyle = '#ff4d5e';
      ctx.beginPath();
      ctx.moveTo(o.x, gy); ctx.lineTo(o.x + o.w / 2, o.y); ctx.lineTo(o.x + o.w, gy);
      ctx.closePath(); ctx.fill();
    } else {
      ctx.fillStyle = '#9b86ff';
      ctx.fillRect(o.x, o.y, o.w, o.h);
      ctx.fillStyle = '#0C0C0C'; ctx.fillRect(o.x + 6, o.y + 7, o.w - 12, 4);
      ctx.fillStyle = '#D7E2EA';
      ctx.fillRect(o.x - 4, o.y - 3, o.w + 8, (S.t % 6 < 3) ? 2 : 4);
    }
  });

  S.coinList.forEach(c => {
    const pulse = 1 + Math.sin(S.t * 0.2 + c.x) * 0.08;
    ctx.beginPath(); ctx.arc(c.x, c.y, 9 * pulse, 0, Math.PI * 2);
    ctx.fillStyle = '#FFD60A'; ctx.fill();
    ctx.beginPath(); ctx.arc(c.x, c.y, 5 * pulse, 0, Math.PI * 2);
    ctx.strokeStyle = '#B88A00'; ctx.lineWidth = 2; ctx.stroke();
  });

  S.particles.forEach(p => {
    ctx.globalAlpha = p.life / 20;
    ctx.strokeStyle = '#FFD60A';
    ctx.beginPath(); ctx.arc(p.x, p.y, (20 - p.life) * 0.8 + 6, 0, Math.PI * 2); ctx.stroke();
  });
  ctx.globalAlpha = 1;

  drawRobot();

  if (!S.running || S.over) {
    ctx.fillStyle = 'rgba(12,12,12,0.6)';
    ctx.fillRect(0, 0, W, H);
    ctx.fillStyle = '#D7E2EA';
    ctx.textAlign = 'center';
    ctx.font = '700 22px Kanit, sans-serif';
    ctx.fillText(S.over ? 'GAME OVER' : 'ROBOT RUNNER', W / 2, H / 2 - 12);
    ctx.font = '400 14px Kanit, sans-serif';
    ctx.fillText(
      S.over
        ? `Score ${S.score} · Coins ${S.coins} · Space or tap to retry`
        : 'Space or tap to start · ↓ to duck · collect coins',
      W / 2, H / 2 + 14
    );
    ctx.textAlign = 'left';
  }
}

function syncHud() {
  hud.score.textContent = String(S.score).padStart(5, '0');
  hud.coins.textContent = String(S.coins);
  hud.level.textContent = String(S.level);
  hud.best.textContent = String(Math.max(best, S.score)).padStart(5, '0');
}

function loop() {
  if (gameVisible) {
    update();
    draw();
    syncHud();
  }
  requestAnimationFrame(loop);
}

new IntersectionObserver(([en]) => {
  gameVisible = en.isIntersecting && en.intersectionRatio >= 0.5;
}, { threshold: [0, 0.5, 1] }).observe(cv);

window.addEventListener('keydown', e => {
  if (!gameVisible) return;
  if (e.code === 'Space' || e.code === 'ArrowUp') {
    e.preventDefault();
    if (!e.repeat) jump();
  }
  if (e.code === 'ArrowDown') {
    e.preventDefault();
    S.robot.ducking = true;
  }
});
window.addEventListener('keyup', e => {
  if (e.code === 'ArrowDown') S.robot.ducking = false;
});
cv.addEventListener('pointerdown', e => { e.preventDefault(); jump(); });

window.addEventListener('resize', resize);
resize();
loop();
</script>
</body>
</html>
"""

PLACEHOLDERS = {
    "{{BG_HTML}}": bg_html,
    "{{PORTRAIT_HTML}}": portrait_html,
    "{{GITHUB_URL}}": GITHUB_URL,
    "{{EMAIL}}": EMAIL,
    "{{PHONE_LINK}}": PHONE_LINK,
    "{{PHONE}}": PHONE,
    "{{RESUME_URL}}": RESUME_URL,
    "{{TICKET}}": TICKET,
    "{{HOME}}": HOME,
    "{{AXON}}": AXON,
    "{{DRIVER_ROUTE}}": DRIVER_ROUTE,
    "{{DRIVER_DRIVER}}": DRIVER_DRIVER,
    "{{DRIVER_USER}}": DRIVER_USER,
    "{{FOOD_ORPHANAGE}}": FOOD_ORPHANAGE,
    "{{FOOD_ACTIVITY}}": FOOD_ACTIVITY,
    "{{FOOD_DONATION}}": FOOD_DONATION,
    "{{FOOD_LOGIN}}": FOOD_LOGIN,
}

for key, value in PLACEHOLDERS.items():
    HTML = HTML.replace(key, value)

components.html(HTML, height=FRAME_HEIGHT, scrolling=True)