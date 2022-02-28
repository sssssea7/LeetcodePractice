class Solution:
    def summaryRanges(self, A: List[int]) -> List[str]:
        A.append(inf)
        ans = []
        i = 0
        for j in range(len(A)-1):
            if A[j+1]-A[j] > 1:
                if A[i]==A[j]: ans.append(str(A[i]))
                else: ans.append(str(A[i])+"->"+str(A[j]))
                i = j+1
        return ans