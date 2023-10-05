class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return Counter(nums).most_common()[0][0]

# sort hashtable
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(Counter(nums).items(), key = lambda pair:pair[1], reverse=True)[0][0]
        
class Solution:
    def majorityElement(self, A: List[int]) -> int:
        cnt = Counter(A)
        for k, v in cnt.items():
            if v>len(A)//2: return k