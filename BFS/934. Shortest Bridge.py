class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    si = i
                    sj = j
                    Q = [(i, j)]
                    seen = [(i, j)]
                    grid[i][j]=2
                    break
            else:
                continue
            break
        
        D = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while Q:
            for _ in range(len(Q)):
                x, y = Q.pop(0)
                for dx, dy in D:
                    if 0<=x+dx<len(grid) and 0<=y+dy<len(grid[0]):
                        if grid[x+dx][y+dy] == 1 and (x+dx, y+dy) not in seen: 
                            grid[x+dx][y+dy] = 2
                            Q.append((x+dx, y+dy)) 
                            seen.append((x+dx, y+dy))

        Q = [(0, si, sj)]
        seen = [(si, sj)]

        while Q:
            for _ in range(len(Q)):
                k, x, y = heapq.heappop(Q)
                if grid[x][y]==1: return k
                for dx, dy in D:
                    if 0<=x+dx<len(grid) and 0<=y+dy<len(grid[0]) and (x+dx, y+dy) not in seen:
                        if grid[x+dx][y+dy]==0:
                            seen.append((x+dx, y+dy))
                            heapq.heappush(Q, (k+1, x+dx, y+dy))
                        else:
                            seen.append((x+dx, y+dy))
                            heapq.heappush(Q, (k, x+dx, y+dy))