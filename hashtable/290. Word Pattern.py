class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(pattern) != len(s): return False
        P, S = {}, {}
        pp, ss = "", ""
        
        for i in range(len(s)):
            if pattern[i] not in P: P[pattern[i]] = len(P)
            pp += str(P[pattern[i]])
            if s[i] not in S: S[s[i]] = len(S)
            ss += str(S[s[i]])
        return pp==ss