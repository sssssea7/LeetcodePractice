# https://leetcode.com/problems/binary-search/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) # [left, right)
        while left < right:
            middle = (left+right)//2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right = middle
            else:
                left = middle + 1
        return -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1 # [l, r]
        while l <= r:
            m = (l+r)//2
            if nums[m]==target:
                return m
            elif nums[m]<target:
                l = m + 1
            else:
                r = m - 1
        return -1