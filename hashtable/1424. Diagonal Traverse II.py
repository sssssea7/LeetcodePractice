class Solution:
    def findDiagonalOrder(self, A: List[List[int]]) -> List[int]:
        D = defaultdict(list)
        for i in range(len(A)):
            for j in range(len(A[i])):
                D[i+j].append(A[i][j])
        ans = []
        for k, v in D.items():
            ans.extend(v[::-1])
        return ans