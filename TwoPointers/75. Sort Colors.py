class Solution:
    def sortColors(self, A: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(A)-1
        while l<r:
            if A[l]>A[r]: A[l], A[r] = A[r], A[l]
            if A[l]==0: l += 1
            if A[r]==2: r -= 1
            if A[l]==A[r]: l += 1
        
        l, r = 0, len(A)-1
        while l<r:
            if A[l]>A[r]: A[l], A[r] = A[r], A[l]
            if A[l]==0: l += 1
            if A[r]==2: r -= 1
            if A[l]==A[r]: r -= 1