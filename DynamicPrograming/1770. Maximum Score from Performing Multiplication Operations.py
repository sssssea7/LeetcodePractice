# https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/description/

class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)
        @cache
        def dfs(i, j, k):
            if i>j or k==m:
                return 0
            return max(dfs(i+1, j, k+1)+nums[i]*multipliers[k], dfs(i, j-1, k+1)+nums[j]*multipliers[k])
        return dfs(0, n-1, 0)

### this problem can't be directly converted from top-down to bottom-up.
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)
        dp = [[0]*m for _ in range(m+1)]
        for i in reversed(range(m)):
            for j in range(i, m):
                k = i + m-j-1
                dp[i][j] = max(dp[i+1][j]+nums[i]*multipliers[k], dp[i][j-1]+nums[j-m+n]*multipliers[k])
        return dp[0][-1]