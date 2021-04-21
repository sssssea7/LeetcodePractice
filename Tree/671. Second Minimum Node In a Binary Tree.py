# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        arr = []
        def dfs(node):
            if not node: return
            if node.val not in arr: arr.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        if len(arr)==1: return -1
        return sorted(arr)[1]