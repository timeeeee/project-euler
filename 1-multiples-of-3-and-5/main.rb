# Sum of all numbers less than 1000 that are divisible by 3 or 5

sum = 0
(1...1000).each { |x| sum += x if (x % 3 == 0 or x % 5 == 0) }
p sum
