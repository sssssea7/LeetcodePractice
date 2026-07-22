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


# Boyer-Moore majority vote algorithm
# The idea is that if we pair up each occurrence of the majority element with a different element, they will cancel each other out in the end. Since the majority element appears more than n/2 times, it will always be the last remaining element.
class Solution:
    def majorityElement(self, A: List[int]) -> int:
        cand = None
        cnt = 0
        for a in A:
            if a == cand:
                cnt += 1
            elif cnt == 0:
                cand = a
            else:
                cnt -= 1
        return cand