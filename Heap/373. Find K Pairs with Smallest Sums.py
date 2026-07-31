# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        seen = {(0, 0)}
        pq = [(nums1[0]+nums2[0], 0, 0)]
        ans = []
        for _ in range(k):
            _, i, j = heappop(pq)
            ans.append([nums1[i], nums2[j]])
            if i+1<len(nums1) and (i+1, j) not in seen:
                heappush(pq, (nums1[i+1]+nums2[j], i+1, j))
                seen.add((i+1, j))
            if j+1<len(nums2) and (i, j+1) not in seen:
                heappush(pq, (nums1[i]+nums2[j+1], i, j+1))
                seen.add((i, j+1))
        return ans