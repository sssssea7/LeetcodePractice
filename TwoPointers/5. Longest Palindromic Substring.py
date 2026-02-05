class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):
            l, r = i, i  # odd length palindrome
            while 0 <= l <= r < len(s) and s[l]==s[r]:
                l -= 1
                r += 1
            ans = max(ans, s[l+1:r], key=len)

        for i in range(len(s)):
            l, r = i, i+1  # even length palindrome
            while 0 <= l <= r < len(s) and s[l]==s[r]:
                l -= 1
                r += 1
            ans = max(ans, s[l+1:r], key=len)
            
        return ans

class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        for i in range(2*len(s)-1):
            l, r = i//2, (i+1)//2
            while 0 <= l <= r < len(s) and s[l]==s[r]:
                l -= 1
                r += 1
            ans = max(ans, s[l+1:r], key=len)

        return ans