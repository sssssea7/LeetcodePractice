# https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        self.D = defaultdict(list)
        def dfs(node, d):
            if not node: return
            self.D[d].append(node.val)
            dfs(node.left, d+1)
            dfs(node.right, d+1)
        dfs(root, 0)
        sm = [sum(v) for k, v in self.D.items()]
        sm.sort(reverse=True)
        # print(sm)
        return sm[k-1] if len(self.D)>k-1 else -1