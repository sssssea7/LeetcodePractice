# https://leetcode.com/problems/removing-stars-from-a-string/
class Solution:
    def removeStars(self, s: str) -> str:
        stk = []
        for c in s:
            if c!="*": stk.append(c)
            else: 
                if stk: stk.pop()
        return "".join(stk)