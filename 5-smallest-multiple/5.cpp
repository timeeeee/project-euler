#include <iostream>

// Finds greatest common divisor using Euclids algorithm
// Expects that a > b
unsigned long int gcd(unsigned long int a, unsigned long int b) {
  unsigned long int remainder = a % b;
  if (remainder == 0) {
    return b;
  } else {
    return gcd(b, remainder);
  }
}

unsigned long int lcm(unsigned long int a, unsigned long int b) {
  if (a > b) {
    return a / gcd(a, b) *  b;
  } else {
    return b / gcd(b, a) * a;
  }
}

int main() {
  unsigned long int divByList = 1;
  for (int x = 1; x <= 20; x++) {
    divByList = lcm(x, divByList);
  }
  std::cout << divByList << std::endl;
  return 0;
}
