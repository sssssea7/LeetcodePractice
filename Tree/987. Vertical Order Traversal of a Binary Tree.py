# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.D = defaultdict(list)
        def dfs(node, row, col):
            if not node: return
            self.D[col].append([row, node.val])
            dfs(node.left, row+1, col-1)
            dfs(node.right, row+1, col+1)
        dfs(root, 0, 0)
        ans = []
        for k, v in sorted(self.D.items()):
            v.sort()
            ans.append([vv for _, vv in v])
        return ans
