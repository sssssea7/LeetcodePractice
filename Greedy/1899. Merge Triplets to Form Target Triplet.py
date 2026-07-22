# https://leetcode.com/problems/merge-triplets-to-form-target-triplet/description/

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        cur_a, cur_b, cur_c = 0, 0, 0
        for a, b, c in triplets:
            if a<=target[0] and b<=target[1] and c<=target[2]:
                cur_a = max(cur_a, a)
                cur_b = max(cur_b, b)
                cur_c = max(cur_c, c)
        return [cur_a, cur_b, cur_c] == target