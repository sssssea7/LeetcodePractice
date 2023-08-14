class Solution:
    def search(self, A: List[int], t: int) -> int:
        l, r = 0, len(A)-1
        while l<r:
            m = (l+r)//2
            if A[l]<=t<=A[m] or (A[l]>A[m] and (t<=A[m] or t>=A[l])):
                r = m
            else:
                l = m+1
        return l if A[l]==t else -1