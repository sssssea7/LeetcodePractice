# top down
class Solution:
    def maxProfit(self, A: List[int]) -> int:
        A = [A[i]-A[i-1] for i in range(1, len(A))]
        @cache
        def dp(i):
            if i==len(A): return 0
            return max(0, A[i]+dp(i+1))
        return max([dp(i) for i in range(len(A))], default=0)


# Kadane
class Solution:
    def maxProfit(self, A: List[int]) -> int:
        A = [A[i]-A[i-1] for i in range(1, len(A))]
        ans = 0
        cur = 0
        for x in A:
            cur = max(0, cur+x)
            ans = max(ans, cur)
        return ans


# bottom up
class Solution:
    def maxProfit(self, A: List[int]) -> int:
        dp = [0]*len(A)
        dp[0] = A[0]
        ans = 0
        for i in range(1, len(A)):
            dp[i] = min(dp[i-1], A[i])
            ans = max(ans, A[i]-dp[i-1])
        return ans