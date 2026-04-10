# https://leetcode.com/problems/minimum-path-sum/description/

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        @cache
        def dfs(i, j):
            if i==0 and j==0:
                return grid[i][j]
            if i<0 or j<0:
                return inf
            return min(dfs(i-1, j), dfs(i, j-1)) + grid[i][j]
        m, n = len(grid), len(grid[0])
        return dfs(m-1, n-1)
                