# https://leetcode.com/problems/sliding-window-maximum/description/

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = []
        q = deque()
        for i in range(n):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
            
            if i-q[0] >=k:
                q.popleft()

            if i >= k-1:
                ans.append(nums[q[0]])

        return ans