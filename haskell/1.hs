-- Find sum of all multiples of 3 or 5 less than 1000

sumMultiples3and5 :: Int -> Int
sumMultiples3and5 max = sum (filter isMultiple [1..max])
                        where isMultiple x = (mod x 3 == 0) || (mod x 5 == 0)
                              
-- result of sumMultiples3and5 9 = 23, given in problem
-- result of sumMultiples3and5 999 = 233168