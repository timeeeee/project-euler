# Find the pythagorean triplet which adds up to 1000.

def triple a, b, c
  a**2 + b**2 == c**2
end


def triple_totalling n
  c = 5
  loop do
    b = 2
    while b < c
      a = n - b - c
      if triple a, b, c
        return [a, b, c] if a + b + c == n
      end
      b += 1
    end
    c += 1
  end
end

a, b, c = triple_totalling 1000
puts a * b * c
