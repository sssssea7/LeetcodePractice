class Solution:
    def minSetSize(self, A: List[int]) -> int:
        cnt = sorted(Counter(A).items(), key=lambda kv:kv[1], reverse=True)
        ans = 0
        size = 0
        for k, v in cnt:
            if size < len(A)//2:
                ans += 1
                size += v
            else:
                break
        return ans