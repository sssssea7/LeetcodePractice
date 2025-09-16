# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0
        def dfs(node, mx):
            if not node: return
            if node.val>=mx: self.ans += 1
            dfs(node.left, max(mx, node.val))
            dfs(node.right, max(mx, node.val))
        dfs(root, -inf)
        return self.ans
        

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, mx):
            if not node: return 0
            l = dfs(node.left, max(mx, node.val))
            r = dfs(node.right, max(mx, node.val))
            return l + r + (node.val>=mx)
        return dfs(root,-inf)