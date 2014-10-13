-- Find the largest prime factor of 600851475143

largestPrimeFactor :: (Integral a) => a -> a
largestPrimeFactor x = largestFactorAbove 3 x where
  largestFactorAbove start x
      | start^2 > x = x
      | (mod x start == 0) = largestFactorAbove (start + 2) (quot x start)
      | otherwise = largestFactorAbove (start + 2) x
                    
main = print (largestPrimeFactor 600851475143)