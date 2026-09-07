# https://leetcode.com/problems/minimum-operations-to-halve-array-sum/description/

class Solution:
    def halveArray(self, nums: List[int]) -> int:
        sm = sum(nums)
        half = sm/2
        heapify_max(nums)
        operation = 0
        while half>0:
            half -= nums[0]/2
            heapreplace_max(nums, nums[0]/2)
            operation += 1
        return operation
