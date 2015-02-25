-- Find the maximum total along a path from the top to the bottom of a triangle of numbers

-- Once we get to a row, each number will have a best path down to it
-- The result for a row is the maximum value path to and including that number
-- For each number in a row, we only have to check the one or two paths above it

-- Take two consecutive rows, and find the maximum-value paths to the bottom row
-- Top row is guaranteed to have at least 1, bottom guaranteed to have at least 2 points
-- length top + 1 = length bottom
foldRows :: [Int] -> [Int] -> [Int]
foldRows [cap] [a, b] = [a + cap, b + cap]
foldRows top bottom = let topOptions = zip (init top) (tail top)
                          topCompare = map (\(a, b) -> max a b) topOptions
                          topMaxes = [head top] ++ topCompare ++ [last top]
                      in zipWith (+) topMaxes bottom

maxPathValue :: [[Int]] -> Int
maxPathValue = maximum . foldl1 foldRows

getTriangle :: String -> [[Int]]
getTriangle = map (map read) . map words . lines

main = do contents <- readFile "example.txt"
          print "example:"
          print $ maxPathValue $ getTriangle contents
          contents <- readFile "triangle.txt"
          print "full problem:"
          print $ maxPathValue $ getTriangle contents