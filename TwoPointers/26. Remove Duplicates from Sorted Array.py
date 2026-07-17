# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, cur = 0, 0
        while cur<len(nums):
            if nums[left] != nums[cur]:
                left += 1
                nums[left] = nums[cur]
            cur += 1
        return left+1

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, curr = 0, 0
        while curr<len(nums):
            if nums[curr]==nums[left]:
                curr += 1
            else:
                left += 1
                nums[left] = nums[curr]
        # print(nums, curr, left)
        return left+1