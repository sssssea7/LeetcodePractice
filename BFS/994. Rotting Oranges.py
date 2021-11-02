class Solution:
    def orangesRotting(self, A: List[List[int]]) -> int:
        M = len(A)
        N = len(A[0])
        Q = [[i, j] for j in range(N) for i in range(M) if A[i][j]==2]
        fresh = sum([1 for j in range(N) for i in range(M) if A[i][j]==1])
        if not fresh: return 0
        D = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        step = -1
        while Q:
            for _ in range(len(Q)):
                x, y = Q.pop(0)
                
                for dx, dy in D:
                    if 0<=x+dx<M and 0<=y+dy<N and A[x+dx][y+dy]==1:
                        A[x+dx][y+dy] = 2
                        fresh -= 1
                        Q.append([x+dx, y+dy])
            step += 1
        if not fresh: return step
        else: return -1