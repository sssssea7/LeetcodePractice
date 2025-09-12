# https://leetcode.com/problems/4sum/description/

class Solution:
    def fourSum(self, A: List[int], t: int) -> List[List[int]]:
        A.sort()
        ans = []
        
        for a in range(len(A)-3):
            if a and A[a] == A[a-1]: continue         # skip the same number
            if A[a]+A[a+1]+A[a+2]+A[a+3]>t: break     # if smallest 4 numbers are greater than t, no need to continue
            if A[a]+A[-3]+A[-2]+A[-1]<t: continue     # if largest 4 numbers are less than t, continue to next starting number

            for b in range(a+1, len(A)-2):
                if b>a+1 and A[b]==A[b-1]: continue
                if A[a]+A[b]+A[b+1]+A[b+2] > t: break
                if A[a]+A[b]+A[-2]+A[-1] < t: continue

                c, d = b+1, len(A)-1
                while c<d:
                    sm = A[a]+A[b]+A[c]+A[d]
                    if sm==t and [A[a],A[b],A[c],A[d]] not in ans:
                        ans.append([A[a],A[b],A[c],A[d]])
                        c += 1
                        d -= 1
                    elif sm<t:
                        c += 1
                    else:
                        d -= 1
        return ans