class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        
        def dfs(x,y, moves, visit):
            if moves == 0:
                return x < 0 or x == m or y < 0 or y == n
            
            if (x,y,moves) in visit:
                return visit[(x,y,moves)]
            
            if x < 0 or x == m or y < 0 or y == n:
                return 1
            
            rows = [1,0,-1,0]
            cols = [0,1,0,-1]
            count = 0
            for i in range(4):
                count += dfs(x+rows[i],y+cols[i],moves-1,visit)
            
            visit[(x,y,moves)] = count

            return count

        visit = {}
        return dfs(startRow,startColumn, maxMove, visit) % (10**9+7)

