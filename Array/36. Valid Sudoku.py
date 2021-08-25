class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check(arr):
            seen = set()
            for n in arr:
                if n == ".": continue
                if n in seen: return False
                seen.add(n)
            return True
        
        for i in range(9):
            if not check(board[i]): return False
            
        for col in zip(*board):
            if not check(col): return False
            
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                cell = [board[p][q] for p in range(i,i+3) for q in range(j,j+3)]
                if not check(cell): return False
        return True