class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for row in range(len(board)):
            for col in range(len(board[0])):
                if self.backtrack(board, word, row, col):
                    return True

    def backtrack(self, board, word, i, j):
        
        if not word: return True

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j]!=word[0]:
            return False
        

        board[i][j] = '#'
        rows = [1, 0, -1, 0]
        cols = [0, 1, 0, -1]
        for k in range(len(rows)):
            if self.backtrack(board, word[1:], i+rows[k], j+cols[k]):
                return True
        
        board[i][j] = word[0]
        
        return False
