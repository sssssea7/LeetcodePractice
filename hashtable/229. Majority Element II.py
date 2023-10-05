class Solution:
    def majorityElement(self, A: List[int]) -> List[int]:
        n, ans = len(A), []
        cnt = Counter(A)
        for k, v in cnt.items():
            if v>n//3: ans.append(k)
        return ans