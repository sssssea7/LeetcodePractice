class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        # ref: https://leetcode.com/problems/find-and-replace-pattern/discuss/161288/C%2B%2BJavaPython-Normalise-Word
        def F(w):
            m = {}
            return [m.setdefault(c, len(m)) for c in w]
        return [w for w in words if F(w) == F(p)]
        

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def convert(word):
            ht = {}
            arr = []
            for c in word:
                if c not in ht: ht[c] = len(ht)
                arr.append(ht[c])
            return arr
        p = convert(pattern)
        return [w for w in words if convert(w) == p]