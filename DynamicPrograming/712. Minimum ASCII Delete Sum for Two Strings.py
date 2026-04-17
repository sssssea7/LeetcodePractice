# https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/description/

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n, m = len(s1), len(s2)
        @cache
        def dfs(i, j):
            if i<0:
                return sum([ord(s2[i]) for i in range(j+1)])
            if j<0:
                return sum([ord(s1[j]) for j in range(i+1)])
            if s1[i]==s2[j]:
                return dfs(i-1, j-1)
            return min(dfs(i-1, j)+ord(s1[i]), dfs(i, j-1)+ord(s2[j]))
        return dfs(n-1, m-1)

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n, m = len(s1), len(s2)
        dp = [[inf]*(m+1) for _ in range(n+1)]
        dp[0] = [0]+list(accumulate([ord(c) for c in s2]))
        for i in range(n):
            dp[i+1][0] = sum([ord(c) for c in s1[:i+1]])
            for j in range(m):
                if s1[i]==s2[j]:
                    dp[i+1][j+1] = dp[i][j]
                else:
                    dp[i+1][j+1] = min(dp[i][j+1]+ord(s1[i]), dp[i+1][j]+ord(s2[j]))
        return dp[-1][-1]

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        
        @cache
        def dfs(i, j):
            if i==len(s1):
                return sum([ord(s2[idx]) for idx in range(j, len(s2))])
            if j==len(s2):
                return sum([ord(s1[idx]) for idx in range(i, len(s1))])
            if s1[i]==s2[j]:
                return dfs(i+1, j+1)
            return min(dfs(i+1, j)+ord(s1[i]), dfs(i, j+1)+ord(s2[j]))
        return dfs(0, 0)