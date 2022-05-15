"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        T = defaultdict(list)
        def dfs(node, d):
            if not node: return
            T[d].append(node)
            dfs(node.left, d+1)
            dfs(node.right, d+1)
        dfs(root, 0)
        for _, v in T.items():
            for i in range(len(v)-1):
                v[i].next = v[i+1]
        return root