class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        # white rook - no diagonals , white bishop - only diagonals
        # black queen

        # we can only move white pieces
        # min num of moves to capture black queen

        # while true:
        #   is queen in direct path of rook or bishop
        #   go to closest point to queen either through rook or bishop
        
        rook_x, rook_y = a,b
        bishop_x, bishop_y = c,d
        queen_x, queen_y = e,f

        if queen_x == rook_x:
            if bishop_x == rook_x and (bishop_y - rook_y) * (bishop_y - queen_y) < 0:
                return 2
            return 1
        
        if queen_y == rook_y:
            if bishop_y == rook_y and (bishop_x - rook_x) * (bishop_x - queen_x) < 0:
                return 2
            return 1

        if abs(bishop_x-queen_x) == abs(bishop_y-queen_y):
            if abs(rook_x-bishop_x) == abs(rook_y-bishop_y) and (rook_y-bishop_y) * (rook_y-queen_y) < 0:
                    return 2
            return 1
        
        return 2
