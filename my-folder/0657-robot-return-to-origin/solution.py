class Solution:
    def judgeCircle(self, moves: str) -> bool:
        
        move_directions = {'U':[0,1],'D':[0,-1],'R':[1,0],'L':[-1,0]}

        currx, curry = 0,0
        for move in moves:
            x,y = move_directions[move]
            currx += x
            curry += y
        
        return [currx, curry] == [0,0]
