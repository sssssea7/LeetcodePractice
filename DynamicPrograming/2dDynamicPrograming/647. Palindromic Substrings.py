class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[0]*len(s) for _ in range(len(s))]
        ans = 0
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                dp[i][j] = s[i]==s[j] and (j-i<=2 or dp[i+1][j-1])
                if dp[i][j]: ans += 1
        return ans