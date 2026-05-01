# https://leetcode.com/problems/longest-palindromic-subsequence-after-at-most-k-operations/


class Solution:
    def longestPalindromicSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        def dist(a, b):
            distance = abs(ord(a)-ord(b))
            return min(distance, 26-distance)
        dp = [[[0] * n for _ in range(n)] for _ in range(k+1)]
        for q in range(k+1):
            for i in range(n-1, -1, -1):
                dp[q][i][i] = 1
                for j in range(i+1, n):        
                    if q-dist(s[i], s[j])<0:
                        dp[q][i][j] = max(dp[q][i+1][j], dp[q][i][j-1])
                    else:
                        dp[q][i][j] = max(dp[q][i+1][j], dp[q][i][j-1], dp[q-dist(s[i], s[j])][i+1][j-1]+2)
        return dp[k][0][n-1]

# memory limit exceeded
class Solution:
    def longestPalindromicSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        def dist(a, b):
            distance = abs(ord(a)-ord(b))
            return min(distance, 26-distance)
        
        @cache
        def dfs(i, j, k):
            if i==j:
                return 1
            if i>j:
                return 0
            if k-dist(s[i], s[j])<0:
                return max(dfs(i+1, j, k), dfs(i, j-1, k))
            return max(dfs(i+1, j, k), dfs(i, j-1, k), dfs(i+1, j-1, k-dist(s[i], s[j]))+2)
        dfs.cache_clear()
        return dfs(0, n-1, k)