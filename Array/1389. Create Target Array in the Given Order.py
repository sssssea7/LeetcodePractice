class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        t = []
        for i, n in zip(index, nums):
            # t[i:i] = [n]
            t.insert(i,n)
        return t