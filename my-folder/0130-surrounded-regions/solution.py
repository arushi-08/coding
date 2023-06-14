from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = [[False]*len(board[0]) for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i == 0 or j == 0 or i == len(board)-1 or j == len(board[0])-1) and not visited[i][j] and board[i][j]=='O':
                    visited[i][j] = True
                    self.bfs(board, i, j, visited, ffill=False)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if not visited[i][j] and board[i][j] == 'O':
                    visited[i][j] = True
                    board[i][j] = 'X'
                    self.bfs(board, i, j, visited, ffill=True)

    def bfs(self, board, x, y, visited, ffill):
        queue = deque()
        queue.append((x, y))
        rows = [1, 0, -1, 0]
        cols = [0, 1, 0, -1]
        while len(queue):
            currx, curry = queue.popleft()
            for i in range(len(rows)):
                if self.isSafe(
                    board, 
                    currx+rows[i],
                    curry+cols[i],
                    visited
                ):
                    visited[currx+rows[i]][curry+cols[i]] = True
                    queue.append((currx+rows[i], curry+cols[i]))
                    if ffill:
                        board[currx+rows[i]][curry+cols[i]] = 'X'
    
    def isSafe(self, board, x, y, visited):
        return (
            x >= 0 and
            y >= 0 and
            x < len(board) and
            y < len(board[0]) and
            not visited[x][y] and
            board[x][y] == 'O'
        )


        
