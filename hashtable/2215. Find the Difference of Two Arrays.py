# https://leetcode.com/problems/find-the-difference-of-two-arrays/
class Solution:
    def findDifference(self, A: List[int], B: List[int]) -> List[List[int]]:
        cnt1 = Counter(A)
        cnt2 = Counter(B)
        return [list(A-cnt2.keys()), list(B-cnt1.keys())]

class Solution:
    def findDifference(self, A: List[int], B: List[int]) -> List[List[int]]:
        return [set(A)-set(B), set(B)-set(A)]