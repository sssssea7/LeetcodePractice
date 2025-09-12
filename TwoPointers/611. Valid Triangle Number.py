# https://leetcode.com/problems/valid-triangle-number/description/
# solution: https://leetcode.cn/problems/valid-triangle-number/solutions/2432875/zhuan-huan-cheng-abcyong-xiang-xiang-shu-1ex3/
class Solution:
    def triangleNumber(self, A: List[int]) -> int:
        A.sort()
        ans = 0
        for k in range(2, len(A)):
            i, j = 0, k-1
            while i<j:
                if A[i]+A[j]>A[k]:
                    ans += j-i
                    j -= 1
                else:
                    i += 1
        return ans