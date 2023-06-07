class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr = sorted(arr)     # arr.sort()
        for i in range(len(arr)-2):
            if arr[i+1]-arr[i] == arr[i+2]-arr[i+1]: continue
            return False
        return True

class Solution:
    def canMakeArithmeticProgression(self, A: List[int]) -> bool:
        A.sort()
        diff = A[1]-A[0]
        for i in range(2, len(A)):
            if A[i]-A[i-1] != diff:
                return False
        return True