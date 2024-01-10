# https://leetcode.com/problems/number-of-recent-calls/
class RecentCounter:

    def __init__(self):
        self.Q = []

    def ping(self, t: int) -> int:
        self.Q.append(t)
        ans = 0
        for x in self.Q:
            if t-3000<=x<=t:
                ans += 1
        return ans


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)