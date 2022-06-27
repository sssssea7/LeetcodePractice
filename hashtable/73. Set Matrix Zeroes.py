class Solution:
    def setZeroes(self, A: List[List[int]]) -> None:
        row, col = set(), set()
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j]==0:
                    row.add(i)
                    col.add(j)
        for i in range(len(A)):
            for j in range(len(A[0])):
                if i in row or j in col:
                    A[i][j]=0