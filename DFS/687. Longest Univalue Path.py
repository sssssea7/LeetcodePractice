# https://leetcode.com/problems/longest-univalue-path/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        @cache
        def dfs(node):
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            if node.left and node.val != node.left.val:
                l = 0
            if node.right and node.val != node.right.val:
                r = 0
            self.ans = max(self.ans, l+r)
            return max(l, r) + 1
        dfs(root)
        return self.ans