slowpathsNxM :: Int -> Int -> Int
slowpathsNxM _ 0 = 1
slowpathsNxM 0 _ = 1
slowpathsNxM width height
  | width == height = 2 * slowpathsNxM width (height - 1)
  | otherwise = slowpathsNxM (width - 1) height + slowpathsNxM width (height - 1)

-- Gets prohibitively slow very rapidly starting around n = 15 I know there's a better
-- way to do this recursively but I can't remember it!

-- Don't do this recursively! do one line at a time
-- Start with 0xn lattice- there is only one path from each point
-- adding rows, each is the cumulative sum of the previous one

firstLine = repeat 1 :: [Int]

cumSum :: (Num a) => [a] -> [a]
cumSum = scanl1 (+)

rowM :: Int -> [Int]
rowM height = iterate cumSum firstLine !! height

pathsNxM :: Int -> Int -> Int
pathsNxM width height = rowM height !! width

main = print $ pathsNxM 20 20

-- simpler: main = print $ iterate (scanl1 (+)) (repeat 1) !! 20 !! 20