class Solution:
    def intersection(self, A: List[int], B: List[int]) -> List[int]:
        return set(A)&set(B)