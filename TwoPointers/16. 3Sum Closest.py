# https://leetcode.com/problems/3sum-closest/description/

class Solution:
    def threeSumClosest(self, A: List[int], t: int) -> int:
        A.sort()
        ans = 0
        mindiff= inf
        for i in range(len(A)-2):
            sm = A[i] + A[i+1] + A[i+2]

            if i and A[i]==A[i-1]:
                continue

            if sm>t:
                    if sm-t < mindiff:
                        ans = sm
                    break

            sm = A[i] + A[-2] + A[-1]
            if sm < t:
                if t - sm < mindiff:
                    mindiff = t - sm
                    ans = sm
                continue
            
            j, k = i+1, len(A)-1
            while j<k:
                sm = A[i]+A[j]+A[k]
                if sm==t:
                    return sm
                elif sm<t:
                    if t - sm < mindiff:
                        mindiff = t - sm
                        ans = sm
                    j += 1
                    
                else: # sm>t
                    if sm - t < mindiff:
                        mindiff = sm - t
                        ans = sm
                    k -= 1
                    
        return ans
        