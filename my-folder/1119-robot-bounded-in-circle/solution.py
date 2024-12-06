class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        

        # robot faces north initial direction (0,0)
        # G : go straight 1 unit
        # L : turn left, not go left
        # R : turn right, not go right

        # key point: robot repeats instruction forever

        # if robot ends in north direction and not in initial position -> false
        # 
        x,y = 0,0
        dir_x, dir_y = 0,1

        for i in range(len(instructions)):
            if instructions[i] == 'G':
                x += dir_x
                y += dir_y
                
            elif instructions[i] == 'L':
                dir_y, dir_x = dir_x, -1*dir_y 
                
            elif instructions[i] == 'R':
                dir_x, dir_y = dir_y, -1*dir_x
            
        # print(x,y, dir_x, dir_y) 
        return [x,y] == [0,0] or [dir_x, dir_y] != [0,1] # VVV IMP condition
        

