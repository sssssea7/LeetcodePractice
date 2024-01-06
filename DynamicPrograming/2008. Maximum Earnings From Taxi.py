# https://leetcode.com/problems/maximum-earnings-from-taxi/
class Solution:
    def maxTaxiEarnings(self, n: int, A: List[List[int]]) -> int:
        A.sort()
        @cache
        def dp(i):
            if i==len(A): return 0
            ans = dp(i+1)
            nxt = bisect_left(A, [A[i][1], 0 ,0])
            ans = max(ans, A[i][1]-A[i][0]+A[i][2]+dp(nxt))
            return ans
        return dp(0)