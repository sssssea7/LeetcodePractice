"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        T = defaultdict(list)
        def dfs(node, d):
            if not node: return
            T[d].append(node.val)
            for child in node.children:
                dfs(child, d+1)
        dfs(root, 0)
        return [T[t] for t in T]