# https://leetcode.com/problems/find-bottom-left-tree-value/

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        Q = [root]
        while Q:
            node = Q.pop(0)
            if node.right: Q.append(node.right)
            if node.left: Q.append(node.left)
        return node.val

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        self.T = defaultdict(list)
        def dfs(node, d):
            if not node: return
            self.T[d].append(node.val)
            dfs(node.left, d+1)
            dfs(node.right, d+1)
        dfs(root, 0)
        return self.T[max(self.T)][0]