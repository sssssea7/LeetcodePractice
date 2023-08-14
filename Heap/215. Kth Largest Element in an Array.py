class Solution(object):
    def findKthLargest(self, nums, k):
        return sorted(nums, reverse=True)[k-1]
    

class Solution:
    def findKthLargest(self, A: List[int], k: int) -> int:
        pq = []
        for x in A:
            heappush(pq, x)
            if len(pq) > k: heappop(pq)
        return pq[0]