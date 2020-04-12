ising: ising.o
	gcc -o ising ising.o -L$(EDULIB) -lmtwister -lcpgplot -lpgplot -L/usr/lib64 -lX11 -lgfortran -lm
ising.o: ising.c
	gcc -I$(EDULIB) -c ising.c
