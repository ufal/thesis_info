.PHONY: all
all: thesis.html

thesis.html: thesis.md $(wildcard scripts/*)
	scripts/markdown $< >$@

.PHONY: clean
clean:
	rm -r thesis.html
