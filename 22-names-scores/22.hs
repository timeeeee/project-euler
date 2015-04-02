import Data.List
import Data.List.Split

nameStringToList :: String -> [String]
nameStringToList = sort . splitOn "," . filter (/= '"')

charValue :: Char -> Int
charValue = flip (-) 64 . fromEnum

nameScore :: String -> Int
nameScore = sum . map charValue

nameStringScore :: String -> Int
nameStringScore str = sum [number * nameScore name | (number, name) <- zip [1..] (nameStringToList str)]

main = do name_string <- readFile "names.txt"
          print $ nameStringScore name_string
     