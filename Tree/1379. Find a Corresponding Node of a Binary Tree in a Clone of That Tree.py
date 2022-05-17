# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def dfs(node):
            if not node: return
            if node.val == target.val:
                self.ans = node
                return 
            dfs(node.left)
            dfs(node.right)
        dfs(cloned)
        return self.ans