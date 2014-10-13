-- Find the largest palindrome that is the product of two 3-digit numbers

-- toDigits :: (Integral a) => a -> [a]
-- toDigits n = addDigits n [] where
--   addDigits 0 list = list
--   addDigits n list = addDigits (n `quot` 10) ((n `mod` 10):list)

-- After reading someone's integer-to-digits question on stack overflow I rewrote that ^ as this:  
toDigits :: (Integral a) => a -> [a]
toDigits 0 = []
toDigits n = (n `mod` 10):(toDigits (n `quot` 10))
  
isPalindrome :: (Integral a) => a -> Bool
isPalindrome x = digits == reverse digits where
  digits = toDigits x
  
maxPalindrome = maximum (filter isPalindrome [a*b | a <- [111..999], b <- [111.. 999]])

main = (print maxPalindrome)