# https://leetcode.com/problems/subarray-sum-equals-k/

# prefix[i] + (-prefix[j]) = k -> two sum
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixes = list(accumulate(nums, initial=0))
        frequency = defaultdict(int) # prefix: cnt
        ans = 0
        for prefix in prefixes:
            needed = prefix - k
            ans += frequency[needed]
            frequency[prefix] += 1
        return ans