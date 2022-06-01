class Solution:
    def runningSum(self, A: List[int]) -> List[int]:
        for i in range(1, len(A)):
            A[i] += A[i-1]
        return A