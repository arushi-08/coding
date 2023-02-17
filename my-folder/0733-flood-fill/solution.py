from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
#       bfs
        visited = [[False]*len(image[0]) for i in range(len(image))]
        for i in range(len(image)):
            for j in range(len(image[0])):
                if not visited[i][j]:
                    self.bfs(image, sr, sc, color, visited)
        return image
    
    def bfs(self, image, sr, sc, color, visited):

        queue = deque()
        queue.append((sr, sc))
        rows = [-1, 0, 1, 0]
        cols = [ 0, 1, 0, -1]
        og_color = image[sr][sc]
        while queue:
            currr, currc = queue.popleft()
            image[currr][currc] = color
            visited[currr][currc] = True
            for i in range(len(rows)):
                if self.isSafe(
                    image, 
                    currr+rows[i], 
                    currc+cols[i],
                    og_color,
                    visited
                    ):
                    queue.append((currr+rows[i], currc+cols[i]))

    def isSafe(self, image, x, y, og_color, visited):
        # 2, 0
        return (x >= 0 
        and x < len(image) 
        and y >= 0 
        and y < len(image[0])
        and image[x][y] == og_color
        and not visited[x][y]
        )

