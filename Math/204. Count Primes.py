# https://leetcode.com/problems/count-primes/description/

class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2:
            return 0
        
        is_prime = [1] * n
        is_prime[0] = 0
        is_prime[1] = 0

        for x in range(int(sqrt(n)+1)):
            if is_prime[x]:
                for multiple in range(x*x, n, x):
                    is_prime[multiple] = 0

        return sum(is_prime)
