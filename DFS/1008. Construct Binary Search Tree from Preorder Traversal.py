# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, A: List[int]) -> Optional[TreeNode]:
        def dfs(vals):
            if not vals: return None
            v = vals.pop(0)
            node = TreeNode(v)
            idx = bisect_left(vals, v)
            node.left = dfs(vals[:idx])
            node.right = dfs(vals[idx:])
            return node
        return dfs(A)
    