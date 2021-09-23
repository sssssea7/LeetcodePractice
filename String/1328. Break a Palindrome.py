class Solution:
    def breakPalindrome(self, S: str) -> str:
        if len(S) == 1: return ""
        for i in range(len(S)//2):
            if S[i] != "a":
                return S[:i] + "a" + S[(i+1):]
        return S[:-1]+"b"