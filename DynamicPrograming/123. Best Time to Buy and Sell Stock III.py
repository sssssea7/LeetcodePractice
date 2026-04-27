# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

# similar to 188, but k is fixed to 2
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        k = 2
        n = len(prices)
        dp = [[[-inf]*2 for _ in range(k+2)] for _ in range(n+1)]
        for j in range(1, k+2):
            dp[0][j][0] = 0
        for i, p in enumerate(prices):
            for j in range(1, k+2):
                dp[i+1][j][0] = max(dp[i][j][0], dp[i][j-1][1]+p)
                dp[i+1][j][1] = max(dp[i][j][1], dp[i][j][0]-p)
        return dp[n][k+1][0]

class Solution:
    def maxProfit(self, A: List[int]) -> int:
        @cache
        def dp(i, canBuy, k):
            if i==len(A) or k==0: return 0
            ans = dp(i+1, canBuy, k)
            if canBuy:
                ans = max(ans, -A[i]+dp(i+1, False, k))
            else:
                ans = max(ans, A[i]+dp(i+1, True, k-1))
            return ans
        return dp(0, True, 2)