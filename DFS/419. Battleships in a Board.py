# https://leetcode.com/problems/battleships-in-a-board/description/

class Solution:
    def countBattleships(self, A: List[List[str]]) -> int:
        
        def dfs(x, y):
            A[x][y] = "."
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0<=x+dx<len(A) and 0<=y+dy<len(A[0]) and A[x+dx][y+dy]=="X":
                    dfs(x+dx, y+dy)
        
        ans = 0
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == "X":
                    dfs(i, j)
                    ans += 1
        return ans