class CombinationIterator:

    def __init__(self, s: str, n: int):
        self.S = s
        self.L = n
        self.combs = []
        self.dfs("", 0)
        
    def next(self) -> str:
        return self.combs.pop(0)

    def hasNext(self) -> bool:
        return len(self.combs)>0
        
    def dfs(self, comb, i):
        if len(comb)==self.L: self.combs.append(comb)
        if i==len(self.S): return
        for j in range(i, len(self.S)):
            self.dfs(comb+self.S[j], j+1)