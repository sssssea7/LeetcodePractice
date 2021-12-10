class Solution:
    def longestCommonSubsequence(self, A: str, B: str) -> int:
        @cache
        def dfs(i, j):
            if i==len(A) or j == len(B): return 0
            if A[i]==B[j]: return 1+dfs(i+1, j+1)
            else: return max(dfs(i+1, j), dfs(i, j+1))
        return dfs(0, 0)