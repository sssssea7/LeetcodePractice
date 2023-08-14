class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)==1: return nums[0]
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l+r)//2
            if nums[m] > nums[m+1]: return nums[m+1]
            elif nums[m] < nums[r]: r = m
            else: l = m + 1
        return nums[0]
        

class Solution:
    def findMin(self, A: List[int]) -> int:
        l, r = 0, len(A)-1
        while l<r:
            m = (l+r)//2
            if A[m]<A[r]:
                r = m
            else:
                l = m+1
        return A[l]