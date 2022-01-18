# itertools.groupby
class Solution:
    def canPlaceFlowers(self, A: List[int], n: int) -> bool:
        A = [0]+A+[0]
        for k, v in groupby(A):
            if not k: n -= (len(list(v))-1)//2
            if n<=0: return True
        return False


# greedy
class Solution:
    def canPlaceFlowers(self, A: List[int], n: int) -> bool:
        A = [0]+A+[0]
        for i in range(1, len(A)-1):
            if A[i]==A[i-1]==A[i+1]==0: 
                A[i]=1
                n -= 1
            if n<=0: return True
        return False
        