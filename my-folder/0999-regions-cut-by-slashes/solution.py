class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:

        # build graph
        ROWS_GRID = len(grid[0])
        ROWS_GRAPH = len(grid[0])*3
        COLS_GRID = len(grid)
        COLS_GRAPH = len(grid)*3

        graph = [[1]*ROWS_GRAPH for _ in range(COLS_GRAPH)]

        for i in range(ROWS_GRID):
            for j in range(COLS_GRID):
                if grid[i][j] == ' ':
                    continue

                st_row = i*3
                st_col = j*3
                if grid[i][j] == '/':
                    for k in range(3):
                        graph[st_row + k][st_col + 2 - k] = 0
                    
                elif grid[i][j] == '\\':
                    for k in range(3):
                        graph[st_row + k][st_col + k] = 0
        
        # print(graph)
        return self.count_islands(graph)
    
    def count_islands(self, graph):

        r = len(graph)
        c = len(graph[0])

        ans = 0
        for i in range(r):
            for j in range(c):
                if graph[i][j]:
                    self.bfs(graph, i, j)
                    ans += 1
        return ans
    
    def bfs(self, graph, x, y):

        queue = deque()
        queue.append((x, y))
        graph[x][y] = 0

        rows = [1,0,-1,0]
        cols = [0,1,0,-1]

        while queue:
            currx, curry = queue.popleft()

            for i in range(4):
                if self.is_safe(currx + rows[i], curry + cols[i], graph):
                    graph[currx + rows[i]][curry + cols[i]] = 0
                    queue.append((currx + rows[i], curry + cols[i]))
        
    
    def is_safe(self, x, y, graph):
        return 0 <= x < len(graph) and 0 <= y < len(graph[0]) and graph[x][y]





        

