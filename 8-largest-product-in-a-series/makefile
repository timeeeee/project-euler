all: eight-haskell.o
	ghc eight-haskell.o -o eight-haskell

eight-haskell.o: 8.hs
	ghc -c 8.hs -o eight-haskell.o

clean:
	rm -f *.o *.hi *~ eight-haskell