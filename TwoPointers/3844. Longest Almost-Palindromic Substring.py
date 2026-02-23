# https://leetcode.com/problems/longest-almost-palindromic-substring/description/


class Solution:
    def almostPalindromic(self, s: str) -> int:
        ans = 0
        
        def expand(l ,r):
            while l>=0 and r<len(s) and s[l]==s[r]:
                l -= 1
                r += 1
            nonlocal ans
            ans = max(ans, r-l-1) # [l+1, r-1] 是回文串

        for i in range(2*len(s)-1):
            l, r = i//2, (i+1)//2
            while l>=0 and r<len(s) and s[l]==s[r]:
                l -= 1
                r += 1
            expand(l-1, r)
            expand(l, r+1)
            if ans >= len(s):
                return len(s)
        
        return ans
        

class Solution:
    def almostPalindromic(self, s: str) -> int:
        ans1 = ""
        ans1_len = 0
        ans2 = ""
        ans2_len = 0
        for i in range(2*len(s)-1):
            # print('-------')
            l, r = i//2, (i+1)//2
            # print(l, r)
            k1 = 1
            while 0 <= l <= r < len(s):
                if k1:
                    if s[l]==s[r]:
                        l -= 1
                        r += 1
                    elif s[l] != s[r]:
                        l -= 1
                        k1 -= 1
                else:
                    if s[l]==s[r]:
                        l -= 1
                        r += 1
                    else: 
                        break
            
            ans1 = max(ans1, s[l+1:r], key=len)
            ans1_len = max(ans1_len, r-l+k1-1)
            # print(r-l+k1-1)
        
            l, r = i//2, (i+1)//2            
            k2 = 1
            # print('abcd', l, r)
            while 0 <= l <= r < len(s):
                if k2:
                    if s[l]==s[r]:
                        l -= 1
                        r += 1
                    elif s[l] != s[r]:
                        r += 1
                        k2 -= 1 
                else:
                    if s[l]==s[r]:
                        l -= 1
                        r += 1
                    else: 
                        break
                # print('qwer', l, r)

            ans2 = max(ans2, s[l+1:r], key=len)
            ans2_len = max(ans2_len, r-l+k2-1)
            # print(r-l+k2-1, k2, l, r)

        # print(ans1, ans2)
        # print(ans1_len, ans2_len)

        if len(ans1)<len(ans2):
            # print("ans2")
            return min(ans2_len, len(s))
        else:
            # print("ans1")
            return min(ans1_len, len(s))