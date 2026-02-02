# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/


class Solution:
    def searchRange(self, A: List[int], target: int) -> List[int]:
        def lower_bound(A, t):
            l, r = 0, len(A)
            while l<r:
                m = (l+r)//2
                if A[m]>=t: r=m
                else: l = m+1
            return l
        start = lower_bound(A, target)
        if start==len(A) or A[start]!=target:
            return [-1, -1]
        end = lower_bound(A, target+1)
        return [start, end-1]

        
class Solution:
    def searchRange(self, A: List[int], t: int) -> List[int]:
        # if t not in A: return [-1, -1]
        def lower_bound(A, t):
            l, r = 0, len(A)-1
            while l<=r:
                m = (l+r)//2
                if A[m] < t:
                    l = m + 1
                else:
                    r = m - 1
            return l

        start = lower_bound(A, t)
        if start == len(A) or A[start] != t:
            return [-1, -1]
        end = lower_bound(A, t+1)
        return [start, end-1]


