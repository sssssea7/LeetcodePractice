class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        T = defaultdict(list)
        def dfs(node, d):
            if not node: return
            T[d].append(node.val)
            dfs(node.left, d+1)
            dfs(node.right, d+1)
        dfs(root, 0)
        return [sum(v)/len(v) for k, v in T.items()]