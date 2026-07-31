# https://leetcode.com/problems/maximum-sum-circular-subarray/description/

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        local_max = -inf
        global_max = -inf
        local_min = 0
        global_min = 0
        for x in nums:
            local_max = max(local_max+x, x)
            global_max = max(global_max, local_max)
            local_min = min(local_min+x, x)
            global_min = min(global_min, local_min)
        
        if global_max < 0:
            return global_max
        return max(global_max, sum(nums)-global_min)