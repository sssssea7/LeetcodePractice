class Solution:
    def uniquePathsWithObstacles(self, A: List[List[int]]) -> int:
        M, N = len(A), len(A[0])
        if A[0][0]==1 or A[M-1][N-1]==1: return 0
        
        @cache
        def dfs(x, y):
            if [x, y]==[M-1, N-1]: return 1
            if not (0<=x<M and 0<=y<N and A[x][y]==0): return 0
            return dfs(x+1, y)+dfs(x, y+1)
        
        return dfs(0, 0)

class Solution:
    def uniquePathsWithObstacles(self, A: List[List[int]]) -> int:
        m = len(A)
        n = len(A[0])
        @cache
        def dfs(i, j):
            if i==m-1 and j==n-1 and not A[i][j]: return 1
            if i==m or j==n or A[i][j]: return 0
            return dfs(i+1, j)+dfs(i, j+1)
        return dfs(0, 0)