class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        lo, hi = 1, m*n
        while lo < hi: 
            mid = (lo + hi)//2
            cnt = sum(min(n, mid//(i+1)) for i in range(m))
            if cnt < k: lo = mid + 1
            else: hi = mid 
        return lo
            