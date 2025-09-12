class Solution:
    def productExceptSelf(self, A: List[int]) -> List[int]:
        prefix = [1] + list(accumulate(A, mul)) + [1]
        suffix = [1] + list(accumulate(A[::-1], mul))[::-1] + [1]
        # print(prefix)
        # print(suffix)
        return [prefix[i-1]*suffix[i+1] for i in range(1, len(prefix)-1)]

class Solution:
    def productExceptSelf(self, A: List[int]) -> List[int]:
        pre = [1] + list(accumulate(A, mul))
        suf = list(accumulate(A[::-1], mul))[::-1] + [1]
        return [pre[i]*suf[i+1] for i in range(len(A))]