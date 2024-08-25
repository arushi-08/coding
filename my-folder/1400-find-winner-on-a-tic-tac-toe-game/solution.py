class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        
        # A plays X
        # B plays O
        # A will play first
        # 3x3 grid
        # just check for matrix[x][:] and then matrix[:][y] for them to be matrix[x][y] (current piece)

        # [[0,0],[2,0],[1,1],[2,1],[2,2]]

        matrix = [['']*3 for _ in range(3)]

        for i in range(len(moves)):
            x,y = moves[i]
            if i & 1 == 0:
                matrix[x][y] = 'A'
            else:
                matrix[x][y] = 'B'
            
            if i >= 4:
                if matrix[x][0] == matrix[x][1] == matrix[x][2] == matrix[x][y]:
                    return matrix[x][y]
                
                if matrix[0][y] == matrix[1][y] == matrix[2][y] == matrix[x][y]:
                    return matrix[x][y]
                    
                if matrix[0][0] == matrix[1][1] == matrix[2][2] == matrix[x][y]:
                    return matrix[x][y]
                
                if matrix[0][2] == matrix[1][1] == matrix[2][0] == matrix[x][y]:
                    return matrix[x][y]

        if len(moves) == 9:
            return 'Draw'
        
        return 'Pending'

