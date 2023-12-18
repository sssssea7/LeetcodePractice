class Solution:
    def maxProductDifference(self, A: List[int]) -> int:
        A.sort()
        return (A[-1]*A[-2])-(A[0]*A[1])