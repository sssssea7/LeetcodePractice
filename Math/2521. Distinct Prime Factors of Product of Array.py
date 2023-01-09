# Math theorem: the factors of a number are: 1) less than sqrt(n) 2) optional: one large prime factor greater than sqrt(n)

class Solution:
    def distinctPrimeFactors(self, A: List[int]) -> int:
        primes = []
        for i in range(2, int(sqrt(1000))+1):
            isPrime = True
            for j in range(2, i):
                if i%j==0:
                    isPrime = False
            if isPrime:
                primes.append(i)
                
        ans = set()
        for a in A:
            for p in primes:
                while a%p==0:
                    a //= p
                    ans.add(p)
            if a!=1: ans.add(a)    # contain a large prime factor
        return len(ans)


class Solution:
    def distinctPrimeFactors(self, A: List[int]) -> int:
        ans = set()
        for i in A:
            sq = int(math.sqrt(i))
            for j in range(2, sq + 1):
                if i % j == 0:
                    ans.add(j)
                    while i % j == 0:
                        i //= j
            if i >= 2:
                ans.add(i)
        print(ans)
        return len(ans) 