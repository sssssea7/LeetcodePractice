# https://leetcode.com/problems/merge-strings-alternately/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        i, j = 0, 0
        while i<len(word1) and j<len(word2):
            ans += word1[i] + word2[j]
            i += 1
            j += 1
        if i<len(word1):
            ans += word1[i:]
        if j<len(word2):
            ans += word2[j:]
        return ans


class Solution:
    def mergeAlternately(self, w1: str, w2: str) -> str:
        ans = ""
        while w1 and w2:
            a = w1[0]
            w1 = w1[1:]
            b = w2[0]
            w2 = w2[1:]
            ans += a+b
        if w1:
            ans += w1
        elif w2:
            ans += w2
        return ans