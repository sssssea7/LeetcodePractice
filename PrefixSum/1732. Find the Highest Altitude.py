# https://leetcode.com/problems/find-the-highest-altitude/
class Solution:
    def largestAltitude(self, A: List[int]) -> int:
        A = [0]+A
        pre = list(accumulate(A))
        return max(pre)