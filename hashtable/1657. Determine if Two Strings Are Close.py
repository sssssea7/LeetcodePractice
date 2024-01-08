# https://leetcode.com/problems/determine-if-two-strings-are-close/
class Solution:
    def closeStrings(self, A: str, B: str) -> bool:
        return set(A)==set(B) and sorted(Counter(A).values())==sorted(Counter(B).values())