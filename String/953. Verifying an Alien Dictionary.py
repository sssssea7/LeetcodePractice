class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i in range(len(words)-1):  #
            if words[i] == words[i+1]: continue
            if words[i+1] in words[i] and len(words[i+1]) < len(words[i]): return False
            for j in range(min(len(words[i]), len(words[i+1]))):
                # if order.index(words[i][j]) == order.index(words[i+1][j]): continue
                if order.index(words[i][j]) < order.index(words[i+1][j]): break
                if order.index(words[i][j]) > order.index(words[i+1][j]): return False
        return True