"""Build the reference gallery page for one video.

Usage: python tools/make_gallery.py videos/<name> <out-dir>

Reads the "Reference images" table in the video's bible.md (file | plain name | what it is for).
Images in refs/ and shots/ that are not in the table get a name made from their file name.
Writes <out-dir>/index.html, <out-dir>/img/<file> (full size) and <out-dir>/thumb/<file>.
Publish index.html as an Artifact with everything in img/ and thumb/ as files.
"""
import html, re, shutil, sys
from pathlib import Path
from PIL import Image

video = Path(sys.argv[1]); out = Path(sys.argv[2])
(out / "img").mkdir(parents=True, exist_ok=True); (out / "thumb").mkdir(exist_ok=True)
bible = (video / "bible.md").read_text(encoding="utf-8")
title = re.search(r"^# Video bible: (.+)$", bible, re.M)
title = title.group(1).strip() if title else video.name

table = {}
m = re.search(r"^## Reference images\n(.*?)(?=^## )", bible, re.M | re.S)
if m:
    for line in m.group(1).splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 3 and cells[0].startswith("`"):
            table[cells[0].strip("`")] = (cells[1], cells[2])

def group(rel):
    n = Path(rel).stem
    if rel.startswith("shots/"): return "Approved shots"
    if n.startswith("prop-"): return "Props"
    if n.startswith(("band-", "stage-")): return "Band"
    if n.startswith("plate-"): return "Camera angles"
    if n.endswith(("-sheet", "-source")) or "inspiration" in n: return "Characters and inspiration"
    if n == "style-pick": return "Look"
    return "Locations"

ORDER = ["Look", "Characters and inspiration", "Props", "Locations", "Camera angles", "Band", "Approved shots"]
items = []
for sub in ("refs", "shots"):
    for f in sorted((video / sub).glob("*")):
        if f.suffix.lower() not in (".jpg", ".jpeg", ".png", ".webp"): continue
        rel = f"{sub}/{f.name}"
        name, use = table.get(rel, (None, ""))
        if not name:
            stem = re.sub(r"^(prop|plate)-", "", f.stem).replace("-", " ")
            name = stem[:1].upper() + stem[1:]
            if sub == "shots": name = "Shot " + f.stem
        key = f"{sub}-{f.name}"
        shutil.copy(f, out / "img" / key)
        im = Image.open(f).convert("RGB"); im.thumbnail((640, 640)); im.save(out / "thumb" / (Path(key).stem + ".jpg"), quality=80)
        items.append((group(rel), name, use, key, Path(key).stem + ".jpg"))

sections = []
for g in ORDER:
    cards = [i for i in items if i[0] == g]
    if not cards: continue
    cs = "".join(
        f'<figure class="card"><button class="pic" data-full="img/{html.escape(k)}" data-name="{html.escape(n)}" aria-label="Show {html.escape(n)} full size">'
        f'<img src="thumb/{html.escape(t)}" alt="{html.escape(n)}" loading="lazy"></button>'
        f'<figcaption><span class="name">{html.escape(n)}</span>'
        + (f'<span class="use">{html.escape(u)}</span>' if u else "")
        + f'<span class="file">{html.escape(k.split("-",1)[1])}</span></figcaption></figure>'
        for _, n, u, k, t in cards)
    sections.append(f'<section><h2>{g} <span class="count">{len(cards)}</span></h2><div class="grid">{cs}</div></section>')

page = f"""<title>{html.escape(title)} references</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Space+Grotesk:wght@500;600&display=swap">
<style>
/* Contact sheet: dark-room neutrals, thumbnails on a loose grid, names under each print */
:root {{ --bg:#f3f2ef; --card:#ffffff; --fg:#1d1c1a; --muted:#6b675f; --line:#dcd8d0; --accent:#9b3d2c;
  --display:"Space Grotesk",system-ui,sans-serif; --body:"Inter",system-ui,sans-serif; }}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{ --bg:#161513; --card:#201f1c; --fg:#ece9e2; --muted:#a39e94; --line:#34322d; --accent:#e07a62; color-scheme:dark }} }}
:root[data-theme="dark"] {{ --bg:#161513; --card:#201f1c; --fg:#ece9e2; --muted:#a39e94; --line:#34322d; --accent:#e07a62; color-scheme:dark }}
body {{ background:var(--bg); color:var(--fg); font-family:var(--body); line-height:1.5;
  padding-left:max(16px,env(safe-area-inset-left,0px)); padding-right:max(16px,env(safe-area-inset-right,0px)); padding-block:24px 48px }}
.wrap {{ max-width:1200px; margin:0 auto; display:flex; flex-direction:column; gap:32px }}
h1 {{ font-family:var(--display); font-size:1.9rem; margin:0; text-wrap:balance }}
.lead {{ color:var(--muted); margin:6px 0 0; max-width:65ch }}
h2 {{ font-family:var(--display); font-size:1.15rem; margin:0 0 12px; display:flex; gap:8px; align-items:baseline }}
.count {{ font-family:var(--body); font-size:.8rem; color:var(--muted); font-weight:500 }}
.grid {{ display:grid; grid-template-columns:repeat(auto-fill,minmax(220px,1fr)); gap:16px }}
.card {{ margin:0; background:var(--card); border:1px solid var(--line); border-radius:6px; overflow:hidden; display:flex; flex-direction:column; min-width:0 }}
.pic {{ border:0; padding:0; background:#000; cursor:zoom-in; display:block; aspect-ratio:16/9 }}
.pic img {{ width:100%; height:100%; object-fit:cover; display:block }}
.pic:focus-visible {{ outline:3px solid var(--accent); outline-offset:-3px }}
figcaption {{ padding:10px 12px 12px; display:flex; flex-direction:column; gap:2px; min-width:0 }}
.name {{ font-weight:600 }}
.use {{ color:var(--muted); font-size:.85rem }}
.file {{ color:var(--muted); font-size:.75rem; overflow-wrap:anywhere }}
#view {{ position:fixed; inset:0; background:rgba(0,0,0,.92); display:flex; flex-direction:column; align-items:center; justify-content:center; gap:12px; padding:16px; z-index:20 }}
#view img {{ max-height:82vh; max-width:100%; object-fit:contain }}
#view p {{ color:#eee; margin:0; text-align:center }}
#view button {{ font:inherit; background:#eee; color:#111; border:0; border-radius:4px; padding:6px 14px; cursor:pointer }}
</style>
<div class="wrap">
<header><h1>{html.escape(title)}: reference images</h1>
<p class="lead">Every approved picture for this video, under the name the prompts use. Click a picture to see it full size, then right-click it (or press and hold on a phone) and choose Save image.</p></header>
{''.join(sections)}
</div>
<div id="view" hidden><img alt=""><p></p><button type="button">Close</button></div>
<script>
const v=document.getElementById('view'),vi=v.querySelector('img'),vp=v.querySelector('p');
document.querySelectorAll('.pic').forEach(b=>b.addEventListener('click',()=>{{vi.src=b.dataset.full;vi.alt=b.dataset.name;vp.textContent=b.dataset.name;v.hidden=false;v.querySelector('button').focus()}}));
const close=()=>{{v.hidden=true;vi.src=''}};
v.querySelector('button').addEventListener('click',close);
v.addEventListener('click',e=>{{if(e.target===v)close()}});
document.addEventListener('keydown',e=>{{if(e.key==='Escape'&&!v.hidden)close()}});
</script>
"""
(out / "index.html").write_text(page, encoding="utf-8")
print(len(items), "images")
