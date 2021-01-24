# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution(object):
    def pseudoPalindromicPaths (self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        def dfs(node, p):
            if not node: return
            if not node.left and not node.right: 
                p += [node.val]
                cnt = collections.Counter(p)
                self.ans += sum([v%2 for v in cnt.values()])<2
            
            dfs(node.left, p+[node.val])
            dfs(node.right, p+[node.val])
        dfs(root, [])
        return self.ans
            
            