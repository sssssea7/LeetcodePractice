class Solution:
    def longestCommonSubsequence(self, A: str, B: str) -> int:
        @cache
        def dfs(i, j):
            if i==len(A) or j == len(B): return 0
            if A[i]==B[j]: return 1+dfs(i+1, j+1)
            else: return max(dfs(i+1, j), dfs(i, j+1))
        return dfs(0, 0)

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                if text1[i]==text2[j]:
                    dp[i+1][j+1] = 1+dp[i][j]
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
        return dp[-1][-1]