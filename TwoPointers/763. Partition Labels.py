class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {c: i for i, c in enumerate(s)}
        j = first = 0
        ans = []
        for i, c in enumerate(s):
            j = max(j, last[c])
            if i==j:
                ans.append(i-first+1)
                first = i+1
        return ans