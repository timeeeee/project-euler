-- Find the highest product of 13 adjacent digits in a 1000 digit number

import Data.Char

eachThirteen :: String -> [String]
eachThirteen string
    | length string == 13 = [string]
    | otherwise = (take 13 string):eachThirteen (tail string)
                  
strProduct :: String -> Integer          
strProduct string = product (map (toInteger . digitToInt) string)

maxString :: [String] -> Integer
maxString strings = maximum (map strProduct strings)
                  
main = do
  string <- readFile "series.txt"
  print $ (maxString . eachThirteen . init) string
