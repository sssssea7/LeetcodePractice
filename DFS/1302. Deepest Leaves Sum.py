# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        L = defaultdict(list)
        def dfs(node, d):
            if not node: return
            if not node.left and not node.right: L[d].append(node.val)
            dfs(node.left, d+1)
            dfs(node.right, d+1)
        dfs(root, 0)
        L_max = sorted(L.items(), key=lambda x:x[0])
        return sum(L_max[-1][1])