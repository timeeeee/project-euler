#include <iostream>

const int M = 20;
const int N = 20;

void print_row(unsigned long int row[]) {
  for (int x = 0; x <= N; x++) std::cout << row[x] << " ";
  std::cout << std::endl;
}

int main() {
  int n, m;
  unsigned long int row[N + 1];
  for (n = 0; n <= N; n++) row[n] = 1;

  for (m = 1; m <= M; m++) {
    //    print_row(row);
    for (n = 1; n <= N; n++) row[n] += row[n - 1];
  }
  //  print_row(row);

  std::cout << row[N] << std::endl;

  return 0;
}

  
