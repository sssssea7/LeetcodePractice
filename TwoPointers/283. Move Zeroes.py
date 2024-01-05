# https://leetcode.com/problems/move-zeroes/
class Solution:
    def moveZeroes(self, A: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j in range(len(A)):
            if A[j]!=0:
                A[i], A[j] = A[j], A[i]
                i += 1
            