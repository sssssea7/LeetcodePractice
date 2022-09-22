# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0
        def dfs(node, path):
            if not node: return
            if len(path) == sum([1 for n in path if node.val>=n]):
                self.ans += 1                
            dfs(node.left, path+[node.val])
            dfs(node.right, path+[node.val])
        dfs(root, [])
        return self.ans 