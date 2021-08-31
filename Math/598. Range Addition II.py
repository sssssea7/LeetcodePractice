class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        for i, j in ops:
            m = min(m, i)
            n = min(n, j)
        return m*n