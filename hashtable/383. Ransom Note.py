class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt1 = Counter(ransomNote)
        cnt2 = Counter(magazine)
        return cnt1<=cnt2


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt1 = Counter(ransomNote)
        cnt2 = Counter(magazine)
        for k, v in cnt1.items():
            if v<=cnt2[k]: continue
            else: return False
        return True