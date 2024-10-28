# https://leetcode.com/problems/rank-transform-of-an-array/

class Solution:
    def arrayRankTransform(self, A: List[int]) -> List[int]:
        B = sorted(A)
        ht = {}
        idx = 1
        for b in B:
            if b not in ht:
                ht[b] = idx
                idx += 1
        
        return [ht[a] for a in A]