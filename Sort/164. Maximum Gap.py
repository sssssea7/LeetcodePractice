class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums)==1: return 0
        nums = sorted(nums)
        ans = 0
        for i in range(len(nums)-1):
            ans = max(ans, nums[i+1]-nums[i])
        return ans

# try runs in linear time and uses linear extra space