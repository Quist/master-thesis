all:
	make clean && pdflatex thesis.tex && biber thesis && pdflatex thesis.tex && pdflatex thesis.tex
clean:
	rm -f *.aux *.bcf *.lof *.log *.lot *.run.xml *.toc *-blx.bib *.bbl *.blg
