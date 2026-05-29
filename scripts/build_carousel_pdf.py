from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
IMG_DIR = ROOT / "carousel" / "images"
OUT = ROOT / "dist" / "FinOps_Confidence_Constrained_Carousel_A4_HighRes.pdf"

images = []
for path in sorted(IMG_DIR.glob("slide_*_A4_300dpi.jpg")):
    img = Image.open(path).convert("RGB")
    images.append(img)

if not images:
    raise SystemExit("No carousel images found.")

OUT.parent.mkdir(parents=True, exist_ok=True)
first, rest = images[0], images[1:]
first.save(OUT, save_all=True, append_images=rest, resolution=300.0, quality=95)
print(f"Wrote {OUT} ({len(images)} pages)")
