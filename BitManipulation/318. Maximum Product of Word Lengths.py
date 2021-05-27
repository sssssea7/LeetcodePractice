class Solution:
    def maxProduct(self, words: List[str]) -> int:
        ans = 0
        words_set = [set(w) for w in words]
        for i in range(len(words_set)):
            for j in range(i+1, len(words_set)):
                if not words_set[i]&words_set[j] and len(words[i]) * len(words[j]) > ans:
                    ans = len(words[i]) * len(words[j])
        return ans