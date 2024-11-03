# https://leetcode.com/problems/grumpy-bookstore-owner/
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], k: int) -> int:
        A = [x*y for x, y in zip(customers, grumpy)]
        i = 0
        sm = mx = sum(A[:k])
        for j in range(k, len(A)):
            sm = sm - A[j-k] + A[j]
            if sm>mx: 
                mx = sm
                i = j-k+1
        
        ans = 0
        for ii in range(len(customers)):
            if i<=ii<i+k or grumpy[ii]==0:
                ans += customers[ii]
        return ans