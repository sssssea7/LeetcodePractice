# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node: return 0, 0
            if not node.left and not node.right:
                return 0, node.val
            
            ld, lv = dfs(node.left)
            rd, rv = dfs(node.right)
            
            if ld==rd: return 1+ld, lv+rv
            if ld>rd: return ld+1, lv
            else: return rd+1, rv
        
        return dfs(root)[1]
            