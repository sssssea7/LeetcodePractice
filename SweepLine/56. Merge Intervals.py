class Solution:
    def merge(self, A: List[List[int]]) -> List[List[int]]:
        sl = []
        print(len(sl))
        for x, y in A:
            sl.append((x, 1))
            sl.append((y+1, -1))
        sl.sort()
        
        cnt = 0
        l = None
        n = len(sl)
        ans = []
        for i, x in sl:
            if cnt==0 and l==None:
                l = i
            cnt += x
            if cnt==0:
                ans.append([l, i-1])
                l = None
        return ans
