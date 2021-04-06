#include <iostream>
#include <sstream>

using namespace std;

void sum(char* output, const long unsigned int d, const long unsigned int n) {
	long unsigned int digits[d + 11];
	#pragma omp parallel for default(none) shared(d, digits)
	for (long unsigned int digit = 0; digit < d + 11; ++digit) {
		digits[digit] = 0;
	}
	int i;
	long unsigned int digit;
	long unsigned int remainder;
	#pragma omp parallel for private(i, remainder, digit)
	for (i = 1; i <= n; ++i) {
		remainder = 1;
		for (long unsigned int digit = 0; digit < d + 11 && remainder; ++digit) {
			long unsigned int div = remainder / i;
			long unsigned int mod = remainder % i;
			#pragma omp atomic
			digits[digit] += div;
			remainder = mod * 10; 
		}
	}
	for (long unsigned int i = d + 11 - 1; i > 0; --i) {
		digits[i - 1] += digits[i] / 10;
		digits[i] %= 10;
	}
	if (digits[d + 1] >= 5) {
		++digits[d];
	}
	for (long unsigned int i = d; i > 0; --i) {
		digits[i - 1] += digits[i] / 10;
		digits[i] %= 10;
	}
	stringstream stringstreamA;
	stringstreamA << digits[0] << ".";
	for (long unsigned int i = 1; i <= d; ++i) {
		stringstreamA << digits[i];
	}
	stringstreamA << '\0';
	string stringA = stringstreamA.str();
	stringA.copy(output, stringA.size());
}

int main() {

	long unsigned int d, n;

	cin >> d >> n;

	char output[d + 10]; // extra precision due to possible error

	sum(output, d, n);

	cout << output << endl;

	return 0;
}
//./sum < sum.in > sum.out 