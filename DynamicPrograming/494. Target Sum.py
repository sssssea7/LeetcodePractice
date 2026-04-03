# https://leetcode.com/problems/target-sum/description/

class Solution:
    def findTargetSumWays(self, A: List[int], target: int) -> int:
        
        @cache
        def dfs(i, sm):
            if i==len(A):
                return sm == target
            return dfs(i+1, sm+A[i]) + dfs(i+1, sm-A[i])
        
        return dfs(0, 0)
