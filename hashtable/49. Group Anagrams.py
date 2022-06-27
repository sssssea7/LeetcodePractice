class Solution:
    def groupAnagrams(self, A: List[str]) -> List[List[str]]:
        ht = defaultdict(list)
        for s in A:
            ht["".join(sorted(s))].append(s)
        return ht.values()