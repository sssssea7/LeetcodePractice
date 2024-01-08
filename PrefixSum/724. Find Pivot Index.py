# https://leetcode.com/problems/find-pivot-index/
class Solution:
    def pivotIndex(self, A: List[int]) -> int:
        prefix = list(accumulate(A))
        suffix = list(accumulate(A[::-1]))[::-1]
        for i, [p, s] in enumerate(zip(prefix, suffix)):
            if p==s:
                return i
        return -1