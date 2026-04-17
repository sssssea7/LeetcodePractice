# https://leetcode.com/problems/delete-operation-for-two-strings/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        @cache
        def dfs(i, j):
            if i<0:
                return j+1
            if j<0:
                return i+1
            if word1[i]==word2[j]:
                return dfs(i-1, j-1)
            return min(dfs(i-1, j), dfs(i, j-1)) + 1
        return dfs(n-1, m-1)

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        dp = [[inf]*(m+1) for _ in range(n+1)]
        dp[0] = list(range(m+1))
        for i in range(n):
            dp[i+1][0] = i+1
            for j in range(m):
                if word1[i]==word2[j]:
                    dp[i+1][j+1] = dp[i][j]
                else:
                    dp[i+1][j+1] = min(dp[i][j+1], dp[i+1][j]) + 1
        return dp[-1][-1]

class Solution:
    def minDistance(self, A: str, B: str) -> int:
        @cache
        def dp(i, j):
            if i==len(A) or j==len(B): return 0
            if A[i]==B[j]: return 1+dp(i+1, j+1)
            else: return max(dp(i+1, j), dp(i, j+1))
        lcs = dp(0, 0)
        return len(A)+len(B)-2*lcs