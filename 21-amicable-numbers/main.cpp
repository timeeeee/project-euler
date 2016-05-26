#include <iostream>

const int MAX = 10000;

int sumOfDivisors(int x);

int main() {
  int divisorSums[MAX - 1];

  // Perform divisor sums
  for (int x = 1; x < MAX; x++) {
    divisorSums[x - 1] = sumOfDivisors(x);
  }

  // Sum amicable numbers
  int total = 0;
  for (int x = 1; x < MAX; x++) {
    int buddy = divisorSums[x - 1];
    //    std::cout << "x = " << x << ", buddy = " << buddy << std::endl;
    if ((buddy > x) &&
	(buddy < 10000) &&
	(divisorSums[buddy - 1] == x)) {
      total += x + buddy;
    }
  }
  std::cout << total << std::endl;
  return 0;
}

int sumOfDivisors(int x) {
  int total = 1;
  int factor = 2;
  while (factor * factor < x) {
    if (x % factor == 0) {
      total += factor + x / factor;
    }
    factor++;
  }
  if (factor * factor == x) total += factor;
  return total;
}
