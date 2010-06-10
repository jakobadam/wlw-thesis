:: build latex
:: quick build if no argument given

IF [%1] == [] (
        pdflatex thesis.tex
)

IF [%1] == [b] (
        pdflatex thesis.tex
        makeindex thesis.glo -s thesis.ist -t thesis.glg -o thesis.gls        
        bibtex thesis   
        pdflatex thesis.tex
        pdflatex thesis.tex
)

IF [%1] == [clean] (
        del thesis.aux
        del thesis.out
        del thesis.toc
        del thesis.log
        del thesis.bbl
        del thesis.blg
        del thesis.ist
        del thesis.glg
        del thesis.glo
        del thesis.gls
        del thesis.pdf
        
)
