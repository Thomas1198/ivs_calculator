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
	rm -fr `find ../ | egrep '__pycache__|html'`

#spusti testy
test:
	@$(PYTHON) -m unittest tests/*

#generovani dokumentace
doc:
	doxygen Doxyfile

#spusti program
run:
	@$(PYTHON) app.py

#spustí překlad programu pro výpočet směrodatné odchylky na profiling
profile:
	python3 ../src/smerodatna_odchylka.py < ../profiling/vypocet/1000cisel.txt