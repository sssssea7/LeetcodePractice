# https://leetcode.com/problems/unique-paths/
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def dfs(i, j):
            if i==m-1 and j==n-1: return 1
            if i==m or j==n: return 0
            return dfs(i+1, j)+dfs(i, j+1)
        return dfs(0, 0)


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0] = [1 for i in range(n)]
        for i in range(m):
            dp[i][0] = 1
            
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j]+dp[i][j-1]

        return dp[-1][-1]