# https://leetcode.com/problems/sum-of-left-leaves/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(node):
            if not node: return 0
            dfs(node.left)
            dfs(node.right)
            if node.left and not node.left.left and not node.left.right:
                self.ans += node.left.val

        dfs(root)    
        
        return self.ans


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node, l=False):
            if not node: return 0
            if not node.left and not node.right and l: return node.val    
            return dfs(node.left, True)+dfs(node.right, False)
        return dfs(root, False)