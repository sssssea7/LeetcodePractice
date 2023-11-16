class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        ans = 0
        for i in range(limit+1):
            mx = min(limit, n-i)
            mn = max(0, n-i-mx)
            if 0<=mx<=limit and 0<=mn<=limit:
                ans += mx-mn+1
        return ans