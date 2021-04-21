class Solution:
    def combinationSum4(self, nums: List[int], t: int) -> int:
        dp = [1] + [0] * t
        for i in range(t):
            if not dp[i]: continue
            for n in nums:
                if n + i <= t: dp[i+n] += dp[i]
        return dp[t]


class Solution:
    def combinationSum4(self, nums: List[int], t: int) -> int:
        dp = [1] + [0] * t
        for i in range(1, t+1):
            for n in nums:
                if n<=i: dp[i] += dp[i-n]
        return dp[t]