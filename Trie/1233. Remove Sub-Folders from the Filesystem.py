# https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = {}
        for f in folder:
            node = trie
            for c in f.split('/'):
                node = node.setdefault(c, {})
            node['#'] = f
        
        def dfs(node):
            if "#" in node:
                return [node["#"]]
            ans = []
            for n in node:
                ans.extend(dfs(node[n]))
            return ans
        
        ans = []
        def dfs(node):
            nonlocal ans
            if "#" in node:
                ans.append(node["#"])
                return 
            for n in node:
                dfs(node[n])
        dfs(trie)
        
        return ans
                