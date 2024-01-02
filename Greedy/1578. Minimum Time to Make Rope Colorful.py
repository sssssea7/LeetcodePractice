# https://leetcode.com/problems/minimum-time-to-make-rope-colorful/
class Solution:
    def minCost(self, s: str, T: List[int]) -> int:
        ans = 0
        i = -1
        for k, v in groupby(s):
            cnt = len(list(v))
            i += 1
            if cnt>1:
                j = i+cnt
                ans += sum(sorted(T[i:j])[:-1])
                i = j-1
        return ans

class Solution:
    def minCost(self, s: str, T: List[int]) -> int:
        ans = 0
        i = 0
        for j in range(1, len(s)):
            if s[i]!=s[j]:
                i = j
            else:
                ans += min(T[j], T[i])
                if T[i] < T[j]: i = j
        return ans