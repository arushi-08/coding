from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        visited = [[False]*len(image[0]) for _ in range(len(image))]
        self.bfs(image, sr, sc, color, visited)
        return image
    
    def bfs(self, image, sr, sc, color, visited):
        
        queue = deque()
        queue.append((sr, sc))
        visited[sr][sc] = True
        rows_list = [0, 1, 0, -1]
        cols_list = [1, 0, -1, 0]
        curr_color = image[sr][sc]
        
        while len(queue):
            cur_row, cur_col = queue.popleft()
            print(cur_row, cur_col)
            image[cur_row][cur_col] = color
            
            for i in range(len(rows_list)):
                if self.isSafe(image, 
                               cur_row + rows_list[i],
                               cur_col + cols_list[i],
                               visited,
                               curr_color
                              ):
                    queue.append((cur_row + rows_list[i], cur_col + cols_list[i]))
                    print(queue)
                    visited[cur_row + rows_list[i]][cur_col + cols_list[i]] = True
    
    def isSafe(self, image, row, col, visited, color):
        return (
            row >= 0 and
            col >= 0 and
            row < len(image) and
            col < len(image[0]) and
            not visited[row][col] and
            image[row][col] == color
        )
                
