class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sht, tht = {}, {}
        ss, tt = "", ""
        for i in range(len(s)):
            if s[i] not in sht:
                sht[s[i]] = len(sht)
            ss += str(sht[s[i]])
            if t[i] not in tht:
                tht[t[i]] = len(tht)
            tt += str(tht[t[i]])
        return ss==tt