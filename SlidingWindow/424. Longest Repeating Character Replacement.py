# https://leetcode.com/problems/longest-repeating-character-replacement/description/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = [0] * 26
        left = 0
        ans = 0
        for right, char in enumerate(s):
            index = ord(char)-ord('A')
            counts[index] += 1

            window_length = right-left+1
            max_frequency = max(counts)

            while window_length - max_frequency > k:
                left_index = ord(s[left])-ord('A')
                counts[left_index] -= 1
                left += 1
                window_length -= 1
                max_frequency = max(counts)
            
            ans = max(ans, window_length)
        return ans