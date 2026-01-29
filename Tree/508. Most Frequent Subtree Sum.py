# https://leetcode.com/problems/most-frequent-subtree-sum/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        cnt = Counter()
        def dfs(node):
            if not node: return 0
            s = node.val + dfs(node.left) + dfs(node.right)
            cnt[s] += 1
            return s

        dfs(root)
        mx_cnt = max(cnt.values())
        return [s for s in cnt if cnt[s]==mx_cnt]

