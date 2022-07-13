class Solution:
    def containsDuplicate(self, A: List[int]) -> bool:
        return len(A)!=len(set(A))