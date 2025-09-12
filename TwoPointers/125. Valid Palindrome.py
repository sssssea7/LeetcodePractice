# https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            if not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
            elif s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else:
                return False
        return True


class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        while i<j:
            print(i, j)
            if s[i].isalnum() and s[j].isalnum():
                if s[i].lower() == s[j].lower():
                    i += 1
                    j -= 1
                else:
                    return False
            elif not s[i].isalnum() and s[j].isalnum():
                i += 1
            elif s[i].isalnum() and not s[j].isalnum():
                j -= 1
            else:
                i += 1
                j -= 1
        return True


