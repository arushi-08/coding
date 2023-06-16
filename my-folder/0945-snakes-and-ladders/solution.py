from collections import deque
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
# [
#     [-1,-1,-1,-1,-1,-1],
#     [-1,-1,-1,-1,-1,-1],
#     [-1,-1,-1,-1,-1,-1],
#     [-1,35,-1,-1,13,-1],
#     [-1,-1,-1,-1,-1,-1],
#     [-1,15,-1,-1,-1,-1]
# ]
        def inttopos(position, n):
            # 1 - 5,0 n-1, 0 (1 to n) - n-1
            # 2 - 5,1 n-1, 1 (2n to n+1) - n-2
            # 3 - 5,2 n-1, 2 (2n+1 to 3n) - n-3
            # 12- 4,0 n-2, 0 (4n to 3n+1) - n-4
            row = (position - 1) // n
            col = (position - 1) % n 
            if row % 2:
                col = n - 1 - col
            return row, col
        
        n = len(board)
        board.reverse()
        visited = set()
        queue = deque()
        queue.append((1, 0))
        while len(queue):
            currpos, currmoves = queue.popleft()
            for nextmove in range(currpos+1, min(currpos+6, n**2)+1):
                row, col = inttopos(nextmove, n)
                val_nextmove = board[row][col]
                if val_nextmove != -1:
                    nextmove = val_nextmove
                if nextmove == n**2:
                    return currmoves + 1
                if nextmove not in visited:
                    visited.add(nextmove)
                    queue.append((nextmove, currmoves+1))
        if currpos == n**2:
            return currmoves
        return -1
            
[
    [-1,-1,19,10,-1],
    [ 2,-1,-1, 6,-1],
    [-1,17,-1,19,-1],
    [25,-1,20,-1,-1],
    [-1,-1,-1,-1,15]
]
