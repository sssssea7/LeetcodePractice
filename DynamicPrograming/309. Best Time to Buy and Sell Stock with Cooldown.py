# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        @cache
        def dfs(i, hold):
            if i<0:
                return -inf if hold else 0
            if hold:
                return max(dfs(i-1, True), dfs(i-2, False)-prices[i])
            return max(dfs(i-1, False), dfs(i-1, True)+prices[i])
        return dfs(n-1, False)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0, 0] for _ in range(n+2)]
        dp[1][1] = -inf
        for i in range(n):
            dp[i+2][1] = max(dp[i+1][1], dp[i][0]-prices[i])
            dp[i+2][0] = max(dp[i+1][0], dp[i+1][1]+prices[i])
        return dp[-1][0]

class Solution:
    def maxProfit(self, A: List[int]) -> int:
        @cache
        def dp(i, canBuy):
            if i>=len(A): return 0
            ans = dp(i+1, canBuy)
            if canBuy:
                ans = max(ans, -A[i]+dp(i+1, False))
            else:
                ans = max(ans, A[i]+dp(i+2, True))
            return ans
        return dp(0, True)