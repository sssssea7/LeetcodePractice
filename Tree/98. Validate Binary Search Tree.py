# https://leetcode.com/problems/validate-binary-search-tree/description/

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, l, r):
            if not node: return True
            return l < node.val < r and dfs(node.left, l, node.val) and dfs(node.right, node.val, r)
        return dfs(root, -inf, inf)