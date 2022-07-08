class Solution:
    def nextGreaterElement(self, A: List[int], B: List[int]) -> List[int]:
        mp = defaultdict(lambda: -1)
        stk = []
        for i in range(len(B)):
            while stk and B[stk[-1]]<B[i]:
                mp[B[stk.pop()]] = B[i]
            stk.append(i)
        return [mp[x] for x in A]