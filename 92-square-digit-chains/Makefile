all: square_digit_chains cache

square_digit_chains: square_digit_chains.o
	g++ -o square_digit_chains square_digit_chains.o

square_digit_chains.o: square_digit_chains.cpp
	g++ -c square_digit_chains.cpp

cache: cache.o
	g++ -o cache cache.o

cache.o: cache.cpp
	g++ -c cache.cpp

clean:
	rm -f square_digit_chains cache *.o *~
