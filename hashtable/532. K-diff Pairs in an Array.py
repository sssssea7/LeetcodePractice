class Solution:
    def findPairs(self, A: List[int], k: int) -> int:
        cnt = Counter(A)
        if k==0: return sum([v>1 for k,v in cnt.items()])
        A = sorted(cnt)
        ans = 0
        ht = {}
        for i in range(len(A)):
            x = A[i]-k
            if x in ht: ans += 1
            ht[A[i]] = i
        return ans