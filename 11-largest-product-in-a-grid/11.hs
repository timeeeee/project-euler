-- Find the greatest of 4 numbers adjacent in the same direction up, down, left, right or diagonal

import Data.List
  
makeGrid :: String -> [[Int]]
makeGrid = map (map read . words) . lines

-- get all consecutive sets of n
setsOfN :: Int -> [a] -> [[a]]
setsOfN size list = if length list < size then [] else (take size list):(setsOfN size (tail list))

horizontalMax :: [[Int]] -> Int
horizontalMax = maximum . map product . foldl1 (++) . map (setsOfN 4)

verticalMax :: [[Int]] -> Int
verticalMax = horizontalMax . transpose

diagonalLeftMax :: [[Int]] -> Int
diagonalLeftMax [_, _, _] = 0
diagonalLeftMax list = max (maxRow list) (diagonalLeftMax (tail list)) where
  maxRow ([_, _, _]:_) = 0
  maxRow list = let thisDiagonal = (list !! 0 !! 0) *
                                   (list !! 1 !! 1) *
                                   (list !! 2 !! 2) *
                                   (list !! 3 !! 3) in
                max thisDiagonal (maxRow (map tail list))
                
diagonalRightMax :: [[Int]] -> Int
diagonalRightMax [_, _, _] = 0
diagonalRightMax list = max (maxRow list) (diagonalRightMax (tail list)) where
  maxRow ([_, _, _]:_) = 0
  maxRow list = let thisDiagonal = (list !! 0 !! 3) *
                                   (list !! 1 !! 2) *
                                   (list !! 2 !! 1) *
                                   (list !! 3 !! 0) in
                max thisDiagonal (maxRow (map tail list))
    
main = do
  stringGrid <- readFile "data.txt"
  let grid = makeGrid stringGrid
      biggest = maximum $ map ($ grid) [horizontalMax, verticalMax, diagonalLeftMax, diagonalRightMax]
  print biggest

testgrid = [[1, 2, 3, 4, 1],
            [2, 3, 4, 5, 2],
            [3, 4, 5, 6, 3],
            [4, 5, 6, 7, 4],
            [3, 4, 2, 1, 1]] :: [[Int]]