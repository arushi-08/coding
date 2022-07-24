from collections import deque
class Solution:
    def isSafe(self, x, y, heights, visited):
        return (x >= 0 
               and y >= 0
               and x < len(heights)
               and y < len(heights[0])
               and visited[x][y] == False)
    
    def get_ocean_graph(self, heights, ocean_type):
        
        ocean_graph = [[0] * len(heights[0]) for _ in range(len(heights))]
        visited = [[False] * len(heights[0]) for _ in range(len(heights))]
        queue = deque()
        
        if ocean_type == "pacific":
            ocean_graph[0] = [1] * len(heights[0])
            
            for i in range(len(ocean_graph[0])):
                queue.append((0,i))
                visited[0][i] = True
                
            for i in range(len(ocean_graph)):
                ocean_graph[i][0] = 1
                queue.append((i,0))
                visited[i][0] = True
        else:
            ocean_graph[-1] = [1] * len(heights[0])
            
            for i in range(len(ocean_graph[-1])):
                queue.append((len(heights)-1,i))
                visited[len(heights)-1][i] = True
                
            for i in range(len(ocean_graph)):
                ocean_graph[i][-1] = 1
                queue.append((i,len(heights[0])-1))
        
                visited[i][len(heights[0])-1] = True
        
        while queue:
            curr_x, curr_y = queue.popleft()
            
            possible_moves_x = [1, 0, -1, 0]
            possible_moves_y = [0, -1, 0, 1]
            
            for x, y in zip(possible_moves_x, possible_moves_y):
                if (self.isSafe(curr_x+x, 
                                curr_y+y, 
                                heights, 
                                visited)
                   and heights[curr_x][curr_y] <= heights[curr_x+x][curr_y+y]):
                    ocean_graph[curr_x+x][curr_y+y] = 1
                    visited[curr_x+x][curr_y+y] = True
                    queue.append((curr_x+x, curr_y+y))
                    
        return ocean_graph
    
        
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        pacific_graph = self.get_ocean_graph(heights, "pacific")
        # print("pacific", pacific_graph)
        atlantic_graph = self.get_ocean_graph(heights, "atlantic")
        # print("atlantic", atlantic_graph)
        
        ans = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if pacific_graph[i][j] == 1 and atlantic_graph[i][j] == 1:
                    ans.append([i,j])
        
        return ans
        
        
