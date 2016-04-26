# add up all numbers less than 1000 and divisible by 3 or 5

sum = 0

for n in 1...1000
  sum += n if n % 3 == 0 or n % 5 == 0
end

puts sum
