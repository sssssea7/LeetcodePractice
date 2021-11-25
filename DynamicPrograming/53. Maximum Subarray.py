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