class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        freq = k
        for n in nums:
            if n == 0: freq += 1
            elif freq >=k: freq = 0
            else: return False
        return True