
# back tracking
class Solution:
    def makesquare(self, A: List[int]) -> bool:
        if sum(A)%4 != 0: return False
        k = sum(A)//4
        seen = [0]*len(A)
        A.sort(reverse=True)

        def dfs(i, sm, group):
            if group==4: return True
            if sm>k: return False
            if sm==k: return dfs(0, 0, group+1)
            for j in range(i, len(A)):
                if not seen[j]:
                    seen[j] = 1
                    if dfs(j, sm+A[j], group): return True
                    seen[j] = 0
            return False
        
        return dfs(0, 0, 0)

# bit mask
class Solution:
    def makesquare(self, A: List[int]) -> bool:
        if sum(A)%4 != 0: return False
        
        k = sum(A)//4
        seen = [0]*len(A)
        A.sort(reverse=True)
        n = len(A)
        
        @cache
        def dp(mask):
            if mask==(1<<n)-1: return 0
            for j in range(n):
                if not mask&(1<<j):
                    neib = dp(mask^(1<<j))
                    if neib>=0 and neib+A[j]<=k:
                        return (neib+A[j])%k
            return -1
        
        return dp(0)==0


class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        def dfs(nums, pos, target):
            if pos == len(nums): return True
            for i in range(4):
                if target[i] >= nums[pos]:
                    target[i] -= nums[pos]
                    if dfs(nums, pos+1, target): return True
                    target[i] += nums[pos]
            return False
        if len(nums) < 4 : return False
        numSum = sum(nums)
        nums.sort(reverse=True)
        if numSum % 4 != 0: return False
        target = [numSum/4] * 4
        return dfs(nums,0, target)
