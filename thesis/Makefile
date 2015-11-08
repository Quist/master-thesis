all:
	make clean && pdflatex thesis.tex && makeglossaries thesis.acn && biber thesis && pdflatex thesis.tex && pdflatex thesis.tex
clean:
	rm -f *.aux *.bcf *.lof *.log *.lot *.run.xml *.toc *-blx.bib *.bbl *.blg *.glo
