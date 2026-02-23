# https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        sms = []
        def dfs(node):
            if not node: return 0
            l = dfs(node.left)
            r = dfs(node.right)
            sm = l + r + node.val
            sms.append(sm)
            return sm
        
        total = dfs(root)
        ans = 0
        for sm in sms:
            ans = max(ans, sm * (total-sm))
        return ans % (10**9+7)