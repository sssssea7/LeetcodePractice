# https://leetcode.com/problems/maximum-profit-in-job-scheduling/
class Solution:
    def jobScheduling(self, st: List[int], et: List[int], profit: List[int]) -> int:
        A = sorted(zip(st, et, profit))
        @cache
        def dp(i):
            if i==len(st): return 0
            ans = dp(i+1)
            nxt = bisect_left(A, (A[i][1], 0, 0))
            ans = max(ans, A[i][2]+dp(nxt))
            return ans
        return dp(0)