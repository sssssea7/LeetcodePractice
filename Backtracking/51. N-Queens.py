# https://leetcode.com/problems/n-queens/

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def check(i, j):
            # row
            if i in seen_row:
                return False
            # col
            if j in seen_col:
                return False
            # diag
            if i-j in seen_diag:
                return False
            # inv diag
            if i+j in seen_inv_diag:
                return False
            return True

        ans = []
        path = []
        seen_row, seen_col, seen_diag, seen_inv_diag = [], [], [], []

        def dfs(i):
            if i==n:
                ans.append(path.copy())
                return
            for j in range(n):
                cand = '.'*j+'Q'+'.'*(n-j-1)
                # print(cand)
                if check(i, j):
                    seen_row.append(i)
                    seen_col.append(j)
                    seen_diag.append(i-j)
                    seen_inv_diag.append(i+j)
                    path.append(cand)
                    dfs(i+1)
                    seen_row.pop()
                    seen_col.pop()
                    seen_diag.pop()
                    seen_inv_diag.pop()
                    path.pop()
        dfs(0)
        return ans

                    

