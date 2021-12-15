# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], l: int, h: int) -> int:
        self.ans = 0
        def dfs(node):
            if not node: return
            dfs(node.left)
            dfs(node.right)
            if l<=node.val<=h: self.ans += node.val
        dfs(root)
        return self.ans