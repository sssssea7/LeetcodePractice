# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def dfs(node, Pre, In):
            if not In: return None
            node.val = Pre.pop(0)
            idx = In.index(node.val)
            node.left = dfs(TreeNode(0), Pre[:idx], In[:idx])
            node.right = dfs(TreeNode(0), Pre[idx:], In[idx+1:])
            return node
   
        return dfs(TreeNode(0), preorder, inorder)