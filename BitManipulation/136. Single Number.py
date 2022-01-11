class Solution:
    def singleNumber(self, n: List[int]) -> int:
        ans = 0
        for i in n:
            ans ^= i
        return ans