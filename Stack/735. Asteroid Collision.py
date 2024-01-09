# https://leetcode.com/problems/asteroid-collision/
class Solution:
    def asteroidCollision(self, A: List[int]) -> List[int]:
        stk = []
        for a in A:
            while stk and stk[-1]>0 and a<0:
                x = stk.pop()
                if abs(x)>abs(a):
                    a = x
                elif abs(x)==abs(a):
                    a = 0
            if a: stk.append(a)
        return stk