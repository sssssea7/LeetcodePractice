class Solution:
    def threeSum(self, A: List[int]) -> List[List[int]]:
        A.sort()
        ans = []
        for i in range(len(A)):
            if A[i]>0: break
            if i and A[i-1]==A[i]: continue
            t = -A[i]
            M = {}
            for j in range(i+1, len(A)):
                if A[j] in M:
                    if not M[A[j]]:
                        ans.append([A[i], A[j], t-A[j]])
                        M[A[j]] += 1
                else: M[t-A[j]] = 0
        return ans