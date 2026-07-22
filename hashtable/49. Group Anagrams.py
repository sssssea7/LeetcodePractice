# https://leetcode.com/problems/group-anagrams/

# time complexity: O(nk)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            counts = [0] * 26
            for char in s:
                index = ord(char)-ord('a')
                counts[index] += 1
            key = tuple(counts)
            groups[key].append(s)
        return list(groups.values())

# time complexity: O(nklogk), where n is the length of strs, and k is the maximum length of a string in strs. The outer loop runs n times, and for each string, we sort it which takes O(klogk) time.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Groups = defaultdict(list)
        for s in strs:
            Groups["".join(sorted(s))].append(s)
        return list(Groups.values())