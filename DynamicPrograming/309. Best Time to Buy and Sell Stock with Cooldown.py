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