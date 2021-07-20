class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ans = ""
        for c in order:
            if c in s:
                ans += c*s.count(c)
                s = s.replace(c, "")
        return ans+s