# https://leetcode.com/problems/count-the-number-of-special-characters-ii/description/

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        index = defaultdict(int) # letter: right most index (lower case) or left most index (upper case)
        for i, c in enumerate(word):
            if c==c.lower():
                index[c] = i
            elif c==c.upper() and c not in index:
                index[c] = i
        ans = 0
        letters = set(word)
        seen = set()
        for letter in letters:
            if letter.lower() not in index or letter.upper() not in index:
                continue
            if letter.lower() not in seen and index[letter.lower()] < index[letter.upper()]:
                ans += 1
                seen.add(letter.lower())
        return ans