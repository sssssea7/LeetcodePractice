class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        ht1 = collections.Counter(word1)
        ht2 = collections.Counter(word2)
        # if ht1.keys()==ht2.keys() and  collections.Counter(ht1.values()) == collections.Counter(ht2.values()):
        if ht1.keys()==ht2.keys() and  sorted(ht1.values()) == sorted(ht2.values()):
            return True
        return False