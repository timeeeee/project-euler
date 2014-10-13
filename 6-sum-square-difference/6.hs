-- Find the difference of the sum of the squares and the square of the sum of the first 100 natural numbers
-- 1^2 + 2^2 + 3^2... - (1 + 2 + 3...)^2

main = print ((sum [1..100])^2 - sum [x^2 | x <- [1..100]])