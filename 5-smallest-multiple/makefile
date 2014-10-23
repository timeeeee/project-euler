all: five-haskell five-cpp

five-haskell: 5.hs
	ghc 5.hs -o five-haskell

five-cpp: 5.cpp
	g++ 5.cpp -o five-cpp

clean:
	rm -f *.o *.hi *~ five-haskell five-cpp