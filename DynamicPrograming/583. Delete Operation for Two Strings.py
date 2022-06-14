class Solution:
    def minDistance(self, A: str, B: str) -> int:
        @cache
        def dp(i, j):
            if i==len(A) or j==len(B): return 0
            if A[i]==B[j]: return 1+dp(i+1, j+1)
            else: return max(dp(i+1, j), dp(i, j+1))
        lcs = dp(0, 0)
        return len(A)+len(B)-2*lcs