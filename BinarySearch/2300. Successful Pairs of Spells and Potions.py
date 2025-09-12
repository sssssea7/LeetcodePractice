# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/description/

class Solution:
    def successfulPairs(self, S: List[int], P: List[int], success: int) -> List[int]:
        P.sort()
        def find_min(s, P, success):
            l, r = 0, len(P)
            while l<r:
                m = (l+r)//2
                if s*P[m]>=success:
                    r = m
                else:
                    l = m + 1
            return l

        ans = []
        for i in range(len(S)):
            p_l = find_min(S[i], P, success)
            ans.append(len(P)-p_l)
        return ans

class Solution:
    def successfulPairs(self, S: List[int], P: List[int], success: int) -> List[int]:
        P.sort()
        ans = []
        for s in S:
            p_l = bisect_right(P, (success-1)//s)
            ans.append(len(P)-p_l)
        return ans