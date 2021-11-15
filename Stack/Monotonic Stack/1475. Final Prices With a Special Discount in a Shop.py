class Solution:
    def finalPrices(self, A: List[int]) -> List[int]:
        stk = []
        ans = A
        for i in range(len(A)):
            while stk and A[stk[-1]]>=A[i]:
                ii = stk.pop()
                ans[ii] = A[ii]-A[i]
            stk.append(i)
        return ans