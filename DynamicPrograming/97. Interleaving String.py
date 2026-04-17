# https://leetcode.com/problems/interleaving-string/description/

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m = len(s1), len(s2)
        if n+m != len(s3):
            return False
        @cache
        def dfs(i, j):
            if i<0 and j<0:
                return True
            return i>=0 and s1[i]==s3[i+j+1] and dfs(i-1, j) or j>=0 and s2[j]==s3[i+j+1] and dfs(i, j-1)
        return dfs(n-1, m-1) 

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m = len(s1), len(s2)
        if n+m != len(s3):
            return False
        dp = [[False]*(m+1) for _ in range(n+1)]
        dp[0][0] = True
        for i in range(n):
            dp[i+1][0] = dp[i][0] and s1[i]==s3[i]
        for j in range(m):
            dp[0][j+1] = dp[0][j] and s2[j]==s3[j]
        for i in range(n):
            for j in range(m):
                dp[i+1][j+1] = s1[i]==s3[i+j+1] and dp[i][j+1] or s2[j]==s3[i+j+1] and dp[i+1][j]
        return dp[-1][-1]