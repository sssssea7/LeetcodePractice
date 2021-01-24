# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def dfs(original, cloned):
            if not original: return None
            if original == target: return cloned
            l = dfs(original.left, cloned.left)
            r = dfs(original.right, cloned.right)
            if l: return l
            return r
        return dfs(original, cloned)