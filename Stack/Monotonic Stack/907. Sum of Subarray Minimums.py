# https://leetcode.com/problems/sum-of-subarray-minimums/description/

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        right_stack = []
        next_smaller_right = [n] * n
        for i in range(n):
            while right_stack and arr[right_stack[-1]] > arr[i]:
                next_smaller_right[right_stack.pop()] = i
            right_stack.append(i)
        
        left_stack = []
        next_smaller_left = [-1] * n
        for i in range(n-1, -1, -1):
        # for i in reversed(range(n)):
            while left_stack and arr[left_stack[-1]] >= arr[i]:
                next_smaller_left[left_stack.pop()] = i
            left_stack.append(i)
    
        ans = 0
        for i, (l, r) in enumerate(zip(next_smaller_left, next_smaller_right)):
            ans += (i-l)*(r-i)*arr[i]
        return ans % (10**9+7)
