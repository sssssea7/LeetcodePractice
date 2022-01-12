# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        self.ans = []
        def dfs(node, path):
            if not node: return
            if not node.left and not node.right and sum(path)+node.val == targetSum:
                self.ans.append(path+[node.val])
            dfs(node.left, path + [node.val])
            dfs(node.right, path + [node.val])
        dfs(root, [])
        return self.ans