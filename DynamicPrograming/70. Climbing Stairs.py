class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1: return n
        dp = [0]*(n+1)
        dp[0], dp[1], dp[2] = 0, 1, 2
        for i in range(3, n+1):
            dp[i] = dp[i-2] + dp[i-1]
        return dp[-1]
        

class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def dp(i):
            if i>=n: return 1
            return dp(i+1) + dp(i+2)
        return dp(1)