class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        Bcounter = Counter(B[0])
        for b in B:
            Bcounter = Bcounter|Counter(b)
        Acounter = [Counter(a) for a in A]
        ans = []
        for i in range(len(Acounter)):
            if Acounter[i]|Bcounter == Acounter[i]: ans.append(A[i])
        return ans