class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.ans = True
        def dfs(node, d):
            if not node: return d
            l = dfs(node.left, d+1)
            r = dfs(node.right, d+1)
            if abs(l-r)>1: self.ans=False
            return max(l, r)
        dfs(root, 0)
        return self.ans


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.ans = True
        def dfs(node):
            if not node: return 0
            l = 1+dfs(node.left)
            r = 1+dfs(node.right)
            if abs(l-r)>1: self.ans = False
            return max(l, r)
        dfs(root)
        return self.ans