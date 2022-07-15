# BFS
class Solution:
    def maxAreaOfIsland(self, A: List[List[int]]) -> int:
        D = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        m, n = len(A), len(A[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if A[i][j]==1:
                    A[i][j]=0
                    cur = 1
                    Q = [[i, j]]
                    while Q:
                        x, y = Q.pop(0)
                        for dx, dy in D:
                            if 0<=x+dx<m and 0<=y+dy<n and A[x+dx][y+dy]==1:
                                Q.append([x+dx, y+dy])
                                A[x+dx][y+dy]=0
                                cur += 1
                    ans = max(ans, cur)
        return ans 


# DFS
class Solution:
    def maxAreaOfIsland(self, A: List[List[int]]) -> int:
        D = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        def dfs(x, y):
            cnt = 1
            for dx, dy in D:
                A[x][y]=0
                if 0<=x+dx<len(A) and 0<=y+dy<len(A[0]) and A[x+dx][y+dy]:
                    cnt += dfs(x+dx, y+dy)
            return cnt     
        ans = 0
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j]: ans = max(ans, dfs(i, j))
        return ans