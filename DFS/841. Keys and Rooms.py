class Solution:
    def canVisitAllRooms(self, A: List[List[int]]) -> bool:
        seen = set([0])
        def dfs(i):
            for key in A[i]:
                if key not in seen:
                    seen.add(key)
                    dfs(key)
        dfs(0)
        return len(seen)==len(A)

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        self.keys = []
        def dfs(room):
            for k in room:
                if k not in self.keys: 
                    self.keys.append(k)
                    dfs(rooms[k])
        dfs(rooms[0])
        for i in range(1, len(rooms)):
            if i not in self.keys: return False
        return True