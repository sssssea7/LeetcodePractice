# https://leetcode.com/problems/subarray-sums-divisible-by-k/

"""
pre: # 

sub[i~j] % k = 0
(pre[0~j] - pre[0~i]) % k = 0
pre[0~j] % k - pre[0~i] % k = 0
pre[0~j] % k = pre[0~i] % k
"""

class Solution:
    def subarraysDivByK(self, A: List[int], k: int) -> int:
        cnt = Counter([0])
        pre = 0
        ans = 0
        for i in range(len(A)):
            pre += A[i]
            if pre%k in cnt:
                ans += cnt[pre%k]
            cnt[pre%k] += 1
        return ans