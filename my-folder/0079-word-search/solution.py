class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        res = False
        rows = len(board)
        cols = len(board[0])
        visit = set()
        def dfs(x, y, visit, index):
            if index == len(word): return True

            if x < 0 or y < 0 or x == rows or y == cols or (x,y) in visit or board[x][y] != word[index]:
                return False

            visit.add((x,y))
            ans= (dfs(x+1, y, visit, index+1) | 
            dfs(x, y+1, visit, index+1) | 
            dfs(x-1, y, visit, index+1) |
            dfs(x, y-1, visit, index+1)
            )
            visit.remove((x,y))
            return ans
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    ans = dfs(i, j, visit, 0)
                    if ans:
                        return ans
        return False
