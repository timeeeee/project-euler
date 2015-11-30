#include <iostream>

const int MAX = 10000000;
const int TABLESIZE = 9 * 9 * 7; // max sum of squares of digits: if every digit was 9

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
  while (n != 1 && n != 89) {
    n = squareDigits(n);
  }
  return n;
}

int oneOr89(int n, int cache[]) {
  return cache[squareDigits(n) - 1];
}

int main() {
  int cache[TABLESIZE];
  for (int x = 1; x <= TABLESIZE; x++) cache[x - 1] = oneOr89(x);
  
  int count = 0;
  for (int n = 1; n < MAX; n++) {
    if (oneOr89(n, cache) == 89) count++;
  }
  std::cout << count << std::endl;

  return 0;
}
