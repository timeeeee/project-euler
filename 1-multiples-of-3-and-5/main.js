// Didn't end up using sum
function sum(list) {
    var total = 0;
    for (var i = 0; i < list.length; i++) {
	total += list[i];
    }
    return total;
}

var should_be_six = sum([1, 2, 3]);
if (should_be_six != 6)
    throw "sum([1, 2, 3]) should be 6 but was " + should_be_six.toString();

var should_be_zero = sum([]);
if (should_be_zero != 0)
    throw "sum([]) should be 0 but was " + should_be_zero.toString();



total = 0
for (var i = 1; i < 1000; i++) {
    if (i % 3 == 0 || i % 5 == 0) total += i;
}
console.log(total);
