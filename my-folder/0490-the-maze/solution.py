class Solution:
    def __init__(self):
        self.visited = set()
        self.directions = ['left', 'up', 'right', 'down']

    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        
        if start == destination:
            return True
        
        self.visited.add((start[0], start[1]))
        return self.dfs(maze, start, destination)
    
    def dfs(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        
        if start == destination:
            return True
        found = False
        
        rows = [-1, 0, 1, 0]
        cols = [0, 1, 0, -1]

        x,y = start

        def get_next_location(direction, curr_location):
            row, col = curr_location
            if direction == 'up':
                while row > 0 and maze[row-1][col] != 1:
                    row -= 1
            elif direction == 'down':
                while row < len(maze)-1 and maze[row+1][col] != 1:
                    row += 1
            elif direction == 'left':
                while col > 0 and maze[row][col-1] != 1:
                    col -= 1
            else:
                while col < len(maze[0])-1 and maze[row][col+1] != 1:
                    col += 1

            return row, col
        
        for direction in self.directions:
            next_row, next_col = get_next_location(direction, start)
            if (next_row, next_col) not in self.visited:
                self.visited.add((next_row, next_col))
                print(next_row, next_col)
                if self.dfs(maze, [next_row, next_col], destination):
                    return True
                # self.visited.remove((next_row, next_col))

        return False

