class Solution:
    def maxProfit(self, k: int, A: List[int]) -> int:
        @cache
        def dp(i, canBuy, k):
            if i==len(A) or k==0: return 0
            ans = dp(i+1, canBuy, k)
            if canBuy:
                ans = max(ans, -A[i]+dp(i+1, False, k))
            else:
                ans = max(ans, A[i]+dp(i+1, True, k-1))
            return ans
        return dp(0, True, k)