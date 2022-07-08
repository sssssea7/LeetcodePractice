class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = [[1 for j in range(i)] for i in range(1, rowIndex+2)]
        for i in range(2, len(dp)):
            for j in range(1, len(dp[i])-1):
                dp[i][j] = dp[i-1][j-1]+dp[i-1][j]
        return dp[rowIndex]