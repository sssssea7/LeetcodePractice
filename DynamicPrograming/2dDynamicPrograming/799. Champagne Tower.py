class Solution:
    def champagneTower(self, n: int, row: int, col: int) -> float:
        dp = [[0 for _ in range(i+1)] for i in range(row+1)]
        dp[0][0] = n
        for i in range(row):
            for j in range(i+1):
                dp[i+1][j] += max(0, (dp[i][j]-1)/2)
                dp[i+1][j+1] += max(0, (dp[i][j]-1)/2)
        return min(dp[row][col], 1)