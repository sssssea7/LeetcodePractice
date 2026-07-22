# https://leetcode.com/problems/interval-list-intersections/description/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        intervals = []
        for start, end in firstList:
            intervals.append([start, 1])
            intervals.append([end, -1])
        for start, end in secondList:
            intervals.append([start, 1])
            intervals.append([end, -1])
        intervals.sort(key=lambda x: (x[0], -x[1]))
        ans = []
        overlap = 0
        cur_start, cur_end = -1, -1
        for cur, change in intervals:
            overlap += change
            if overlap > 1 and change == 1:
                cur_start = cur
            elif overlap <=1 and change == -1 and cur_start != -1:
                cur_end = cur
                ans.append([cur_start, cur_end])
                cur_start, cur_end = -1, -1
                
        return ans