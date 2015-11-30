#include <iostream>

int squareDigits(int n) {
  int result = 0;
  while (n) {
    int digit = n % 10;
    result += digit * digit;
    n /= 10;
  }
  return result;
}

int oneOr89(int n) {
  while (n != 1 && n != 89) n = squareDigits(n);
  return n;
}

int main() {
  int count = 0;
  for (int n = 1; n < 10000000; n++) {
    if (oneOr89(n) == 89) count++;
  }
  std::cout << count << std::endl;

  return 0;
}
