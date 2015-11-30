#include <iostream>

const int M = 20;
const int N = 20;

int main() {
  int n, m;

  // First row is all ones
  int row[M + 1];
  for (m = 0; m <= M; m++) row[m] = 1;

  // Calculate each new row in place
  for (int n = 1; n <= N; n++) {
    for (int m = 1; m <= M; m++) row[m] = row[m - 1] + row[m];
  }

  std::cout << row[m - 1] << std::endl;

  return 0;
}

