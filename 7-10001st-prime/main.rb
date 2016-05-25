# What is the 10001st prime number?

class ::Integer
  def prime?
    # is it divisible by 2?
    return false if self % 2 == 0

    # does it have any factors <= its square root?
    factor = 3
    while factor**2 <= self
      return false if self % factor == 0
      factor += 2
    end

    # otherwise, it's prime!
    true
  end
end


def nth_prime n
  return 2 if n == 1

  count = 1
  x = 1
  while count < n
    x += 2
    count += 1 if x.prime?
  end
  x
end

sixth_prime = nth_prime 6    
raise "6th prime #{sixth_prime} != 13!" unless sixth_prime == 13

puts nth_prime 10001
