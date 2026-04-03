# https://leetcode.com/problems/house-robber-ii/description/

class Solution:
    def rob1(self, nums: List[int]) -> int:
        @cache
        def dfs(i):
            if i<0:
                return 0
            return max(dfs(i-2)+nums[i], dfs(i-1))
        return dfs(len(nums)-1)

    def rob(self, nums: List[int]) -> int:
        return max(self.rob1(nums[1:]), nums[0]+self.rob1(nums[2:-1]))