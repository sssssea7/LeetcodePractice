# https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/description/
# the idea is to find all prefixes of the first array and store them in a set. Then, for each number in the second array, we check if any of its prefixes are in the set. If we find a common prefix, we update the answer with the length of that prefix.

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes = set()
        for num in arr1:
            prefix = num
            while prefix>0:
                prefixes.add(prefix)
                prefix //= 10

        ans = 0
        for num in arr2:
            prefix = num
            while prefix > 0:
                if prefix in prefixes:
                    ans = max(ans, len(str(prefix)))
                    break
                prefix //= 10
        
        return ans