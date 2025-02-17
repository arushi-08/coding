class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        l_steps = instructions.count('L')
        r_steps = instructions.count('R')

        if l_steps == 0 and r_steps == 0:
            return False
        
        x, y = 0, 0
        dx, dy = 0, 1
        period = 4
        while period:
            for instruction in instructions:
                if instruction == 'G':
                    x += dx
                    y += dy
                elif instruction == 'L':
                    dx, dy = -dy, dx
                else:
                    dx, dy = dy, -dx
            
            if [x,y] == [0,0]:
                return True
            
            period -= 1
        
        return False
        
