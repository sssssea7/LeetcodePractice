class Solution:
    def removeElement(self, A: List[int], val: int) -> int:
        i = 0
        for j in range(len(A)):
            if A[j]!=val:
                A[i], A[j] = A[j], A[i]
                i += 1
        return i