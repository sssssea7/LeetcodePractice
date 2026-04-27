# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        @cache
        def dfs(i, hold):
           if i<0: return -inf if hold else 0
           if hold:
               return max(dfs(i-1, True), dfs(i-1, False)-prices[i])
           return max(dfs(i-1, False), dfs(i-1, True)+prices[i])
        return dfs(n-1, False)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0, 0] for _ in range(n+1)]
        dp[0][1] = -inf
        for i, p in enumerate(prices):
            dp[i+1][1] = max(dp[i][1], dp[i][0]-p)
            dp[i+1][0] = max(dp[i][0], dp[i][1]+p)
        return dp[-1][0]

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        f0 = 0
        f1 = -inf
        for p in prices:
            new_f0 = max(f0, f1+p)
            f1 = max(f1, f0-p)
            f0 = new_f0
        return f0


class Solution:
    def maxProfit(self, A: List[int]) -> int:
        p = 0
        for i in range(1, len(A)):
            if A[i]>A[i-1]: p += A[i]-A[i-1]
        return p