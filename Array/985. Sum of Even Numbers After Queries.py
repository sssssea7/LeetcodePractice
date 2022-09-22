class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        sm = sum([n for n in nums if n%2==0])
        for v, i in queries:
            if nums[i]%2==0: sm -= nums[i]
            nums[i] += v
            if nums[i]%2==0: sm += nums[i]
            ans.append(sm)
        return ans