=begin
Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
=end

def sum_of_squares_to n
  (1..n).inject(0) { |sum, x| sum + x**2 }
end

def square_of_sum_to n
  sum = n * (n + 1) / 2
  sum**2
end

square_of_sum = square_of_sum_to 10
sum_of_squares = sum_of_squares_to 10
test_diff = square_of_sum - sum_of_squares
raise "#{square_of_sum} - #{sum_of_squares} != 2640!" unless test_diff == 2640

puts square_of_sum_to(100) - sum_of_squares_to(100)
