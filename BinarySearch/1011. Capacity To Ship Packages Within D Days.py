# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_ship(capacity):
            day = 1
            cur_weight = 0
            for w in weights:
                cur_weight += w
                if cur_weight > capacity:
                    day += 1
                    cur_weight = w
                    if day > days:
                        return False
            return True

        left, right = min(weights), sum(weights)
        while left<right:
            middle = (left+right)//2
            if can_ship(middle):
                right = middle
            else:
                left = middle + 1
        return max(left, max(weights))