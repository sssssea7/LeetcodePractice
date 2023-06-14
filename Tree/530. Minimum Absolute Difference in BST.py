class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.pre = -inf
        self.ans = inf
        def dfs(node):
            if not node: return
            dfs(node.left)
            self.ans = min(self.ans, abs(node.val-self.pre))
            self.pre = node.val
            dfs(node.right)
        dfs(root)
        return self.ans

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.A = []
        def dfs(node):
            if not node: return
            dfs(node.left)
            self.A.append(node.val)
            dfs(node.right)
        dfs(root)    
        return min([abs(x-y) for x, y in pairwise(self.A)])