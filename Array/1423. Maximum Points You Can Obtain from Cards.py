class Solution:
    def maxScore(self, cp: List[int], k: int) -> int:
        if len(cp) == k: return sum(cp)
        s = sum(cp[:k])
        s_arr = [s]
        p_idx = k-1
        n_idx = -1
        for i in range(k):
            s = s - cp[p_idx] + cp[n_idx]
            s_arr.append(s)
            p_idx -= 1
            n_idx -= 1
        return max(s_arr)