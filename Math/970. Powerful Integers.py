class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        ans = []
        X = [x**i for i in range(20) if x**i <= bound]
        Y = [y**j for j in range(20) if y**j <= bound]
        for a in X:
            for b in Y:
                if a+b > bound: break
                if a+b not in ans: ans.append(a+b)
        return ans


# log
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        a = bound if x==1 else int(math.log(bound, x))+1
        b = bound if y==1 else int(math.log(bound, y))+1
        ans = []
        for i in range(a):
            for j in range(b):
                if x**i+y**j<=bound: ans.append(x**i+y**j)
                if y==1: break
            if x==1: break
        return list(set(ans))