# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], t: int) -> bool:
        def dfs(node, t):
            if not node: return False
            if not node.left and not node.right and t==node.val: return True
            return dfs(node.left, t-node.val) or dfs(node.right, t-node.val)
        return dfs(root, t)
                

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], t: int) -> bool:
        def dfs(node, sm):
            if not node: return False
            if not node.left and not node.right and sm+node.val == t: return True
            l = dfs(node.left, sm+node.val)
            r = dfs(node.right, sm+node.val)
            return l or r

        return dfs(root, 0)
