class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        self.ans = [0]        
        def dfs(node, d):
            if not node: return 
            self.ans.append(d)
            for n in node.children:
                dfs(n, d+1)
        dfs(root, 1)
        return max(self.ans)