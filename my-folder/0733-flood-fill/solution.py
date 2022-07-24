from collections import deque
class Solution:
    def isSafe(self, x, y, visited, image, current_color):
        return (x >= 0 
                and y >= 0 
                and x < len(image) 
                and y < len(image[0]) 
                and visited[x][y] == False
                and image[x][y] == current_color)
        
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        current_color = image[sr][sc]
        
        visited = [[False]*len(image[0]) for _ in range(len(image))]
        visited[sr][sc] = True
        
        queue = deque()
        queue.append((sr, sc))
        
        while queue:
            curr_x, curr_y = queue.popleft()
            image[curr_x][curr_y] = color
            
            possible_moves_x = [1, 0, -1, 0]
            possible_moves_y = [0, -1, 0, 1]
            
            for x, y in zip(possible_moves_x, possible_moves_y):
                if self.isSafe(curr_x + x, 
                               curr_y + y, 
                               visited, 
                               image, 
                               current_color):
                    visited[curr_x + x][curr_y + y] = True
                    queue.append((curr_x + x, curr_y + y))
                    
        return image
