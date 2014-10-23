-- Find the sum of all primes less than 2 million

isPrime :: Int -> Bool
isPrime number = not $ any (\x -> mod number x == 0) (takeWhile (\x -> x^2 <= number) [3, 5..])

primes = filter isPrime [3, 5..]

sumOfPrimesBelowN :: Int -> Integer
sumOfPrimesBelowN n = (sum . map toInteger . takeWhile (<n)) primes + 2

main = print (sumOfPrimesBelowN 2000000)

-- This runs SUPER slow, takes almost four minutes on my netbook
-- I don't know how to make primes faster!