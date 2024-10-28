# https://leetcode.com/problems/longest-word-in-dictionary/
class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = {}
        for f in words:
            node = trie
            for c in f:
                node = node.setdefault(c, {})
            node['#'] = f
        
        
        def dfs(node):
            # print(node)
            ans = ""
            if "#" in node:
                ans = node["#"]
            # ans = node.get('#', '')
            for n in node:
                if '#' not in node[n]: continue
                nxt = dfs(node[n])
                if len(nxt)>len(ans) or (len(nxt)==len(ans) and nxt<ans):
                    ans = nxt
                    
            return ans
        
        return dfs(trie)