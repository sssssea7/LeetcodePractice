# https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/description/

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        ans = 0
        max_q = deque()
        min_q = deque()
        left = 0
        for i in range(n):
            while max_q and nums[i] >= nums[max_q[-1]]:
                max_q.pop()
            max_q.append(i)

            while min_q and nums[i] <= nums[min_q[-1]]:
                min_q.pop()
            min_q.append(i)

            if nums[max_q[0]] - nums[min_q[0]] > limit:  # "while" might be better here
                left += 1
                if max_q[0] < left:
                    max_q.popleft()
                if min_q[0] < left:
                    min_q.popleft()

            ans = max(ans, i-left+1)
        
        return ans
