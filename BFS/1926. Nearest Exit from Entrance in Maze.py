# https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/
class Solution:
    def nearestExit(self, A: List[List[str]], entrance: List[int]) -> int:
        m, n = len(A), len(A[0])
        Q = [(entrance[0], entrance[1], 0)]
        A[entrance[0]][entrance[1]]='*'
        while Q:
            x, y, step = Q.pop(0)
            if (x==0 or x==m-1 or y==0 or y==n-1) and [x, y]!=entrance:
                return step
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if 0<=x+dx<m and 0<=y+dy<n and A[x+dx][y+dy]==".":
                    A[x+dx][y+dy] = '*'
                    Q.append([x+dx, y+dy, step+1])
        return -1