# https://leetcode.com/problems/edit-distance/description/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        @cache
        def dfs(i, j):
            if i<0:
                return j+1
            if j<0:
                return i+1
            if word1[i]==word2[j]:
                return dfs(i-1, j-1)
            return min(dfs(i-1, j), dfs(i, j-1), dfs(i-1, j-1))+1
        return dfs(m-1, n-1)

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[inf]*(n+1) for _ in range(m+1)]
        dp[0] = list(range(n+1))
        for i, x in enumerate(word1):
            dp[i+1][0] = i+1
            for j, y in enumerate(word2):
                if word1[i]==word2[j]:
                    dp[i+1][j+1] = dp[i][j]
                else:
                    dp[i+1][j+1] = min(dp[i][j+1], dp[i+1][j], dp[i][j])+1
        return dp[m][n]