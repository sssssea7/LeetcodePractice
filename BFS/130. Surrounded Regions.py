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