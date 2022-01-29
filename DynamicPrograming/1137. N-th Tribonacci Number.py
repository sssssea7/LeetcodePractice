class Solution:
    def tribonacci(self, n: int) -> int:
        @cache
        def fn(i):
            if i<2: return i
            if i==2: return 1
            return fn(i-1)+fn(i-2)+fn(i-3)
        return fn(n)