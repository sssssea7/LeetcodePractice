class NumMatrix:

    def __init__(self, A: List[List[int]]):
        self.prefix = [[0 for _ in range(len(A[0])+1)] for _ in range(len(A)+1)]
        for i in range(len(A)):
            for j in range(len(A[0])):
                self.prefix[i+1][j+1] = A[i][j]+self.prefix[i+1][j]+self.prefix[i][j+1]-self.prefix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefix[row2+1][col2+1]-self.prefix[row2+1][col1]-self.prefix[row1][col2+1]+self.prefix[row1][col1]