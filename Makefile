LATEXMK=latexmk
LATEXMKOPT=-pdf

MAIN=arikahn_cv
BIBFILE=publications.bib
ANNOT_BIBFILE=publications_annotated.bib

all:	$(MAIN).pdf

$(MAIN).pdf: $(MAIN).tex $(ANNOT_BIBFILE)
	$(LATEXMK) $(LATEXMKOPT) $(MAIN)


$(ANNOT_BIBFILE): $(BIBFILE)
	python annotate_bibfile.py $(BIBFILE) $(ANNOT_BIBFILE)

clean:
	$(LATEXMK) -C $(MAIN)

.PHONY: clean all