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


class Solution:
    def maxDistToClosest(self, A: List[int]) -> int:
        ans = A.index(1)
        A.reverse()
        ans = max(ans, A.index(1))
        for k, v in groupby(A):
            if not k:
                ans = max(ans, (len(list(v))+1)//2)
        return ans