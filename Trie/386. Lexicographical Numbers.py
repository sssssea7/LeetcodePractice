# https://leetcode.com/problems/lexicographical-numbers/
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        trie = {}
        for i in range(1, n+1):
            node = trie
            for c in str(i):
                node = node.setdefault(int(c), {})
            node['#'] = i
        
        def dfs(node):
            # print(node)
            ans = []
            if "#" in node:
                ans.append(node["#"])
            
            for n in node:
                if n!='#':
                    ans.extend(dfs(node[n]))
            return ans
            
        return dfs(trie)