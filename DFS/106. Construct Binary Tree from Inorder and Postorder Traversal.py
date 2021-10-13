# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, I: List[int], P: List[int]) -> Optional[TreeNode]:
        def dfs(I, P):
            if not I and not P: return None
            node = TreeNode(P.pop())
            idx = I.index(node.val)
            node.left = dfs(I[:idx], P[:idx])
            node.right = dfs(I[idx+1:], P[idx:])
            return node
        return dfs(I, P)