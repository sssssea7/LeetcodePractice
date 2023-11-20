class Solution:
    def minPairSum(self, A: List[int]) -> int:
        A.sort()
        return max([A[i]+A[len(A)-i-1] for i in range(len(A)//2)])