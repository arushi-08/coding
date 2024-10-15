class Solution:
    def minimumSteps(self, s: str) -> int:
        
        # min steps to get black right white left
        # 1 - black
        # 0 - white
        # 101 -> 011
        s = list(s)
        moves = 0
        placed = len(s)-1
        for i in range(len(s)-1,-1,-1):
            if s[i] == '1':
                moves += placed-i
                placed -= 1
                
        return moves
