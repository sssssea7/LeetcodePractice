class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        return min(len(list(filter(lambda x:(x%2!=0), position))), len(list(filter(lambda x:x%2==0, position))))
        

# Counter to count the # of odd/even nums
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        c = Counter(c%2 for c in position)
        return min(c[0], c[1]) 