class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        

        # n queens - place them - dont attack


        # how do we place them
        # backtracking
        # put queen on pos 1
        # next queen at pos 2
        # 0,0 1,2 == 0,1 2,1
        # attack condn - x1 != x2 y1 != y2 x1 - y1 != x2 - y2 
        def not_attack(x, y, diag, reverse_diag, x2, y2, visited):
            if len(y) == 0:
                return True
            return x2 not in x and y2 not in y and x2-y2 not in diag and x2+y2 not in reverse_diag and (x2, y2) not in visited

        placements = []
        def dfs(horizontals, verticals, diag, reverse_diag, i, placements, curr_placement, visited):
            if i == n:
                placements.append(curr_placement)
                return 
            
            for j in range(n):
                if not_attack(horizontals, verticals, diag, reverse_diag, i, j, visited):
                    visited.add((i, j))
                    dfs(horizontals + [i], verticals + [j], 
                    diag + [i-j], reverse_diag + [i+j], 
                    i+1, placements, curr_placement + ['.'*j + 'Q' + '.'*(n-j-1)], 
                    visited)
                    visited.remove((i, j))
        
        dfs([], [], [], [], 0, placements, [], set())
        return placements
        # 
        # if i+j == x+y -> (i,j) and (x,y) are on same reverse diagonal
