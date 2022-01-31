class Solution:
    def maximumWealth(self, A: List[List[int]]) -> int:
        return max([sum(a) for a in A])