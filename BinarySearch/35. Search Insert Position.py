class Solution:
    def searchInsert(self, A: List[int], t: int) -> int:
        l, r = 0, len(A)
        while l<r:
            m = (l+r)//2
            if A[m] >= t: r = m
            else: l = m+1
        return l


class Solution:
    def searchInsert(self, A: List[int], t: int) -> int:
        return bisect_left(A, t)