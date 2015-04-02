-- How many letters (not counting spaces or hyphens) are used in spelling out the numbers one through one thousand?

onesCounts = map length ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
                        , "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

tensCounts = map length ["zero", "ten", "twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety"]

letterCount :: Int -> Int
letterCount x
    -- "n thousand, ..."
    | x >= 1000 = let (thousands, rest) = divMod x 1000
                  in letterCount thousands + 8 + letterCount rest
    -- "n hundred (and) ..."
    | x >= 100 = let (hundreds, rest) = divMod x 100
                 in onesCounts !! hundreds + 7 + 
                    if rest > 0 then letterCount rest + 3 else 0
    -- "twenty/thirty..."
    | x >= 20 = let (tens, rest) = divMod x 10
                in tensCounts !! tens + letterCount rest
    -- "one..nineteen"
    | otherwise = onesCounts !! x

main = print $ sum $ map letterCount [1..1000]