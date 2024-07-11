class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        # think in reverse
        # how many ways can i move to each position in matrix start from boundary
        if not maxMove: return 0

        rows = [0,1,0,-1]
        cols = [1,0,-1,0]
        visited = {}

        k_mod = 10**9+7
        def dfs(x,y,moves):
            if moves == 0:
                return x < 0 or x == m or y < 0 or y == n
            
            if (x,y,moves) in visited:
                return visited[(x,y,moves)]

            if x < 0 or x == m or y < 0 or y == n:
                return 1
            
            visit = 0
            for i in range(4):
                visit += dfs(x+rows[i], y+cols[i], moves-1) 
            visited[(x,y,moves)] = visit % k_mod

            return visited[(x,y,moves)]

        return dfs(startRow, startColumn, maxMove)

        
# 1 step
# 2,1,2
# 1,0,1
# 2,1,2

# 2 steps
# 2,4,2
# 4,4,4
# 2,4,2

# 3 steps
# 8,8,8
# 8,16,8
# 8,8,8

# 4 steps
# 16,32,16
# 32,32,32
# 16,32,16
