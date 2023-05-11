class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        
        @cache
        def dp(i, j):
            if i==len(A) or j==len(B): return 0
            if A[i]==B[j]:
                return 1+dp(i+1, j+1)
            return max(dp(i+1, j), dp(i, j+1))
        return dp(0, 0)
                