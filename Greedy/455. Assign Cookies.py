class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        ans = 0
        while g and s:
            if s[-1]<g[-1]:
                g.pop()
            else:
                ans += 1
                s.pop()
                g.pop()
        return ans


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        child, cookie = 0, 0
        while child < len(g) and cookie < len(s):
            if g[child] <= s[cookie]: child += 1
            cookie += 1
        return child