class Solution:
    def minimumAbsDifference(self, A: List[int]) -> List[List[int]]:
        A.sort()
        ans = []
        min_d = float(inf)
        for i in range(1, len(A)):
            if A[i]-A[i-1] < min_d:
                min_d = A[i]-A[i-1]
                ans = []
                ans.append([A[i-1], A[i]])
            elif A[i]-A[i-1] == min_d:
                ans.append([A[i-1], A[i]])
        return ans