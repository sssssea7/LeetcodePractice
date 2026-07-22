# https://leetcode.com/problems/car-pooling/

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        rides = []
        for n, start, end in trips:
            rides.append([start, n])
            rides.append([end, -n])
        rides.sort()
        cur_passengers = 0
        for location, n in rides:
            cur_passengers += n
            if cur_passengers > capacity:
                return False
        return True

class Solution:
    def carPooling(self, A: List[List[int]], c: int) -> bool:
        n = max([x for _, _, x in A])
        cnt = [0]*(n+1)
        for x, i, j in A:
            cnt[i] += x
            cnt[j] -= x
        for i in range(1, n+1):
            cnt[i] += cnt[i-1]
        return max(cnt)<=c