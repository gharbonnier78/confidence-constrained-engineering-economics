PDF=Confidence_Constrained_Engineering_Economics.pdf
TEX=Confidence_Constrained_Engineering_Economics.tex

all: $(PDF)

$(PDF): $(TEX)
	latexmk -xelatex -interaction=nonstopmode -halt-on-error $(TEX)

clean:
	latexmk -C
	rm -f *.bbl *.run.xml *.bcf *.out *.toc *.synctex.gz
