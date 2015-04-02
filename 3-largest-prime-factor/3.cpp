#include <iostream>

unsigned long largestPrimeFactor(unsigned long x);

int main() {
  std::cout << largestPrimeFactor(600851475143) << std::endl;
  return 0;
}

unsigned long largestPrimeFactor(unsigned long x) {
  unsigned long factor = 3;
  unsigned long largest = 3;
  while (x > largest) {
    if (x % factor == 0) {
      largest = factor;
      x /= factor;
    } else {
      factor += 2;
    }
  }

  return largest;
}
