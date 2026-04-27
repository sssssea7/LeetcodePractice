# https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/description/

class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        tails = []
        ans = []
        for x in obstacles:
            i = bisect_right(tails, x)
            ans.append(i+1)
            if i==len(tails):
                tails.append(x)
            else:
                tails[i] = x
        return ans