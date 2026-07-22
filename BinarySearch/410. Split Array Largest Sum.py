# https://leetcode.com/problems/split-array-largest-sum/description/

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def can_split(largest_sum):
            parts = 1
            current_sum = 0
            for x in nums:
                if current_sum + x > largest_sum:
                    parts += 1
                    current_sum = x
                    if parts > k:
                        return False
                else:
                    current_sum += x
            return True
        
        left = max(nums)
        right = sum(nums) # max(nums) <= answer <= sum(nums)
        while left<right:
            mid = (left+right)//2
            if can_split(mid):
                right = mid
            else:
                left = mid + 1
        return left


# dp solution
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0] + list(accumulate(nums))
        
        @cache
        def dfs(i, k):
            if k==1:
                return prefix[n]-prefix[i]
            ans = inf
            for j in range(i+1, n-k+2): # -> n-(k-1)+1
                cur_sum = prefix[j]-prefix[i]
                largest_sum = max(cur_sum, dfs(j, k-1))
                ans = min(ans, largest_sum)
            return ans
        
        return dfs(0, k)