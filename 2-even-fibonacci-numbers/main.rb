# Find the sum of all even fibonacci numbers below 4000000

=begin
fibs = Enumerator.new do |yielder|
  prev = 0
  this = 1
  while true
    yielder << this
    this += prev
    prev = this - prev
  end
end

fibs_under_4_million = fibs.take_while { |x| x < 4000000 }
even_fibs_under_4_million = fibs_under_4_million.select { |x| x.even? }
puts even_fibs_under_4_million.inject(0, :+)
=end

prev = 0
current = 1
total = 0
while current < 4000000
  total += current if current.even?
  current += prev
  prev = current - prev
end

puts total
  

  
