# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if node==p or node==q: return node
            if node.val > p.val and node.val>q.val:
                return dfs(node.left)
            if node.val < p.val and node.val<q.val:
                return dfs(node.right)
            return node
            
        return dfs(root)

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or p==root or q==root:
            return root
        if root.val > p.val and root.val>q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if root.val < p.val and root.val<q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root