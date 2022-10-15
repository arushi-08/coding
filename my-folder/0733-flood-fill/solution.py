from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        return self.bfs(image, sr, sc, image[sr][sc], color)
    
    def bfs(self, image, sr, sc, orig_color, color):
        
        q = deque()
        q.append((sr, sc))
        rows = [1, 0, -1, 0]
        cols = [0, 1, 0, -1]
        visited = [[False] * len(image[0]) for i in range(len(image))]
        while q:
            curr_row, curr_col = q.popleft()
            image[curr_row][curr_col] = color
            for i in range(4):
                if self.isSafe(image, 
                               curr_row + rows[i], 
                               curr_col + cols[i], 
                               orig_color,
                               visited
                              ):
                    q.append((curr_row + rows[i], curr_col + cols[i]))
                    visited[curr_row + rows[i]][curr_col + cols[i]] = True
        
        return image
    
    def isSafe(self, image, row, col, orig_color, visited):
        return 0 <= row and row < len(image) and 0 <= col and col < len(image[0]) and image[row][col] == orig_color and not visited[row][col]
                    
            
        
