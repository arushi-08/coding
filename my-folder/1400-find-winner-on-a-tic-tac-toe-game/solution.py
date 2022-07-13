class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        """scores[0] scores[1] scores[2] for rows
           scores[3] scores[4] scores[5] for cols
           scores[6] scores[7] for diagonals
        """
        scores = [0]*8
        for i, (row, col) in enumerate(moves):
            if i % 2 == 0: score = 1
            else: score = -1
            
            scores[row] += score
            scores[col + 3] += score
            if row == col: scores[6] += score
            if 2 - row == col: scores[7] += score
            
        for score in scores:
            if score == 3: return "A"
            if score == -3: return "B"
        return "Draw" if len(moves) == 9 else "Pending"
        
        
        
