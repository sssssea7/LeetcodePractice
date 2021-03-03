class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        s_nums = sorted(nums)
        l, r = 0, len(nums)-1
        while l<r:
            if nums[l]==s_nums[l]: l += 1
            elif nums[r]==s_nums[r]: r -= 1
            else: break
        return r-l+1 if r-l!=0 else 0