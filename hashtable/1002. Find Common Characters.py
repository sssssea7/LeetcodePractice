class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        A = [Counter(a) for a in A]
        j = A[0]
        for a in A:
            j &= a
        return list(j.elements())
        