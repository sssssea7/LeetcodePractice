# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(node, cur):
            if not node: return
            if not node.left and not node.right: 
                self.ans += int(cur+str(node.val), 2)
                return
            dfs(node.left, cur+str(node.val))
            dfs(node.right, cur+str(node.val))
        dfs(root, "")
        return self.ans

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node, cur):
            if not node: return 0
            if not node.left and not node.right: 
                return 2*cur+node.val
            l = dfs(node.left, 2*cur+node.val)
            r = dfs(node.right, 2*cur+node.val)
            return l+r
        return dfs(root, 0)