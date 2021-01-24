class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def dfs(node):
            if not node: return True
            if node.left:
                if node.left.val == node.val: l = dfs(node.left)
                else: l = False
            else: l = True
            if node.right:
                if node.right.val == node.val: r = dfs(node.right)
                else: r = False
            else: r = True
            return l and r    
                
        return dfs(root)