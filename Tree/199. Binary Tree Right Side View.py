# https://leetcode.com/problems/binary-tree-right-side-view/

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def dfs(node, d):
            if not node: return
            if d==len(ans):
                ans.append(node.val)
            dfs(node.right, d+1)
            dfs(node.left, d+1)
        dfs(root, 0)
        return ans


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        tree = collections.defaultdict(list)
        def dfs(node, d):
            if not node: return
            tree[d].append(node)
            dfs(node.left, d+1)
            dfs(node.right, d+1)
        dfs(root,0)
        return [v[-1].val for k,v in tree.items()]
    

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: return []
        T, ans = [root], []
        while T:
            ans.append(T[-1].val)
            for _ in range(len(T)):
                curr = T.pop(0)
                if curr.left: T.append(curr.left)
                if curr.right: T.append(curr.right)
        return ans


