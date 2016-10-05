all: haskell cpp chicken

haskell: main.hs
	ghc -o haskell main.hs

cpp: main.cpp
	g++ -o cpp main.cpp

chicken: main.scm
	csc main.scm -o chicken

clean:
	rm -f *.o *.hi *~ haskell cpp chicken
