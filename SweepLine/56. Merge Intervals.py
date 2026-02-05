# https://leetcode.com/problems/merge-intervals/

# sweep line
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

# sort by start time, then end time
class Solution:
    def merge(self, A: List[List[int]]) -> List[List[int]]:
        A.sort()
        ans = [A[0]]
        for i in range(1, len(A)):
            if A[i][0] <= ans[-1][1]:
                [x, y] = ans.pop()
                ans.append([x, max(A[i][1], y)])   
            else:
                ans.append(A[i])
        return ans