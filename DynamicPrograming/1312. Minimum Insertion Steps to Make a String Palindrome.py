# https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/description/

class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        @cache
        def dfs(i, j):
            if i>=j:
                return 0
            if s[i]==s[j]:
                return dfs(i+1, j-1)
            return min(dfs(i+1, j), dfs(i, j-1)) + 1
        return dfs(0, n-1)

class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if s[i]==s[j]:
                    dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = min(dp[i+1][j], dp[i][j-1]) + 1
        return dp[0][n-1]