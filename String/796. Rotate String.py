# https://leetcode.com/problems/rotate-string/
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        S = s*2
        return goal in S and len(s)==len(goal)