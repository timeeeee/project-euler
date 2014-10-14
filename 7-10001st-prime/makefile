all: seven-haskell.o
	ghc seven-haskell.o -o seven-haskell

seven-haskell.o: 7.hs
	ghc -c 7.hs -o seven-haskell.o

clean:
	rm -f *~ *.o *.hi seven-haskell