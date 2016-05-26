all: haskell cpp

haskell: main.hs
	ghc -o haskell main.hs

cpp: main.cpp
	g++ -o cpp main.cpp

clean:
	rm -f *.o *.hi *~ haskell cpp
