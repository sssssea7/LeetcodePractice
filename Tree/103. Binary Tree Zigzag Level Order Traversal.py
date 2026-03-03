# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        ans = []
        Q = [root]
        from_left = False
        while Q:
            lvl = []
            for _ in range(len(Q)):
                cur = Q.pop(0)
                lvl.append(cur.val)
                if cur.left: Q.append(cur.left)
                if cur.right: Q.append(cur.right)
            from_left = not from_left
            ans.append(lvl if from_left else lvl[::-1])
        return ans
