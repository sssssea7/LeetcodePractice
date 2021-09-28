class Solution:
    def shortestPath(self, A: List[List[int]], k: int) -> int:
        Q = [(0, 0, k)]
        seen = set((0, 0, k))
        step = 0
        D = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while Q:
            for _ in range(len(Q)):
                x, y, k = Q.pop(0)
                if x==len(A)-1 and y==len(A[0])-1: return step
                for dx, dy in D:
                    if 0<=x+dx<len(A) and 0<=y+dy<len(A[0]):
                        if A[x+dx][y+dy]==1 and k>0 and (x+dx, y+dy, k-1) not in seen:
                            seen.add((x+dx, y+dy, k-1))
                            Q.append((x+dx, y+dy, k-1))
                        elif A[x+dx][y+dy]==0 and (x+dx, y+dy, k) not in seen:
                            seen.add((x+dx, y+dy, k))
                            Q.append((x+dx, y+dy, k))
            step += 1
        return -1