# https://leetcode.com/problems/sum-root-to-leaf-numbers/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans = []
        def dfs(node, n):
            if not node: return 
            if not node.left and not node.right: 
                self.ans.append(int(n+str(node.val)))
            dfs(node.left, n+str(node.val))
            dfs(node.right, n+str(node.val))
        dfs(root, "")
        return sum(map(int, self.ans))

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(node, d):
            if not node: return 
            if not node.left and not node.right:
                self.ans += int(d+str(node.val))
            dfs(node.left, d+str(node.val))
            dfs(node.right, d+str(node.val))
        dfs(root, "")
        return self.ans