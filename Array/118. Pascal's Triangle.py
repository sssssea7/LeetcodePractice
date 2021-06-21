class Solution:
    def generate(self, n: int) -> List[List[int]]:
        ans = []
        for i in range(n):
            row = [1 for _ in range(i+1)]
            for j in range(1, len(row)-1):
                row[j]=ans[i-1][j-1]+ans[i-1][j]
            ans.append(row)
        return ans