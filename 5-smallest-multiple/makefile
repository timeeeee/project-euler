all: haskell cpp

haskell: main.hs
	ghc main.hs -o haskell

cpp: main.cpp
	g++ main.cpp -o cpp

clean:
	rm -f *.o *.hi *~ haskell cpp
