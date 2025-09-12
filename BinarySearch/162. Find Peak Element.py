# https://leetcode.com/problems/find-peak-element/description/

class Solution:
    def findPeakElement(self, A: List[int]) -> int:
        l, r = 0, len(A)-2
        while l<=r:
            m = (l+r)//2
            if A[m]>A[m+1]:
                r = m-1
            else:
                l = m+1
        return r+1

class Solution:
    def findPeakElement(self, A: List[int]) -> int:
        l, r = 0, len(A)-1
        while l<r:
            m = (l+r)//2
            if A[m]>A[m+1]:
                r = m
            else:
                l = m+1
        return l