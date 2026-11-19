# make          PDF nach build/main.pdf
# make pages    Seitenzahl ausgeben
# make check    schlägt fehl, solange noch ein \TODO im PDF steht
# make clean    build/ löschen

MAIN    := main
LATEXMK := latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build
PDF     := build/$(MAIN).pdf

.PHONY: pdf pages check clean

pdf:
	$(LATEXMK) $(MAIN).tex

pages: pdf
	@pdfinfo $(PDF) | grep '^Pages:'

check: pdf
	@pdftotext $(PDF) - | grep -n 'TODO' \
	  && { echo "check: TODO-Platzhalter im PDF gefunden"; exit 1; } || true
	@echo "check: OK"

clean:
	rm -rf build
