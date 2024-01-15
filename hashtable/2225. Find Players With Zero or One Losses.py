# https://leetcode.com/problems/find-players-with-zero-or-one-losses/
class Solution:
    def findWinners(self, A: List[List[int]]) -> List[List[int]]:
        winners = Counter(list(zip(*A))[0])
        losers = Counter(list(zip(*A))[1])
        ans = [0, 0]
        ans[0] = sorted(set(winners)-set(losers))
        ans[1] = sorted([k for k, v in losers.items() if v==1])
        return ans