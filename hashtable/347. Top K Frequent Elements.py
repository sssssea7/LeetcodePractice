# https://leetcode.com/problems/top-k-frequent-elements/

# bucket sort
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        buckets = [[] for _ in range(len(nums)+1)] # defaultdict(list) is also ok
        for num, freq in cnt.items():
            buckets[freq].append(num)
        ans = []
        for freq in reversed(range(len(buckets))):
            for num in buckets[freq]:
                ans.append(num)
                if len(ans)==k:
                    return ans

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pq = []
        cnt = Counter(nums)
        for key, v in cnt.items():
            heapq.heappush(pq, (-v, key))
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(pq)[1])
        return ans

class Solution:
    def topKFrequent(self, A: List[int], k: int) -> List[int]:
        cnt = Counter(A)
        cnt = sorted(cnt.items(), key=lambda x:x[1], reverse=True)
        return [cnt[i][0] for i in range(k)]

