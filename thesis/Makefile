
thesis:
	pdflatex thesis.tex && makeglossaries thesis.acn && biber thesis && pdflatex thesis.tex && pdflatex thesis.tex

all: clean results thesis

results:
	$(MAKE) -C ../results/function_tests/rest
clean:
	rm -f *.aux *.bcf *.lof *.log *.lot *.run.xml *.toc *-blx.bib *.bbl *.blg *.glo
