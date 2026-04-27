# https://leetcode.com/problems/minimum-score-triangulation-of-polygon/description/

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        @cache
        def dfs(i, j):
            if i+1==j:
                return 0
            ans = inf
            for k in range(i+1, j):
                ans = min(ans, dfs(i,k) + dfs(k,j) + values[i]*values[j]*values[k])
            return ans
        return dfs(0, n-1)

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp = [[0]* n for _ in range(n)]
        for i in range(n-3, -1, -1):
            for j in range(i+2, n):
                ans = inf
                for k in range(i+1, j):
                    ans = min(ans, dp[i][k]+dp[k][j]+values[i]*values[j]*values[k])
                dp[i][j] = ans
        return dp[0][n-1]