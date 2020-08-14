# Copyright (C) 2020 Andrew Trettel
#
# Licensed under the MIT License.  See LICENSE.txt for additional details.

index=example
latex_compiler=pdflatex
bib_compiler=biber

python_targets := $(patsubst %.py,%.tmp,$(wildcard */*.py))

tex_dependencies = $(wildcard *.tex) $(wildcard */*.tex)

$(index).pdf: $(python_targets) $(index).bcf $(tex_dependencies)
	$(latex_compiler) $(index).tex
	$(latex_compiler) $(index).tex

$(index).bcf: $(index).bib
	$(latex_compiler) $(index).tex
	$(bib_compiler) $(index)
	$(latex_compiler) $(index).tex
	$(bib_compiler) $(index)
	$(latex_compiler) $(index).tex

%.tmp:: %.py
	PYTHONPATH=$(PYTHONPATH):`pwd` python3 -B $^
	-sed -i "s/\\\\sffamily\\\\fontsize{.*}{.*}\\\\selectfont //g" */*.pgf
	-sed -i "s/use as bounding box, clip/use as bounding box/g" */*.pgf
	@touch $@

.PHONY: clean
clean:
	-rm -frv *-blx.bib
	-rm -frv *.aux
	-rm -frv *.bak
	-rm -frv *.bbl
	-rm -frv *.bcf
	-rm -frv *.blg
	-rm -frv *.end
	-rm -frv *.lof
	-rm -frv *.log
	-rm -frv *.lot
	-rm -frv *.out
	-rm -frv *.pdf
	-rm -frv *.pgf */*.pgf
	-rm -frv *.run.xml
	-rm -frv *.tmp */*.tmp
	-rm -frv *.toc
	-rm -frv *.xwm
	-rm -frv *Notes.bib

.PHONY: spellcheck
spellcheck:
	find ./ -iname "*.tex" -exec aspell --lang=en-US --mode=tex --tex-check-comments --dont-backup check "{}" \;
