# https://leetcode.com/problems/text-justification/description/

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        cur = []
        cur_len = 0
        for word in words:
            if maxWidth-cur_len-len(cur) >= len(word):
                cur.append(word)
                cur_len += len(word)
            else:
                if len(cur)==1:
                    line = cur[0] + " " * (maxWidth-len(cur[0]))
                    ans.append(line)
                else:
                    total_space = maxWidth - cur_len
                    avg_space, rem = divmod(total_space, len(cur)-1)
                    line = ""
                    for i, c in enumerate(cur):
                        line += c
                        if i!=len(cur)-1:
                            line += " " * (avg_space+(rem>0))
                            rem -= 1
                    ans.append(line)
                cur = [word]
                cur_len = len(word)
        line = " ".join(cur)
        line += " " * (maxWidth-len(line))
        ans.append(line)
        return ans
            