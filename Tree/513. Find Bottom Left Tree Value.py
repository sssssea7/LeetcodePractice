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