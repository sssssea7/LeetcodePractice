class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans = 0
        for s in zip(*strs):
            if list(s) != sorted(list(s)): ans += 1
        return ans