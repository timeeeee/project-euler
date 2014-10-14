isPrime :: Int -> Bool
isPrime x = testFactorsFrom 3 x where
  testFactorsFrom start x = if start^2 > x
                            then True
                            else (x `mod` start) > 0 && testFactorsFrom (start + 2) x

primes = 2:(filter isPrime [3, 5..])

nthPrime :: Int -> Int
nthPrime n = primes !! (n - 1)

main = print (nthPrime 10001)