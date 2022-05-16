class Solution:
    def shortestPathBinaryMatrix(self, A: List[List[int]]) -> int:
        if A[0][0]==1: return -1
        
        D = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        n = len(A)
        step = 1
        Q = [(0, 0)]
        while Q:
            for _ in range(len(Q)):
                x, y = Q.pop(0)
                if x==y==n-1: return step
                for dx, dy in D:
                    if 0<=x+dx<n and 0<=y+dy<n and A[x+dx][y+dy]==0:
                        A[x+dx][y+dy]=1
                        Q.append([x+dx, y+dy])
            step += 1
        return -1