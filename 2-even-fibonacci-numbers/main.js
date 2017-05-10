// Find the sum of all even fibonacci numbers below 4 million

var a = 1;
var b = 2;
var total = 0;

while (b < 4000000) {
    if ((b % 2) == 0) total += b;
    b = a + b;
    a = b - a;
}

console.log(total);
