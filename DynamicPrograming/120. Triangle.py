class Solution:
    def minimumTotal(self, T: List[List[int]]) -> int:
        dp = T[-1]
        for i in range(len(T)-2, -1, -1):
            for j in range(i+1):
                dp[j] = T[i][j] + min(dp[j], dp[j+1])
        return dp[0]


class Solution:
    def minimumTotal(self, A: List[List[int]]) -> int:
        @cache
        def dfs(i, j):
            if i==len(A) or j==len(A[i]): return 0
            return A[i][j]+min(dfs(i+1, j), dfs(i+1, j+1))
        return dfs(0, 0)

class Solution:
    def minimumTotal(self, A: List[List[int]]) -> int:
        for i in range(len(A)-2, -1, -1):
            for j in range(len(A[i])):
                A[i][j] = A[i][j]+min(A[i+1][j], A[i+1][j+1])
        return A[0][0]