// https://projecteuler.net/problem=32
// We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example
// the 5-digit number, 15234, is 1 through 5 pandigital.
// The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1
// through 9 pandigital.
// Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
// HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
// Expected value: 45228

#include <algorithm>
#include <array>
#include <iostream>
#include <math.h>
bool is_pan(int n) {
    std::array<bool,9> exsits = {false};
    while (n > 0) {
        auto t = n%10;
        if (t == 0 || exsits[t-1])
            return false;
        exsits[t-1] = true;
        n /= 10;
    }
    return std::all_of(exsits.begin(), exsits.end(), [](bool t){return t;});
}
long cat(int a, int b, int c) {
    long lenb = 0, lenc = 0, tb = b, tc = c;
    while(tb > 0) { lenb++; tb /= 10; }
    while(tc > 0) { lenc++; tc /= 10; }
    return a*pow(10, lenb+lenc) + b*pow(10, lenc) + c;
}
int main() {
    long sum = 0;
    for (int i = 1; i <= 9876; i++) {
        for (int j = 1; j <= 9876; j++) {
            if (is_pan(cat(i, j, i*j)))
                sum += i*j;
        }
    }
    std::cout << sum << '\n';
}
