from collections import deque
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        
        board_str = "".join([str(i) for b in board for i in b])
        if board_str == "123450": return 0
        queue = deque()
        queue.append((board_str, board_str.index("0"), 0))
        seen = {board_str}
        neighbors = {0:{1,3},1:{0,2,4},2:{1,5},3:{0,4},4:{1,3,5},5:{2,4}}
        
        while len(queue):
            board_str, digit, moves = queue.popleft()
            if board_str == "123450": return moves
            
            for next_digit in neighbors[digit]:
                ns = self.swap(board_str, digit, next_digit)
                print(ns)
                if ns not in seen:
                    queue.append((ns, next_digit, moves+1))
                    seen.add(ns)
                    if ns == "123450": return moves + 1
        return -1
    
    def swap(self, board_str, digit_idx, next_digit_idx):
        if digit_idx < next_digit_idx:
            return (board_str[:digit_idx] + board_str[next_digit_idx] 
                    + board_str[digit_idx+1:next_digit_idx] 
                    + board_str[digit_idx] + board_str[next_digit_idx+1:]
                   )
        else:
            return (board_str[:next_digit_idx] + board_str[digit_idx] 
                    + board_str[next_digit_idx+1:digit_idx] 
                    + board_str[next_digit_idx] + board_str[digit_idx+1:]
                   )
