class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        
        # 2d int arrays - guards and walls
        # guards[i] = [rowi, coli] -> ith guard -> can see every cell in 4 directions, except if there's a wall
        # walls[j] = [rowj, colj] -> jth wall
        # a cell is guarded if there's atleast 1 guard that can see it

        # count number of unoccupied cells that are not guarded

        # put all guards in a queue
        # bfs around guards
        # remaining - walls are all unguarded

        row = [1, 0, -1, 0]
        col = [0, 1, 0, -1]

        walls_set = set(tuple(wall) for wall in walls)
        guards_set = set(tuple(guard) for guard in guards)

        grid = [[0] * n for _ in range(m)]

        rows_covered = set()
        cols_covered = set()
        count = 0
        guards.sort()
        for i in range(len(guards)):
            inside_rows = False
            inside_cols = False
            currx, curry = guards[i]
            grid[currx][curry] = 1
            
            for j in range(4):
                if row[j] == -1:
                    for k in range(min(m-1, currx+row[j]), -1, -1):
                        grid[k][curry+col[j]] = 1
                        if (k, curry+col[j]) in walls_set:
                            break
                        if (k, curry+col[j]) in guards_set:
                            break
                        inside_rows = True

                elif row[j] == 1:
                    for k in range(max(0,currx+row[j]), m):
                        grid[k][curry+col[j]] = 1
                        if (k, curry+col[j]) in walls_set:
                            break
                        if (k, curry+col[j]) in guards_set:
                            break
                        inside_rows = True

                elif col[j] == -1:
                    for k in range(min(n-1, curry+col[j]), -1, -1):
                        grid[currx+row[j]][k] = 1
                        if (currx+row[j], k) in walls_set:
                            break
                        if (currx+row[j], k) in guards_set:
                            break
                        inside_cols = True

                elif col[j] == 1:
                    for k in range(max(0, curry+col[j]), n):
                        grid[currx+row[j]][k] = 1
                        if (currx+row[j], k) in walls_set:
                            break
                        if (currx+row[j], k) in guards_set:
                            break
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not grid[i][j] and (i,j) not in walls_set:
                    count += 1

        return count
