-- carry the digits in a list, return anything extra
carry :: [Int] -> (Int, [Int])
carry [ones] = let (newCarry, newOnes) = divMod ones 10
      	       in (newCarry, [newOnes])
carry (x:xs) = let (carried, rest) = carry xs
      	     	   (newCarry, newX) = divMod (x + carried) 10
	       in (newCarry, newX:rest)

carries :: [Int] -> [Int]
carries xs = let (overflow, carried) = carry xs
	     in intToList overflow ++ carried

intToList :: Int -> [Int]
intToList 0 = []
intToList x = let (rest, ones) = divMod x 10
	      in intToList rest ++ [ones]

multiplyList :: Int -> [Int] -> [Int]
multiplyList factor = carries . map (* factor)

factorialList :: Int -> [Int]
factorialList 0 = [1]
factorialList n = multiplyList n $ factorialList (n - 1)

main = print $ sum $ factorialList 100