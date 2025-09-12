# https://leetcode.com/problems/string-compression/description/?envType=study-plan-v2&envId=leetcode-75 
class Solution:
    def compress(self, A: List[str]) -> int:
        A.append("*")
        i = 0
        idx = 0
        ans = 0
        for j in range(1, len(A)):
            if A[j]!=A[j-1]:
                A[idx] = A[i]
                cnt = j-i
                idx += 1
                if cnt>1:
                    for d in str(cnt):
                        A[idx] = d
                        idx += 1
                i = j
        for _ in range(len(A)-idx):
            A.pop()