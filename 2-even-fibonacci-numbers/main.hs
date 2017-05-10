-- find sum of even fibonacci numbers less than 4 million

fib_iter :: Int -> Int -> Int -> Int
fib_iter a b 0 = b
fib_iter a b count = fib_iter b (a + b) (count - 1)

fib :: Int -> Int
fib n = fib_iter 0 1 n
                                  
fibs = map fib [0..]

main = print $ sum $ filter even $ takeWhile (< 4000000) fibs
