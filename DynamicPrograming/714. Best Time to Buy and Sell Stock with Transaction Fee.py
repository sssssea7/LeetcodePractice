# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        @cache
        def dfs(i, hold):
            if i<0:
                return -inf if hold else 0
            if hold:
                return max(dfs(i-1, True), dfs(i-1, False)-prices[i]-fee)
            return max(dfs(i-1, False), dfs(i-1, True)+prices[i])
        return dfs(n-1, False)

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[0, 0] for _ in range(n+1)]
        dp[0][1] = -inf
        for i in range(n):
            dp[i+1][1] = max(dp[i][1], dp[i][0]-prices[i]-fee)
            dp[i+1][0] = max(dp[i][0], dp[i][1]+prices[i])
        return dp[-1][0]

class Solution:
    def maxProfit(self, A: List[int], fee: int) -> int:
        @cache
        def dp(i, canBuy):
            if i==len(A): return 0
            ans = dp(i+1, canBuy)
            if canBuy:
                ans = max(ans, -A[i]-fee+dp(i+1, False))
            else:
                ans = max(ans, A[i]+dp(i+1, True))
            return ans
        return dp(0, True)