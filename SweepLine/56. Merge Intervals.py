# https://leetcode.com/problems/merge-intervals/

# sweep line

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        events = []
        for start, end in intervals:
            events.append([start, 1])
            events.append([end, -1])
        events.sort(key=lambda x: [x[0], -x[1]]) # At equal times, process starts before ends.
        active = 0
        cur_start = 0
        for time, change in events:
            if change==1 and active==0:
                cur_start = time
            active += change
            if change==-1 and active==0:
                ans.append([cur_start, time])
        return ans


# sort by start time, then end time
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        stack = []
        for start, end in intervals:
            if stack and stack[-1][1] >= start:
                pre_start, pre_end = stack.pop()
                stack.append([pre_start, max(pre_end, end)])
            else:
                stack.append([start, end])
        return stack