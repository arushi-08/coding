class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        
        # make atleast 1 valid path in grid
        # grid[i][j] = 1 -> right
        # 2 -> left
        # 3 -> lower cell
        # 4 -> upper cell
        
        m = len(grid)
        n = len(grid[0])
        directions = {1:[0,1], 2:[0,-1], 3:[1,0], 4:[-1,0]}
        
        # use bfs
        queue = deque()
        queue.append((0,0,0))
        visited = {}
        visited[(0,0)] = 0
        while queue:
            currx, curry, cost = queue.popleft()
            
            dx, dy = directions[grid[currx][curry]]
            if 0 <= currx+dx < m and 0 <= curry+dy < n and visited.get((currx+dx, curry+dy), float('inf')) > cost:
                queue.append((currx+dx, curry+dy, cost))
                visited[(currx+dx, curry+dy)] = cost
            
            for cand_dx, cand_dy in directions.values():
                if [cand_dx, cand_dy] != [dx,dy] and 0 <= currx+cand_dx < m and 0 <= curry+cand_dy < n and visited.get((currx+cand_dx, curry+cand_dy), float('inf')) > cost+1:
                    queue.append((currx+cand_dx, curry+cand_dy, cost+1))
                    visited[(currx+cand_dx, curry+cand_dy)] = cost+1

        return visited[(m-1,n-1)]







