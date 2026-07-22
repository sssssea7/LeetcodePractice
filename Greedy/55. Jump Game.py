# https://leetcode.com/problems/jump-game/description/

# greedy
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_step = 0
        for i, step in enumerate(nums):
            if i > max_step:
                return False
            max_step = max(max_step, i + step)
            if max_step >= n-1:
                return True
        return True


# dp
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        
        @cache
        def dfs(i):
            if i>=n-1:
                return True
            for j in range(i+1, i+nums[i]+1):
                if dfs(j):
                    return True
            return False
        return dfs(0)


