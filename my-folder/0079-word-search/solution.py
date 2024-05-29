class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        # dfs - similar to #islands

        for i in range(len(board)):
            for j in range(len(board[0])):
                visited = set()
                if board[i][j] == word[0]:
                    visited.add((i, j))
                    ans = self.dfs(i, j, board, word, 1, visited)
                    if ans:
                        return True

        return False
    
    def dfs(self, x, y, board, word, idx, visited):
        
        if idx == len(word):
            return True

        rows = [0, 1, 0, -1]
        cols = [1, 0, -1, 0]

        for i in range(len(rows)):
            if self.isSafe(x+rows[i], y+cols[i], board, word, idx, visited):
                visited.add((x+rows[i], y+cols[i]))
                ans = self.dfs(x+rows[i], y+cols[i], board, word, idx + 1, visited)
                if ans:
                    return ans
                else:
                    visited.remove((x+rows[i], y+cols[i]))
        
        return False
    
    def isSafe(self, x, y, board, word, idx, visited):
        return x >= 0 and y >= 0 and x < len(board) and y < len(board[0]) and board[x][y] == word[idx] and (x,y) not in visited
        

