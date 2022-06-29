class Solution:
    def reconstructQueue(self, A: List[List[int]]) -> List[List[int]]:
        A.sort(key=lambda x:[-x[0], x[1]])
        ans = []
        for a in A:
            ans.insert(a[1], a)
        return ans