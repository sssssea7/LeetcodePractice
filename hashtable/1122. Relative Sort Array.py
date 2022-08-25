class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        cnt1 = Counter(arr1)
        cnt2 = Counter(arr2)
        ans = []
        for a2 in arr2:
            ans.extend([a2]*cnt1[a2])
            cnt1.pop(a2)
        for k, v in sorted(cnt1.items()):
            ans.extend([k]*v)
        return ans
        
        