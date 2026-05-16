# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = -inf
        @cache
        def dfs(node):
            if not node: 
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            self.ans = max(self.ans, l+r+node.val)
            return max(0, max(l, r) + node.val)
        dfs(root)
        return self.ans