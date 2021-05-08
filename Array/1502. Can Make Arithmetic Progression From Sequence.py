class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr = sorted(arr)     # arr.sort()
        for i in range(len(arr)-2):
            if arr[i+1]-arr[i] == arr[i+2]-arr[i+1]: continue
            return False
        return True