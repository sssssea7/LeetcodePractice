# https://leetcode.com/problems/path-crossing/
class Solution:
    def isPathCrossing(self, A: str) -> bool:
        x, y = 0, 0
        seen = set()
        seen.add((0, 0))
        for a in A:
            if a=='N':
                y += 1
            elif a=='S':
                y -= 1
            elif a=='E':
                x += 1
            else:
                x -= 1
            if (x,y) in seen: return True
            seen.add((x,y))
        return False