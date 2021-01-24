class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        self.ans = 0
        #self.ans = Set()
        def dfs(node):
            if not node: return
            dfs(node.left)
            dfs(node.right)
            if node.val>=low and node.val<=high: self.ans += node.val
        dfs(root)
        return self.ans