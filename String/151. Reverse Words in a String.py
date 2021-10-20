class Solution:
    def reverseWords(self, s: str) -> str:
        A = s.split()
        return " ".join(A[::-1])