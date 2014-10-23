all: ten-cpp ten-haskell

ten-cpp: 10.cpp
	g++ 10.cpp -o ten-cpp

ten-haskell: 10.hs
	ghc 10.hs -o ten-haskell

clean:
	rm -f *.o *.hi *~ ten-haskell ten-cpp