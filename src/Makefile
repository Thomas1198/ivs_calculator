PYTHON=python3.7

.PHONY: clean test run
.DEFAULT: all

#prelozi projekt vcetne programu pro profiling
all: run profile

#zabali projekt na odevzdani
pack:
		zip -r xdorda00_xosols00_xmatou32_xchova20.zip xdorda00_xosols00_xmatou32_xchova20

#smaze vsechny soubory co nemaji byt odevzdany
clean:

#spusti testy
test:
	@$(PYTHON) tests/test_math.py
	@$(PYTHON) tests/test_parser.py

#generovani dokumentace
doc:
	doxygen

#spusti program
run:
	@$(PYTHON) app.py

#spustí překlad programu pro výpočet směrodatné odchylky na profiling
profile: