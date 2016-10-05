=begin
What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
=end

def gcd a, b
  if a < b
    a, b = b, a
  end

  while b > 0
    quotient, remainder = a.divmod b
    a, b = b, remainder
  end
  
  a
end
  
def lcm a, b
  return a * b / gcd(a, b)
end

puts (1..20).inject(1) { |a, b| lcm a, b}
