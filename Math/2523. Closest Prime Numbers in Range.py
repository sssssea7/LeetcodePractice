class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        prime = [0]*2+[1]*(right-1)
        
        for i in range(2, int(sqrt(right))+1):
            if prime[i]:
                for j in range(i*i, right+1, i):
                    prime[j] = 0
        primes = [i for i in range(len(prime)) if prime[i]]
        
        cand = [p for p in primes if left<=p<=right]
        
        if len(cand)<2: return [-1, -1]
        ans = [-1 ,-1]
        diff = inf
        for i in range(len(cand)-1):
            if cand[i+1]-cand[i]<diff:
                ans = [cand[i], cand[i+1]]
                diff = cand[i+1]-cand[i]
        return ans