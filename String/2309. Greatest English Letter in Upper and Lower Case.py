# https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case/description/

class Solution:
    def greatestLetter(self, s: str) -> str:
        cnt = Counter(s)
        cnt2 = Counter(cnt.keys())
        ht = {}
        for k, v in cnt2.items():
            if k.upper() not in ht:
                ht[k.upper()] = 1
            else:
                ht[k.upper()] += 1
        ht = sorted(ht.items(), key=lambda x: x[0], reverse=True)
        for k, v in ht:
            if v>1:
                return k
        return ""
        