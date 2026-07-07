# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/description/

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = inf
        q = deque()
        prefix = list(accumulate(nums, initial=0))
        for i in range(n+1):
            while q and prefix[i] <= prefix[q[-1]]:
                q.pop()
            q.append(i)

            while q and prefix[i] - prefix[q[0]] >=k:
                j = q.popleft()
                ans = min(ans, i-j)
        return ans if ans!=inf else -1