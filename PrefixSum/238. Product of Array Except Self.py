class Solution:
    def productExceptSelf(self, A: List[int]) -> List[int]:
        prefix = [1] + list(accumulate(A, mul)) + [1]
        suffix = [1] + list(accumulate(A[::-1], mul))[::-1] + [1]
        # print(prefix)
        # print(suffix)
        return [prefix[i-1]*suffix[i+1] for i in range(1, len(prefix)-1)]