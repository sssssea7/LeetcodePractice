class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        s = 0
        top = [max(t) for t in list(zip(*grid))]
        left = [max(l) for l in grid]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                s += min(left[i], top[j]) - grid[i][j]
        return s