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
#include <unordered_set>
#include <numeric>
int main() {
    std::array<uint8_t,9> nums = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    std::unordered_set<uint32_t> found;
    uint32_t sum = 0;
    do {
        for (uint8_t i = 0; i <= 4; i++) {
            for (uint8_t j = 0; j <= 4; j++) {
                uint32_t a = 0;
                for (uint8_t x = 0; x < i; x++) {
                    a *= 10; 
                    a += nums[x];
                }
                uint32_t b = 0;
                for (uint8_t y = i; y < j+i; y++) {
                    b *= 10; 
                    b += nums[y];
                }
                uint32_t c = 0;
                for (uint8_t z = i+j; z < 9; z++) {
                    c *= 10; 
                    c += nums[z];
                }
                if (a*b == c)
                    found.insert(c);
            }
        }
    } while (std::next_permutation(nums.begin(), nums.end()));
    std::cout << std::accumulate(found.begin(), found.end(), 0) << '\n';
}
