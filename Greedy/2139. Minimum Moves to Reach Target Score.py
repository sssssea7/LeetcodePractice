class Solution:
    def minMoves(self, t: int, m: int) -> int:
        ans = 0
        while t>1 and m:
            if t%2==1:
                t -= 1
                ans += 1
            t //= 2
            m -= 1
            ans += 1
        return ans + t - 1