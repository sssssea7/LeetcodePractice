# https://leetcode.com/problems/minimum-falling-path-sum/
class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        @cache
        def dp(i, j):
            if i==len(A): return 0
            if j<0 or j==len(A): return inf
            return min(A[i][j]+dp(i+1, j-1), A[i][j]+dp(i+1, j), A[i][j]+dp(i+1, j+1))
        ans = inf
        for j in range(len(A)):
            ans = min(ans, dp(0, j))
        return ans