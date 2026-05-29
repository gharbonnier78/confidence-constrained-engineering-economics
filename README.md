# Confidence-Constrained Engineering Economics

**A Bayesian Decision Framework for Architecture, Deployment, Security, Sovereignty, and AI Inference**

This repository contains a foundation article and LinkedIn carousel package around the idea that modern engineering economics is not only about minimizing cost, but about choosing the minimum cost that buys defensible confidence under uncertainty.

The article is intentionally **STRAT-Q agnostic**. It establishes a generic engineering economics and Bayesian trade-off foundation that can later be reinforced by a separate STRAT-Q companion document.

<p align="center">
  <a href="./dist/Confidence_Constrained_Engineering_Economics_arxiv.pdf">
    <img src="https://img.shields.io/badge/Open-Article-0B5FFF?style=for-the-badge&logo=adobeacrobatreader&logoColor=white" alt="Open PDF">
  </a>
</p>

## Core idea

FinOps tells engineering what technology costs. Confidence-constrained engineering economics asks what that cost buys in terms of evidence, margin protection, residual risk reduction, security exposure, sovereignty exposure, delivery flow, and AI inference independence.

The decision problem is not simply:

> What is the cheapest architecture?

It is:

> What is the minimum cost that buys a defensible level of confidence?

## Repository structure

```text
.
├── article/        # Markdown, LaTeX and Pandoc sources for the arXiv-style paper
├── carousel/       # 10 high-resolution A4 carousel slides as images
├── dist/           # Generated PDFs ready to share
├── docs/           # LinkedIn post and carousel generation prompt
├── references/     # Public reference PDFs used as background sources
└── scripts/        # Helper scripts to rebuild carousel and merged PDFs
```

## Main deliverables

- `dist/Confidence_Constrained_Engineering_Economics_arxiv.pdf`  
  The arXiv-style foundation article.

- `dist/FinOps_Confidence_Constrained_Carousel_A4_HighRes.pdf`  
  The 10-page high-resolution A4 carousel PDF.

- `dist/Carousel_then_Confidence_Constrained_Engineering_Economics.pdf`  
  Combined PDF with the carousel first, then the article.

## Rebuild

Install minimal Python dependencies:

```bash
pip install -r requirements.txt
```

Rebuild the carousel PDF and merged PDF:

```bash
python scripts/build_carousel_pdf.py
python scripts/concat_pdfs.py
```

Rebuild the article from LaTeX/Pandoc sources using the `article/Makefile` if your environment has a LaTeX distribution and Pandoc installed.

## Publication strategy

1. Use this repository as the **generic foundation article**.
2. Keep this article independent from any branded method or framework.
3. Build a separate companion document showing how a governance system can operationalize the model through evidence graphs, risk gates, MTPs, rule engines, dashboards, and decision workflows.

## Licensing

No open-source license has been selected yet. Until a license is added, all rights are reserved by default.
