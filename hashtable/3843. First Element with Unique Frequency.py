# https://leetcode.com/problems/first-element-with-unique-frequency/

class Solution:
    def firstUniqueFreq(self, A: List[int]) -> int:
        cnt = Counter(A)
        cnt2 = Counter(cnt.values())
        for k, v in cnt.items():
            cnt[k] = cnt2[v]
        ans = [k for k, v in cnt.items() if v==1]
        return ans[0] if ans else -1
