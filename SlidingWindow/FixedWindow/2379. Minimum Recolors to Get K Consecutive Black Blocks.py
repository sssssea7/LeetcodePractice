# https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/
class Solution:
    def minimumRecolors(self, s: str, k: int) -> int:
        sm = sum([1 for c in s[:k] if c=="W"])
        ans = sm
        for i in range(k, len(s)):
            if s[i]=="W":
                sm += 1
            if s[i-k]=="W":
                sm -= 1
            ans = min(ans, sm)
        return ans