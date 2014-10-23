// Find the sum of all primes under 2 million

#include <iostream>

bool isPrime(int x) {
  for (int factor = 3; factor * factor <= x; factor += 2) {
    if (x % factor == 0) return false;
  }
  return true;
}

int main() {
  long long int sum = 2;
  for (int number = 3; number < 2000000; number += 2) {
    if (isPrime(number)) sum += number;
  }

  std::cout << sum << std::endl;

  return 0;
}

// Takes under 4.5 seconds on my netbook
