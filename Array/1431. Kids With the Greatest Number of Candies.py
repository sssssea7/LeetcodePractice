# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
class Solution:
    def kidsWithCandies(self, A: List[int], e: int) -> List[bool]:
        ans = []
        mx = max(A)
        for a in A:
            if a+e>=mx:
                ans.append(True)
            else:
                ans.append(False)
        return ans