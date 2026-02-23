# https://leetcode.com/problems/toggle-light-bulbs/

class Solution:
    def toggleLightBulbs(self, A: list[int]) -> list[int]:
        cnt = Counter(A)
        ans = []
        for k, v in cnt.items():
            if v&1:
                ans.append(k)
        # print(ans)
        return sorted(ans)