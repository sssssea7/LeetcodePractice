# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        self.X, self.Y = None, None
        def dfs(node, d, p):
            if not node: return
            if node.val==x: self.X=[d, p] 
            if node.val==y: self.Y=[d, p]
            dfs(node.left, d+1, node)
            dfs(node.right, d+1, node)
        dfs(root, 0, None)
        if self.X[0]==self.Y[0] and self.X[1]!=self.Y[1]:
            return True
        else:
            return False