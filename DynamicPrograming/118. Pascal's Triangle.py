class Solution:
    def generate(self, n: int) -> List[List[int]]:
        ans = []
        for i in range(n):
            row = [1 for _ in range(i+1)]
            for j in range(1, len(row)-1):
                row[j]=ans[i-1][j-1]+ans[i-1][j]
            ans.append(row)
        return ans


class Solution:
    def generate(self, n: int) -> List[List[int]]:
        dp = [[1 for j in range(i)] for i in range(1, n+1)]
        for i in range(2, len(dp)):
            for j in range(1, len(dp[i])-1):
                dp[i][j] = dp[i-1][j-1]+dp[i-1][j]
        return dp