#include <iostream>

const int MAX = 1000;

int sumOfMultiples(int max);

int main() {
  std::cout << sumOfMultiples(MAX) << std::endl;

  return 0;
}

int sumOfMultiples(int max) {
  int total = 0;
  for (int x = 1; x < max; x++) {
    if ((x % 3 == 0) || (x % 5 == 0)) {
      total += x;
    }
  }
  return total;
}
