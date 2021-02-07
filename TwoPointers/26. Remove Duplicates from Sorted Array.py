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