# https://leetcode.com/problems/greatest-common-divisor-of-strings/
class Solution:
    def gcdOfStrings(self, s1: str, s2: str) -> str:
        ans = ""
        for i in range(1, len(s1)+1):
            cand = s1[:i]
            if cand*(len(s1)//i)==s1 and cand*(len(s2)//i)==s2:
                ans = cand
        return ans
            