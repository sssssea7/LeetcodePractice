class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], N: int) -> int:
        k = len(str(N))
        ans = sum([len(digits)**i for i in range(1, k)])
        @lru_cache(None)
        def dfs(n):
            # print(n)
            if n and int(n)>N: return -1
            return sum([1+dfs(n+d) for d in digits])
        
        return dfs("")
                
                
    