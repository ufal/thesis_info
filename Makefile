.PHONY: all
all: thesis.html thesis-standalone.html

thesis.html: thesis.md $(wildcard scripts/*)
	cat $< | scripts/pre | scripts/markdown | scripts/post >$@

thesis-standalone.html: thesis.html scripts/standalone
	scripts/standalone <$< >$@

.PHONY: clean
clean:
	rm -r thesis.html thesis-standalone.html
