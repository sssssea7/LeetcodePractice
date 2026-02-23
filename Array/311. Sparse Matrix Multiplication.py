# premium: Given two sparse matrices mat1 of size m x k and mat2 of size k x n, return the result of mat1 x mat2. You may assume that multiplication is always possible.

class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        ans = []
        for rol in mat1:
            cur = []
            for col in zip(*mat2):
                cur.append(sum(r * c for r, c in zip(rol, col)))
            ans.append(cur)
        return ans