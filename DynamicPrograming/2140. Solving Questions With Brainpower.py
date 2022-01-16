class Solution:
    def mostPoints(self, A: List[List[int]]) -> int:
        @cache
        def dfs(i):
            if i>=len(A): return 0
            return max(A[i][0]+dfs(i+A[i][1]+1), dfs(i+1))
        return dfs(0)