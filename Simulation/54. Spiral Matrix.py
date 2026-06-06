# https://leetcode.com/problems/spiral-matrix/description/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len(matrix[0])
        row_start, col_start = 0, 0
        row_end, col_end = n, m
        ans = []
        while len(ans)<n*m:
            for j in range(col_start, col_end):
                ans.append(matrix[row_start][j])
            
            for i in range(row_start+1, row_end):
                ans.append(matrix[i][col_end-1])

            if len(ans)==n*m:
                break

            for j in range(col_end-2, col_start-1, -1):
                ans.append(matrix[row_end-1][j])
            
            for i in range(row_end-2, row_start, -1):
                ans.append(matrix[i][col_start])

            row_start += 1
            row_end -= 1
            col_start += 1
            col_end -= 1
        return ans