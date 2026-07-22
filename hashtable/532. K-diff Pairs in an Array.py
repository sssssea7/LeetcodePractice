# https://leetcode.com/problems/k-diff-pairs-in-an-array/description/

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums = sorted(nums, reverse=True)
        ans = set()
        seen = set()
        for i, x in enumerate(nums):
            needed = x+k
            if needed in seen:
                ans.add((needed, x))
            seen.add(x)
        return len(ans)


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        frequency = Counter(nums)
        if k==0:
            return sum(count>=2 for count in frequency.values())
        ans = 0
        for x in frequency:
            if x+k in frequency:
                ans += 1
        return ans
