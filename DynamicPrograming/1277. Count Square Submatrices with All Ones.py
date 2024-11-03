# https://leetcode.com/problems/count-square-submatrices-with-all-ones/
class Solution:
    def countSquares(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]          
        ans = 0
        for i in range(m):
            for j in range(n):
                if A[i][j]:
                    dp[i+1][j+1] = min(dp[i][j+1], dp[i][j], dp[i+1][j])+1
                    ans += dp[i+1][j+1]
        return ans
                