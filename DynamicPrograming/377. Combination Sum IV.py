# https://leetcode.com/problems/combination-sum-iv/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def dfs(t):
            if t==0: return 1
            ans = 0
            for x in nums:
                if t-x>=0:
                    ans += dfs(t-x)
            return ans
        return dfs(target)

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1] + [0] * target
        for i in range(1, target+1):
            dp[i] = sum([dp[i-x] for x in nums if x<=i])
        return dp[target]

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