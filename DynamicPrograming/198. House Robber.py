class Solution:
    def rob(self, A: List[int]) -> int:
        @cache
        def fn(i):
            if i>=len(A): return 0
            else: return max(fn(i+1), A[i]+fn(i+2))
        return fn(0)