class Solution:
    def numIslands(self, A: List[List[str]]) -> int:
        D = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def dfs(x, y):
            A[x][y] = "0"
            for dx, dy in D:
                if 0<=x+dx<len(A) and 0<=y+dy<len(A[0]) and A[x+dx][y+dy]=="1":
                    dfs(x+dx, y+dy)
        ans = 0            
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j]=="1": 
                    dfs(i, j)
                    ans += 1
        return ans