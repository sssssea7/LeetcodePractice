class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            # ans += n%2
            ans += n & 1
            n = n >> 1
        return ans
        

class Solution:
    def hammingWeight(self, n: int) -> int:
        b = bin(n)[2:]
        return sum([int(i) for i in b])