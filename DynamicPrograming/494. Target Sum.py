# https://leetcode.com/problems/target-sum/description/


"""
Assume the sum of all positive numbers is p. The sum of all # is sm.
Then the sum of all negative numbers is sm-p.
-> p-(sm-p) = t -> 2p-sm = t -> p = (sm+t)/2
"""

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        target = sum(nums) + target
        if target < 0 or target % 2:
            return 0
        target //= 2

        @cache
        def dfs(i, capacity):
            if i<0:
                return 1 if capacity == 0 else 0
            if capacity-nums[i]<0:
                return dfs(i-1, capacity)
            return dfs(i-1, capacity) + dfs(i-1, capacity-nums[i])
        
        return dfs(len(nums)-1, target)


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        target = sum(nums) + target
        if target < 0 or target % 2:
            return 0
        target //= 2

        n = len(nums)
        dp = [[0]*(target+1) for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(n):
            for j in range(target+1):
                if j-nums[i]<0:
                    dp[i+1][j] = dp[i][j]
                else:    
                    dp[i+1][j] = dp[i][j] + dp[i][j-nums[i]]
        return dp[n][target]

#----------------------------

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def dfs(i, capacity):
            if i<0:
                return capacity==0
            return dfs(i-1, capacity+nums[i]) + dfs(i-1, capacity-nums[i])
        return dfs(len(nums)-1, target)

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sm = sum(nums)
        n = len(nums)
        dp = [[0 for _ in range(2*max(sm, abs(target))+1)] for _ in range(n+1)]
        dp[0][0] = 1

        for i in range(n):
            for j in range(-sm-1, sm+1):
                dp[i+1][j] = dp[i][j+nums[i]] + dp[i][j-nums[i]]
        return dp[n][target]

class Solution:
    def findTargetSumWays(self, A: List[int], target: int) -> int:
        @cache
        def dfs(i, sm):
            if i==len(A):
                return sm == target
            return dfs(i+1, sm+A[i]) + dfs(i+1, sm-A[i])
        
        return dfs(0, 0)
