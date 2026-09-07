# https://leetcode.com/problems/word-search/

# both solutions work, but the first one changes the board back to its original state after each dfs call, which is safer in case of multiple calls. The second solution does not restore the board state after a successful path is found, which could lead to incorrect results if the function is called multiple times with the same board.
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        
        def dfs(x, y, index):
            if index==len(word):
                return True
            original = board[x][y]
            board[x][y] = "#"
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if 0<=x+dx<n and 0<=y+dy<m and board[x+dx][y+dy] == word[index]:
                    if dfs(x+dx, y+dy, index+1):
                        board[x][y] = original
                        return True
            board[x][y] = original
            return False
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if dfs(i, j, 1):
                        return True
                    
        return False

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        
        def dfs(x, y, index):
            if index==len(word):
                return True

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if 0<=x+dx<n and 0<=y+dy<m and board[x+dx][y+dy] == word[index]:
                    original = board[x][y]
                    board[x][y] = "#"
                    if dfs(x+dx, y+dy, index+1):
                        return True
                    board[x][y] = original
            return False
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if dfs(i, j, 1):
                        return True
                    
        return False