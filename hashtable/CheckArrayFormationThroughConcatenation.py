class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        mp, i = {p[0]: p for p in pieces}, 0
        while i < len(arr):
            if arr[i] in mp and arr[i:i+len(mp[arr[i]])] == mp[arr[i]]: i += len(mp[arr[i]])
            else: return False
        return True
        