class Solution:
    def numTilings(self, n: int) -> int:
        @cache
        def fn(n):
            if n==1: return 1
            if n==2: return 2
            if n==3: return 5
            return 2*fn(n-1)+fn(n-3)
        return fn(n)%(10**9+7)