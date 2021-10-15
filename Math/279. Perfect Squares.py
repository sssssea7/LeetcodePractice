class Solution:
    def numSquares(self, n: int) -> int:
        if int(sqrt(n))**2 == n: return 1
        
        for i in range(int(sqrt(n))+1):
            if int(sqrt(n-i*i))**2 == n-i*i: return 2
            
        # Every positive integer is a sum of four integer squares
        # If the number has the form 4^r (8⁢k+7) it can be expressed as a sum of four squares.
        while n%4 == 0:
            n //= 4
        if n%8 == 7: return 4
        
        return 3

# dp
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        for i in range(n+1):
            j = 1
            while i+j*j<=n:
                dp[i+j*j] = min(dp[i]+1, dp[i+j*j])
                j += 1
        return dp[-1]
                