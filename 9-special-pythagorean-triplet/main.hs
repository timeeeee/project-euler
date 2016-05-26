-- Find the product of the only pythagorean triple whose sum is 1000

-- triples is all pythagorean triples that add up to 1000 (there is only one)
triples = [(a, b, c) | b <- [2..], a <- [1..(b-1)], let c = 1000 - a - b, a^2 + b^2 == c^2]

main = do
  let triple = head triples
  print triple
  print (threeTupleProduct triple) where
    threeTupleProduct (a, b, c) = a * b * c