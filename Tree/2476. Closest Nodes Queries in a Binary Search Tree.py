# https://leetcode.com/problems/closest-nodes-queries-in-a-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        A = []
        def dfs(node):
            if not node: return
            dfs(node.left)
            A.append(node.val)
            dfs(node.right)
        dfs(root)

        ans = []
        for q in queries:
            l = bisect_left(A, q)
            if l==0:
                if A[l]==q:
                    ans.append([A[0], A[0]])
                else:
                    ans.append([-1, A[0]])
            elif l==len(A):
                ans.append([A[-1], -1])
            elif A[l]==q:
                ans.append([q, q])
            else:
                ans.append([A[l-1], A[l]])
        return ans