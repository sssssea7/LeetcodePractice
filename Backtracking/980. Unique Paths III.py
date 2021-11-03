class Solution:
    def uniquePathsIII(self, A: List[List[int]]) -> int:
        M, N = len(A), len(A[0])
        path = set()
        for i in range(M):
            for j in range(N):
                if A[i][j]==0: path.add((i, j))
                if A[i][j]==1: s = [i, j]
                if A[i][j]==2: 
                    e = [i, j]
                    path.add((i, j))
        D = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(x, y, path):
            if [x, y] == e and len(path)==0:
                return 1
            ans = 0
            for dx, dy in D:
                if (x+dx, y+dy) in path:
                    path.remove((x+dx, y+dy))
                    ans += dfs(x+dx, y+dy, path)
                    path.add((x+dx, y+dy))
            return ans
        return dfs(s[0], s[1], path)



class Solution:
    def uniquePathsIII(self, A: List[List[int]]) -> int:
        M, N = len(A), len(A[0])
        D = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        obs = 0
        for i in range(M):
            for j in range(N):
                if A[i][j]==-1: obs += 1
                if A[i][j]==1: s = (i, j)
        def dfs(x, y, cnt):
            if A[x][y]==2 and cnt==M*N-obs: return 1
            ans = 0
            tmp = A[x][y]
            A[x][y] = -1
            for dx, dy in D:
                if 0<=x+dx<M and 0<=y+dy<N and A[x+dx][y+dy]!=-1:
                    ans += dfs(x+dx, y+dy, cnt+1)
            A[x][y] = tmp
            return ans
        ans = dfs(s[0], s[1], 1)
        return ans