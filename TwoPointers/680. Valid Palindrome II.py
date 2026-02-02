# https://leetcode.com/problems/valid-palindrome-ii/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(s, i, j):
            while i<j:
                if s[i]!=s[j]:
                    return False
                else:
                    i += 1
                    j -= 1
            return True

        i, j = 0, len(s)-1
        while i<j:
            if s[i]!=s[j]:
                return is_palindrome(s, i+1, j) or is_palindrome(s, i, j-1)
            else:
                i += 1
                j -= 1
        return True

