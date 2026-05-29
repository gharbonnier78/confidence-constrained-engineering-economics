from pathlib import Path
from pypdf import PdfReader, PdfWriter

ROOT = Path(__file__).resolve().parents[1]
CAROUSEL = ROOT / "dist" / "FinOps_Confidence_Constrained_Carousel_A4_HighRes.pdf"
ARTICLE = ROOT / "dist" / "Confidence_Constrained_Engineering_Economics_arxiv.pdf"
OUT = ROOT / "dist" / "Carousel_then_Confidence_Constrained_Engineering_Economics.pdf"

writer = PdfWriter()
for pdf in [CAROUSEL, ARTICLE]:
    reader = PdfReader(str(pdf))
    for page in reader.pages:
        writer.add_page(page)

with OUT.open("wb") as f:
    writer.write(f)

print(f"Wrote {OUT} ({len(writer.pages)} pages)")
