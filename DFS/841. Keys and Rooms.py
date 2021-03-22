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