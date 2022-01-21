class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        A = [g-c for g, c in zip(gas, cost)]
        if sum(A)<0: return -1
        
        ans = 0
        prefix = 0
        for i in range(len(A)):
            prefix += A[i]
            if prefix<0:
                prefix = 0
                ans = i+1
        return ans