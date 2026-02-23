# https://leetcode.com/problems/merge-adjacent-equal-elements/description/

class Solution:
    def mergeAdjacent(self, A: List[int]) -> List[int]:
        stk = []
        for i in range(len(A)):
            a = A[i]
            if stk:
                while stk and a==stk[-1]:
                    stk.pop()
                    a += a
            stk.append(a)
        return stk
