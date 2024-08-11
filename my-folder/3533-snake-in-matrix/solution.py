class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        
        command_map = {'RIGHT':[0,1],
        'LEFT':[0,-1],
        'DOWN':[1,0],
        'UP':[-1,0]}

        newposx = 0
        newposy = 0
        for cmd in commands:

            x, y = command_map[cmd]
            newposx += x
            newposy += y

        return newposx*n + newposy
