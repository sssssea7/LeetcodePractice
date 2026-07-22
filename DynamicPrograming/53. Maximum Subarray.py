# https://leetcode.com/problems/maximum-subarray/

# kadane
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        current_max = -inf
        global_max = -inf
        for x in nums:
            current_max = max(x, x+current_max)
            global_max = max(current_max, global_max)
        return global_max

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = nums
        for i in range(1, len(nums)):
            dp[i] = max(dp[i], dp[i]+dp[i-1])
        return max(dp)


class Solution:
    def maxSubArray(self, A: List[int]) -> int:
        cur = 0
        ans = float('-inf')
        for i in range(len(A)):
            cur = max(A[i], A[i]+cur)
            if cur > ans: ans = cur
        return ans