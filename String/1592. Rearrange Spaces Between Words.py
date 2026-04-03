# https://leetcode.com/problems/rearrange-spaces-between-words/description/

class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.split()
        words_len = sum([len(word) for word in words])
        if len(words)==1:
            return words[0] + " "*(len(text)-words_len)
        total_space = len(text)-words_len
        avg, end = divmod(total_space, len(words)-1)
        avg_space = avg*" "
        return avg_space.join(words) + " "*end