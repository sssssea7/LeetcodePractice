class Solution(object):
    def lcaDeepestLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def dfs(node):
            if not node: return 0, None
            ld, ln = dfs(node.left)
            rd, rn = dfs(node.right)
            if ld < rd: return rd+1, rn
            elif ld > rd: return ld+1, ln
            else: return ld+1, node
        return dfs(root)[1]