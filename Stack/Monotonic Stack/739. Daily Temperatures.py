""" monotonic stack
two types: 1. store value 2. store index
"""
class Solution:
    def dailyTemperatures(self, A: List[int]) -> List[int]:
        stk = [] # monotonic decreasing stack
        ans = [0] * len(A)
        for i in range(len(A)):
            while stk and A[i]>A[stk[-1]]:
                ii = stk.pop()
                ans[ii] = i - ii
            stk.append(i)
        return ans