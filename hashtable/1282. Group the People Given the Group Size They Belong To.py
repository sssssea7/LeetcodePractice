class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        ans = []
        cur = defaultdict(list)
        for i, g in enumerate(groupSizes):
            cur[g].append(i)
            if len(cur[g]) == g:
                ans.append(cur[g])
                del cur[g]
        return ans