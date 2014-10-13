# Find the sum of all even fibonacci numbers below 4000000

a = 1
b = 1
c = 2
total = 0

while c < 4000000:
    if c % 2 == 0:
        total += c
    a = b
    b = c
    c = a + b

print total 
