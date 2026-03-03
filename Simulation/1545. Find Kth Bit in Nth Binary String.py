# https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/description/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        k -= 1
        cnt = 0
        while k>0:
            x = 1
            while 2**x-1<=k:
                x += 1
            m = (2**x-1)//2
            k = 2*m-k
            if k==m:
                return '0' if cnt&1 else '1'
            cnt += 1
        return '1' if cnt&1 else '0'
