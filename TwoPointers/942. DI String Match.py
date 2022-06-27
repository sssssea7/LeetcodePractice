class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        i, j = 0, len(s)
        ans = []
        for c in s:
            if c=="I":
                ans.append(i)
                i += 1
            else:
                ans.append(j)
                j -= 1
        ans.append(i)
        return ans