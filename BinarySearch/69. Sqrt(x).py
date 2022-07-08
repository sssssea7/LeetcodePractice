class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x+1
        while l<r:
            m = (l+r)//2
            if m*m>x: r = m
            else: l = m+1
        return l-1


class Solution:
    def mySqrt(self, x: int) -> int:
        for i in range(46341):
            if i*i<=x<(i+1)*(i+1): return i