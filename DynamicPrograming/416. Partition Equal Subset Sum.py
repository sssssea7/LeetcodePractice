# https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        sm = sum(nums)
        target = sm//2
        if target != sm/2:
            return False
        dp = [[False]*(target+1) for _ in range(n+1)]
        dp[0][0] = True
        for i in range(n):
            for c in range(target+1):
                if c-nums[i] < 0:
                    dp[i+1][c] = dp[i][c]
                else:
                    dp[i+1][c] = dp[i][c-nums[i]] or dp[i][c]
        return dp[-1][-1]

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        sm = sum(nums)
        target = sm//2
        if target != sm/2:
            return False
        @cache
        def dfs(i, c):
            if i<0:
                return True if c==0 else False
            if c-nums[i] < 0:
                return dfs(i-1, c)
            return dfs(i-1, c-nums[i]) or dfs(i-1, c)
        return dfs(n-1, target)


class Solution:
    def canPartition(self, A: List[int]) -> bool:
        if sum(A)&1: return False      # if sum is odd, can't be partitioned into 2 equal subsetsx
        s = sum(A)//2
        @cache
        def dfs(i, cur):
            if i==len(A) or cur<0: return False
            if cur==0: return True
            return dfs(i+1, cur-A[i]) or dfs(i+1, cur)
        return dfs(0, s)


