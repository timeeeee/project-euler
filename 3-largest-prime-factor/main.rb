# What is the largest prime factor of the number 600851475143?

def prime_factors n
  factor = 3
  factors = []
  until n == 1
    dividend, remainder = n.divmod factor
    if remainder == 0
      n = dividend
      factors << factor
    end
    factor += 2
  end
  factors
end

puts prime_factors(600851475143).last

