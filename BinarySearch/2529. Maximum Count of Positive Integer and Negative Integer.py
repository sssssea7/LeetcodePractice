# https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/description/

class Solution:
    def maximumCount(self, A: List[int]) -> int:
        
        def bs(A, t):
            l, r = 0, len(A)
            while l<r:
                m = (l+r)//2
                if A[m]>t:
                    r = m
                else:
                    l = m+1
            return l
        
        start = bs(A, -1)
        end = bs(A, 0)
        return max(start, len(A)-end)
