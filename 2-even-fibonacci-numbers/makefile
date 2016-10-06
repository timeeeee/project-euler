all: haskell cpp chicken

haskell: main.hs
	ghc -o haskell main.hs

chicken: main.scm
	csc main.scm -o chicken

cpp: main.cpp
	g++ -o cpp main.cpp

clean:
	rm -f *.o *.hi *~ haskell cpp chicken
