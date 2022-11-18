class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        cnt = Counter(s)
        if len(set([v for k, v in cnt.items()]))==1:
            return True
        return False
            