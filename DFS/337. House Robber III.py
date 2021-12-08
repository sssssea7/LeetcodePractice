# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @cache
        def dfs(node):
            if not node: return 0
            ans =  node.val
            if node.left: ans += dfs(node.left.left)+dfs(node.left.right)
            if node.right: ans += dfs(node.right.left)+dfs(node.right.right)
            return max(ans, dfs(node.left)+dfs(node.right))
        return dfs(root)