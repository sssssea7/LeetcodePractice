class Solution:
    def candy(self, ratings: List[int]) -> int:
        C = [1]*len(ratings)
        for i in range(len(ratings)-1):
            if ratings[i]<ratings[i+1]: C[i+1] = C[i]+1
        for i in range(len(ratings)-1, 0, -1):
            if ratings[i]<ratings[i-1]: C[i-1] = max(C[i-1], C[i]+1)
        return sum(C)