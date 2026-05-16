# https://leetcode.com/problems/maximize-palindrome-length-from-subsequences/description/

class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        s = word1 + word2
        n1, n = len(word1), len(s)
        self.ans = 0

        @cache
        def dfs(i, j):
            if i > j: return 0
            if i == j: return 1
            
            if s[i] == s[j]:
                res = dfs(i + 1, j - 1) + 2
                # Only update global answer if it spans both words
                if i < n1 <= j:
                    self.ans = max(self.ans, res)
                return res
            else:
                return max(dfs(i + 1, j), dfs(i, j - 1))
        
        dfs(0, n - 1)
        return self.ans