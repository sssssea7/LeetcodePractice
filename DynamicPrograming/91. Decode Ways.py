# https://leetcode.com/problems/decode-ways/
class Solution:
    def numDecodings(self, s: str) -> int:
        @cache
        def dp(i):
            if i==len(s): return 1
            if s[i]=="0": return 0
            if i<len(s)-1 and s[i:i+2]<="26":
                return dp(i+1)+dp(i+2)
            return dp(i+1)
        return dp(0)