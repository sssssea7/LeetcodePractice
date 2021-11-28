class Solution:
    def allPathsSourceTarget(self, G: List[List[int]]) -> List[List[int]]:
        self.ans = []
        def dfs(node, cur):
            if cur[-1]==len(G)-1: 
                self.ans.append(cur)
                return
            for n in node:
                dfs(G[n], cur+[n])
        dfs(G[0], [0])
        return self.ans