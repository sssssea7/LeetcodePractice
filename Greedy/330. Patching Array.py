class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        ans, i, s = 0, 0, 0
        while s < n:
            if i < len(nums) and s + 1 >= nums[i]:
                s += nums[i]
                i += 1
            else: 
                s += s + 1
                ans += 1
        return ans