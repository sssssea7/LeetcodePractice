# https://leetcode.com/problems/minimum-window-substring/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cnt_t = Counter(t)
        cnt_s = Counter()
        
        if not (Counter(s)>=cnt_t):
            return ""
        left = 0
        n = len(s)
        ans_left, ans_right = 0, len(s)
        for right in range(n):
            cnt_s[s[right]] += 1
            while cnt_s >= cnt_t:
                if right-left < ans_right-ans_left:
                    ans_left, ans_right = left, right
                cnt_s[s[left]] -= 1
                left += 1
                
        return s[ans_left:ans_right+1] 