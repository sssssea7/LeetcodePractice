class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        if (k-n)//25==0:
            x = k-n+1
            return "a"*(n-1)+chr(96+x)
        else:
            numOfZ = (k-n)//25
            x=k-26*numOfZ-(n-1-numOfZ)
            if(n==numOfZ): return "z"*numOfZ
            return "a"*(n-1-numOfZ)+chr(96+x)+"z"*numOfZ
        
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        x = k - n
        ans = 'z' * (x // 25)
        x %= 25
        if x: ans = chr(ord('a')+x) + ans
        return 'a'*(n-len(ans))+ans
        