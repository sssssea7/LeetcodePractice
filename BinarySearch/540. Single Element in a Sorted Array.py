class Solution:
    def singleNonDuplicate(self, A: List[int]) -> int:
        l, r = 0, len(A)-1
        while l<r:
            m = ((l+r)//4)*2
            if A[m] != A[m+1]: r = m
            else: l = m+2
        return A[l]