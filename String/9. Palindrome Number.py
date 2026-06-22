# https://leetcode.com/problems/palindrome-number/description/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x%10==0 and x!=0):
            return False

        rev_x = 0
        while x>rev_x:
            rev_x = x % 10 + rev_x * 10
            x //= 10

        return x==rev_x or x==rev_x//10

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)==str(x)[::-1]