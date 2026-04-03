# https://leetcode.com/problems/delete-and-earn/description/

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        a = [0] * (max(nums)+1)
        for x in nums:
            a[x] += x

        n = len(a)
        @cache
        def dfs(i):
            if i<0:
                return 0
            return max(dfs(i-1), dfs(i-2)+a[i])
            
        return dfs(n-1)
