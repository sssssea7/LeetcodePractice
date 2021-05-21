class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        x = sorted(nums)[len(nums)//2]
        return sum([abs(n-x) for n in nums])