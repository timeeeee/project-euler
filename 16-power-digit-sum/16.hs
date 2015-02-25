-- doubles a list of digits, in reverse order from the number they represent
doubleList :: [Int] -> [Int]
doubleList (ones:tens:rest) =
    if ones < 5 then ones * 2:(doubleList (tens:rest))
                else (:) (ones * 2 - 10) $ carry $ doubleList (tens:rest)
doubleList [ones] = if ones < 5 then [ones * 2] else [ones * 2 - 10, 1]

-- carry a one into the lowest digit of a list
carry :: [Int] -> [Int]
carry (x:xs) = if x < 9
               then x + 1:xs
               else 0:(carry xs)
carry [] = [1]

-- find the sum of the digits of 2^n
sumOfDigits :: Int -> Int
sumOfDigits n = sum $ iterate doubleList[1] !! n

main = print $ sumOfDigits 1000