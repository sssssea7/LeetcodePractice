
class Solution:
    def isToeplitzMatrix(self, A: List[List[int]]) -> bool:
        diag = {}
        for i in range(len(A)):
            for j in range(len(A[0])):
                if i-j not in diag:
                    diag[i-j] = A[i][j]
                elif diag[i-j] != A[i][j]:
                    return False
        return True

class Solution:
    def isToeplitzMatrix(self, A: List[List[int]]) -> bool:
        D = defaultdict(list)
        for i in range(len(A)):
            for j in range(len(A[0])):
                D[i-j].append(A[i][j])
        for k, v in D.items():
            if len(set(v))!=1: return False
        return True