class Solution:
    def maxPower(self, s: str) -> int:
        ans, cur = 1, 1
        for i in range(len(s)-1):
            if s[i]==s[i+1]: cur += 1
            else: 
                ans = max(ans, cur)
                cur = 1
        return max(ans, cur)