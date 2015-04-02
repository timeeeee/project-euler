#include <iostream>

// Find sum of even fibonacci numbers less than 4 million

int main() {
  int last = 1;
  int current = 1;
  int sum = 0;
  while (current < 4000000) {
    if (current % 2 == 0) sum += current;
    current = last + current;
    last = current - last;
  }

  std::cout << sum << std::endl;
  return 0;
}
