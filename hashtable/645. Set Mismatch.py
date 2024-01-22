# https://leetcode.com/problems/set-mismatch/
class Solution:
    def findErrorNums(self, A: List[int]) -> List[int]:
        B = [1] + [0]*len(A)
        for x in A:
            B[x] += 1
        a, b = 0, 0
        for i, x in enumerate(B):
            if x==2: a = i
            if x==0: b = i
        return [a, b]