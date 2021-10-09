class Solution:
    def findWords(self, A: List[List[str]], words: List[str]) -> List[str]:
        self.trie = {}
        
        def insert(word):
            cur = self.trie
            for w in word:
                if w not in cur:
                    cur[w] = {}
                cur = cur[w]
            cur['#'] = 0
            
        for word in words:
            insert(word)
            
        D = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        self.ans = set()
        def dfs(x, y, T, W):
            if '#' in T and W not in self.ans:
                self.ans.add(W)
            for dx, dy in D:
                if 0<=x+dx<len(A) and 0<=y+dy<len(A[0]) and A[x+dx][y+dy] in T:
                    tmp = A[x][y]
                    A[x][y] = '0'
                    dfs(x+dx, y+dy, T[A[x+dx][y+dy]], W+A[x+dx][y+dy])
                    A[x][y] = tmp
        
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] in self.trie:
                    dfs(i, j, self.trie[A[i][j]], A[i][j])
                    
        return self.ans
            