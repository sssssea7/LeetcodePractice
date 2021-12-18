class Solution:
    def maximalSquare(self, A: List[List[str]]) -> int:
        @cache
        def dfs(i, j):
            if i==len(A) or j==len(A[0]) or A[i][j]=='0': return 0
            return 1+min(dfs(i+1, j), dfs(i, j+1), dfs(i+1, j+1))

        ans = 0
        for i in range(len(A)):
            for j in range(len(A[0])):
                ans = max(ans, dfs(i, j))
        return ans**2        
        