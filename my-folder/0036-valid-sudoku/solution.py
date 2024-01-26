from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # use hash set or array that's fine

        rows = defaultdict(set)
        cols = defaultdict(set)
        box = defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in box[(i//3,j//3)] or board[i][j] in rows[i] or board[i][j] in cols[j]:
                        return False
                    else:
                        rows[i].add(board[i][j])
                        cols[j].add(board[i][j])
                        box[(i//3,j//3)].add(board[i][j])
                
        return True
