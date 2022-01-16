class Solution:
    def maxDistToClosest(self, A: List[int]) -> int:
        B = [[k, len(list(v))] for k, v in groupby(A)]
        d1, d2 = -1, -1
        if B[0][0] == 0: d1 = B[0][1]
        if B[-1][0] == 0: d2 = B[-1][1]
        B = sorted(B, key=lambda x:x[1], reverse=True)
        for a, b in B:
            if a==0:
                return max((b+1)//2, d1, d2)