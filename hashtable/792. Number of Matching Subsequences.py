class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        ans = 0
        # build simple trie
        D = defaultdict(list)
        for w in words: 
            D[w[0]].append(w)
        for c in s:
            W = D[c]
            D[c] = [] 
            # query and update trie
            for w in W:
                if len(w)>1: D[w[1]].append(w[1:])
                else: ans += 1
        return ans
            