class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        n = len(rooms)
        visited = set([0])

        def dfs(key, visited):
            for k in rooms[key]:
                if k not in visited:
                    visited.add(k)
                    dfs(k, visited)

        for key in rooms[0]:
            if key not in visited:
                visited.add(key)
                dfs(key, visited)
        # print(visited)
        return len(visited) == n
