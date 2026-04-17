# https://leetcode.com/problems/perfect-squares/description/

class Solution:
    def numSquares(self, n: int) -> int:
        nums = [x**2 for x in range(1, 1+ceil(sqrt(n)))]
        @cache
        def dfs(i, c):
            if i<0:
                return 0 if c==0 else inf
            if c-nums[i] < 0:
                return dfs(i-1, c)
            return min(1+dfs(i, c-nums[i]), dfs(i-1, c))
        ans = dfs(len(nums)-1, n)
        dfs.cache_clear()
        return ans

class Solution:
    def numSquares(self, n: int) -> int:
        nums = [x**2 for x in range(1, 1+ceil(sqrt(n)))]
        m = len(nums)
        dp = [[inf] * (n+1) for _ in range(m+1)]
        dp[0][0] = 0
        for i in range(m):
            for c in range(n+1):
                if c-nums[i] < 0:
                    dp[i+1][c] = dp[i][c]
                else:
                    dp[i+1][c] = min(1+dp[i+1][c-nums[i]], dp[i][c])
        return dp[-1][-1]

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
                