# https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/
class Solution:
    def findMatrix(self, A: List[int]) -> List[List[int]]:
        cnt = Counter(A)
        D = defaultdict(list)
        n = max(cnt.values())
        for i in range(1, n+1):
            for k, v in cnt.items():
                if v>0:
                    D[i].append(k)
                    cnt[k] -= 1
        ans = [v for k, v in D.items()]
        return ans