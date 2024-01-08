# https://leetcode.com/problems/equal-row-and-column-pairs/
class Solution:
    def equalPairs(self, A: List[List[int]]) -> int:
        cnt1 = Counter(map(tuple, A))
        cnt2 = Counter(zip(*A))
        return sum([v1*v2 for k1, v1 in cnt1.items() for k2, v2 in cnt2.items() if k1==k2])
        