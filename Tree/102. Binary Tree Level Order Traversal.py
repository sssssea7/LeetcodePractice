# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        T = defaultdict(list)
        def dfs(node, d):
            if not node: return
            T[d].append(node.val)
            dfs(node.left, d+1)
            dfs(node.right, d+1)
        dfs(root, 0)
        return [v for k, v in T.items()]


class Solution:
def levelOrder(self, root: TreeNode) -> List[List[int]]:
    if not root: return []
    ans = []
    Q = [root]
    while Q:
        lvl = []
        for _ in range(len(Q)):
            curr = Q.pop(0)
            lvl.append(curr.val)
            if curr.left: Q.append(curr.left)
            if curr.right: Q.append(curr.right)
        ans.append(lvl)
    return ans

    
# template
# deftree_BFS(self, root: TreeNode) -> int:
#  queue = [root]
# `define ans`
# while queue:
# for _ inrange(len(queue)):
#  cur = queue.pop(0)
# if cur.left: queue.append(cur.left)
# if cur.right: queue.append(cur.right)
# return`define ans`

