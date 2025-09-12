# https://leetcode.com/problems/find-if-array-can-be-sorted/
class Solution:
    def canSortArray(self, A: List[int]) -> bool:
        A_bit = [[a, a.bit_count()] for a in A]
        B = sorted(A_bit)

        D = defaultdict(list)
        pre = 0
        cur_k = 0
        for k, v in A_bit:
            if v!=pre:
                cur_k += 1
                pre = v
            D[cur_k].append(k)
            
        D2 = defaultdict(list)
        pre = 0
        cur_k = 0
        for k, v in B:
            if v!=pre:
                cur_k += 1
                pre = v
            D2[cur_k].append(k)
            
            
        for i in range(len(D)):
            if Counter(D[i])!=Counter(D2[i]): return False
        
        return True