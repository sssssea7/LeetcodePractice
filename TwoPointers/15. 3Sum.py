# https://leetcode.com/problems/3sum/
class Solution:
    def threeSum(self, A: List[int]) -> List[List[int]]:
        A.sort()
        ans = []
        for i in range(len(A)-2):
            if i>0 and A[i] == A[i-1]: continue
            if A[i] + A[i+1] + A[i+1] > 0: break
            if A[i] + A[-2] + A[-1] < 0: continue
            l, r = i+1, len(A)-1
            while l<r:
                if A[i] + A[l] + A[r] > 0:
                    r -= 1
                elif A[i] + A[l] + A[r] < 0:
                    l += 1
                else:
                    ans.append([A[i], A[l], A[r]])
                    r -= 1
                    while l<r and A[r]==A[r+1]:
                        r -= 1
                    l += 1
                    while l<r and A[l]==A[l-1]:
                        l += 1
        return ans