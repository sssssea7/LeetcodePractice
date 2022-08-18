class Solution:
    def firstUniqChar(self, s: str) -> int:
        cand = [k for k, v in Counter(s).items() if v==1]
        for i in range(len(s)):
            if s[i] in cand:
                return i
        return -1