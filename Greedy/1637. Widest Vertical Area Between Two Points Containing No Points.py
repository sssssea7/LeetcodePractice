class Solution:
    def maxWidthOfVerticalArea(self, A: List[List[int]]) -> int:
        return max([(j-i) for (i, _), (j, _) in pairwise(sorted(A))])