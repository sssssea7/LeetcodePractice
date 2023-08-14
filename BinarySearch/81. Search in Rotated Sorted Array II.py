class Solution:
    def search(self, A: List[int], t: int) -> bool:
        l, r = 0, len(A)-1
        while l<r:
            m = (l+r)//2
            if A[l]==A[r]: 
                l += 1
                continue
            if A[l]<=t<=A[m] or (A[l]>A[m] and (t<=A[m] or t>=A[l])):
                r = m
            else:
                l = m+1
        return A[l]==t