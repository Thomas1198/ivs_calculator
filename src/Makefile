PYTHON=python3

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
<<<<<<< HEAD
	@$(PYTHON) -m unittest tests/*
=======
	@$(PYTHON) -m unittest tests/test_math.py
	@$(PYTHON) -m unittest tests/test_parser.py
>>>>>>> e60028f988d632c7bbf03efd262c04d864d09e0c

#generovani dokumentace
doc:
	doxygen Doxyfile

#spusti program
run:
	@$(PYTHON) app.py

#spustí překlad programu pro výpočet směrodatné odchylky na profiling
profile: