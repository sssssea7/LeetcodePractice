class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        arr = set()
        for i in range(len(s)-k+1):
            arr.add(s[i:i+k])
        return len(arr)==2**k