class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        ans = []
        def dfs(t):
            if not t: return
            ans.append(str(t.val))
            if t.left or (not t.left and t.right):
                ans.append("(")
                dfs(t.left)
                ans.append(")")
            if t.right:
                ans.append("(")
                dfs(t.right)
                ans.append(")")
        dfs(t)
        return ''.join(ans)