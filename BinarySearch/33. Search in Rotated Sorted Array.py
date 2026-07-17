# https://leetcode.com/problems/search-in-rotated-sorted-array/description/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) # exclusive r: [l, r)
        while l<r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m
                else:
                    l = m + 1
            else:
                if nums[m] < target <= nums[r-1]:
                    l = m + 1
                else:
                    r = m
        return -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1 # inclusive: [l, r]
        while l <= r:
            m = (l+r)//2
            if nums[m]==target:
                return m
            elif nums[l] > nums[m]:       # right half is sorted
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            else:                         # left half is sorted
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
        return -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l<r:
            m = (l+r)//2
            if nums[l] <= nums[m]:
                if nums[l] <= target <= nums[m]:
                    r = m
                else:
                    l = m + 1
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m
        return l if nums[l] == target else -1

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