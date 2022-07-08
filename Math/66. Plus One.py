class Solution:
    def plusOne(self, A: List[int]) -> List[int]:
        A[-1] += 1
        i = len(A)-1
        while A[i]==10:
            A[i] = 0
            if i!=0:
                A[i-1] += 1
            else:
                A = [1] + A
            i -= 1
        return A


class Solution:
    def plusOne(self, A: List[int]) -> List[int]:
        A = int("".join([str(a) for a in A]))
        A += 1
        return [int(a) for a in str(A)]
            