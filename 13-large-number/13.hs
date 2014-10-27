numberList :: String -> [Integer]
numberList = map read . lines

firstTenDigits :: Integer -> String
firstTenDigits = take 10 . show

main = do
  numberString <- readFile "data.txt"
  print . firstTenDigits $ sum (numberList numberString)