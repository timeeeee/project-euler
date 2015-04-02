haskell: 22.hs
	ghc 22.hs -o haskell22

cpp: 22cpp.o minHeap.o
	g++ 22cpp.o minHeap.o -o cpp22

22cpp.o: 22.cpp
	g++ -c 22.cpp

minHeap.o: minHeap.h minHeap.cpp 
	g++ -c minHeap.cpp

clean:
	rm -f *.o *.hi *.pyc *~ haskell22 cpp22
