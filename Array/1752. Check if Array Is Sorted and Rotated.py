# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/

class Solution:
    def check(self, A: List[int]) -> bool:
        rotate = 1
        for i in range(len(A)):
            if A[i] < A[i-1]:
                rotate -= 1
            if rotate < 0:
                return False
        return True
        