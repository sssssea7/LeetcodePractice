# https://leetcode.com/problems/summary-ranges/description/

class Solution:
    def summaryRanges(self, A: List[int]) -> List[str]:
        i = 0
        ans = []
        A.append(inf)
        for j in range(len(A)-1):
            if A[j+1] != A[j]+1:
                if i==j: 
                    ans.append(str(A[i]))
                else:
                    ans.append(str(A[i])+"->"+str(A[j]))
                i = j+1
        return ans