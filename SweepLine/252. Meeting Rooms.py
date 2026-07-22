# https://leetcode.com/problems/meeting-rooms/description/
# given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings. if e1==s2, it is not considered an overlap.

# sweep line solution
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        events = []
        for start, end in intervals:
            events.append([start, 1])
            events.append([end, -1])
        events.sort()
        active_meetings = 0
        for time, change in events:
            active_meetings += change
            if active_meetings>1:
                return False
        return True

# sort the intervals by start time, then check if any interval overlaps with the previous one.
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        for i, (start, end) in enumerate(intervals):
            if i and start < intervals[i-1][1]:
                return False
        return True