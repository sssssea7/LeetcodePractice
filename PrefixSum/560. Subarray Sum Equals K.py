class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = Counter()
        cnt[0] = 1
        prefix = 0
        ans = 0
        for n in nums:
            prefix += n
            ans += cnt[prefix-k]
            cnt[prefix] += 1
        return ans