# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        Q = [[root, 0]]
        ans = 0
        while Q:
            ans = max(ans, Q[-1][1]-Q[0][1]+1)
            for i in range(len(Q)):
                node, _ = Q.pop(0)
                if node.left:
                    Q.append([node.left, 2*i])
                if node.right:
                    Q.append([node.right, 2*i+1])
        return ans