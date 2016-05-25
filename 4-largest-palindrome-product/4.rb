# Find the largest palindrome made from the product of two 3-digit numbers.

class String
  def is_palindrome?
    self == self.reverse
  end
end

=begin
three_digit_numbers = (1..999).to_a
result = three_digit_numbers.product(three_digit_numbers).inject(0) do |max, factors|
  a, b = factors
  product = a * b
  if product.to_s.is_palindrome? and product > max
    product
  else
    max
  end
end
=end


max = 0
(100..999).each do |a|
  (100..999).each do |b|
    product = a * b
    max = product if product > max and product.to_s.is_palindrome?
  end
end

puts max
