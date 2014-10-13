-- What is the smallest positive number that is evenly divisible by all numbers 1-20?

divisiblebyrange :: Int -> Int
divisiblebyrange stop = foldl lcm 1 [1..stop]

main = print (divisiblebyrange 20)