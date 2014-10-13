all: five-haskell.o five-cpp.o
	ghc five-haskell.o -o five-haskell
	g++ five-cpp.o -o five-cpp

five-haskell.o: 5.hs
	ghc -c 5.hs -o five-haskell.o

five-cpp.o: 5.cpp
	g++ -c 5.cpp -o five-cpp.o

clean:
	rm -f *.o *.hi *~ five-haskell five-cpp