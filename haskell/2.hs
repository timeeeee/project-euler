-- find sum of even fibonacci numbers less than 4 million

fibonacci :: Int -> [Int]
fibonacci max = listTo max [1,1] where
  listTo max (a:b:list) = if (a + b >= max)
                             then a:b:list
                             else listTo max ((a + b):a:b:list)
                                  
-- sum (filter even (fibonacci 4000000)) = 4613732