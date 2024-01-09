class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        self.T = defaultdict(list)
        def dfs(node, d):
            if not node: return
            self.T[d].append(node.val)
            dfs(node.left, d+1)
            dfs(node.right, d+1)
        dfs(root, 1)
        ans, sm = 0, -inf
        for k, v in self.T.items():
            if sum(v)>sm: 
                ans = k
                sm = sum(v)
        return ans

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        self.D = defaultdict(list)
        def dfs(node, d):
            if not node: return            
            self.D[d].append(node.val)
            dfs(node.left, d+1)
            dfs(node.right, d+1)
        dfs(root, 1)
        self.D = sorted(self.D.items(), key=lambda x: (sum(x[1], -x[0])))
        # print(self.D)
        return self.D[-1][0]