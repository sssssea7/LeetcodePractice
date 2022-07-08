class Solution:
    def strStr(self, A: str, B: str) -> int:
        if B not in A: return -1
        for i in range(len(A)-len(B)+1):
            if A[i:(i+len(B))]==B: return i