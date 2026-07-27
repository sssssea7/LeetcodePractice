# https://leetcode.com/problems/h-index/description/

# O(n)
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        frequency = [0] * (n+1)
        for c in citations:
            frequency[min(c, n)] += 1
        
        citation_cnt = 0 # at least have i citations
        for i in range(n, -1, -1):
            citation_cnt += frequency[i]
            if citation_cnt >= i:
                return i

# O(n^2)
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        frequency = [0] * (n+1) # each element means at least k papers have index number of citations
        for i in range(n+1):
            fre = 0
            for j, c in enumerate(citations):
                if c>=i:
                    fre += 1
            frequency[i] = fre
        
        ans = 0
        for i, fre in enumerate(frequency): 
            ans = max(ans, min(i, fre))
        return ans