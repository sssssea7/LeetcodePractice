# https://leetcode.com/problems/n-queens-ii/

class Solution:
    def totalNQueens(self, n: int) -> int:
        col_seen = []
        diag_seen = []
        inv_diag_seen = []
        def is_valid(i, j):
            if j not in col_seen and i-j not in diag_seen and i+j not in inv_diag_seen:
                return True
            return False
        
        self.ans = 0
        def dfs(i):
            if i==n:
                self.ans += 1
                return
            for j in range(n):
                if is_valid(i, j):
                    col_seen.append(j)
                    diag_seen.append(i-j)
                    inv_diag_seen.append(i+j)
                    dfs(i+1)
                    col_seen.pop()
                    diag_seen.pop()
                    inv_diag_seen.pop()
        dfs(0)
        return self.ans
                