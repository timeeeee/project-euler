-- Find starting number under one million with longest collatz chain

-- for maximumBy
import Data.List

collatzSequenceLength :: Int -> Int
collatzSequenceLength 1 = 1
collatzSequenceLength start = (+1) $ collatzSequenceLength $ if even start then start `quot` 2 else start * 3 + 1

sequences to = zip starts results where
  starts = [1..to]
  results = map collatzSequenceLength starts
  
main = print $ foldl1 pairMax (sequences 1000000) where
  pairMax (start1, length1) (start2, length2) = if start1 < start2 then
                                                  (start1, length1) else
                                                  (start2, length2)
                                                  
-- stack space overflow :-(                                                  