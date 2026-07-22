# https://leetcode.com/problems/meeting-rooms-ii/description/
# given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required. if e1==s2, it is not considered an overlap.

# sweep line solution
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        events = []
        for start, end in intervals:
            events.append([start, 1])
            events.append([end, -1])
        events.sort()

        active_meetings = 0
        max_rooms = 0
        for time, change in events:
            active_meetings += change
            max_rooms = max(max_rooms, active_meetings)
        return max_rooms

# heap solution
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        cur_meetings = 0
        active_end_times = []
        for start, end in intervals:
            while active_end_times and active_end_times[0]<=start:
                heappop(active_end_times)
            heappush(active_end_times, end)
            cur_meetings = max(cur_meetings, len(active_end_times))
        return cur_meetings