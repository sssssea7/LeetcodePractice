# BFS
class Solution:
    def solve(self, A: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        M, N = len(A), len(A[0])
        D = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        for i in range(M):
            for j in range(N):
                if (i in [0, M-1] or j in [0, N-1]) and A[i][j] == "O": 
                    Q = [[i, j]]
                    A[i][j] = "#"
                    while Q:
                        x, y = Q.pop(0)
                        for dx, dy in D:
                            if 0<=x+dx<M and 0<=y+dy<N and A[x+dx][y+dy]=="O":
                                Q.append([x+dx, y+dy])
                                A[x+dx][y+dy] = "#"
        for i in range(M):
            for j in range(N):
                if A[i][j]=="O": A[i][j]="X"
                if A[i][j]=="#": A[i][j]="O"

# DFS
class Solution:
    def solve(self, A: List[List[str]]) -> None:
        D = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        m, n = len(A), len(A[0])
        def dfs(x, y):
            if A[x][y]=="O": 
                A[x][y] = "#"
                for dx, dy in D:
                    if 0<=x+dx<m and 0<=y+dy<n and A[x+dx][y+dy]=="O":
                        dfs(x+dx, y+dy)
        for i in range(m):
            for j in range(n):
                if (i in [0, m-1]) or (j in [0, n-1]):
                    dfs(i, j)

        for i in range(m):
            for j in range(n):
                if A[i][j]=="O": A[i][j]="X"
                if A[i][j]=="#": A[i][j]="O"