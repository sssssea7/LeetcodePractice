# https://leetcode.com/problems/maximum-number-of-robots-within-budget/description/

class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        n = len(chargeTimes)
        ans = 0
        q = deque()
        costs = 0
        left = 0
        for i in range(n):
            while q and chargeTimes[i] >= chargeTimes[q[-1]]:
                q.pop()
            q.append(i)
            costs += runningCosts[i]

            k = i - left + 1
            while q and chargeTimes[q[0]] + k * costs > budget: # "if chargeTimes[q[0]] + k * costs > budget:" also works
                if q[0] == left:
                    q.popleft()
                costs -= runningCosts[left]
                left += 1
                
            ans = max(ans, i-left+1)
        return ans
