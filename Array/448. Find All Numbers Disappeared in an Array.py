class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for n in nums:
            if nums[abs(n)-1]>0: nums[abs(n)-1] *= -1
        return [i+1 for i in range(len(nums)) if nums[i]>0]