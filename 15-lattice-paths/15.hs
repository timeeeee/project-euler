pathsNxM :: Int -> Int -> Int
pathsNxM _ 0 = 1
pathsNxM 0 _ = 1
pathsNxM width height
  | width == height = 2 * pathsNxM width (height - 1)
  | otherwise = pathsNxM (width - 1) height + pathsNxM width (height - 1)

main = print $ pathsNxM 20 20

-- Gets prohibitively slow very rapidly starting around n = 15 I know there's a better
-- way to do this recursively but I can't remember it!