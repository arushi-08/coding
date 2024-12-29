class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
         
        #  return true if there's a circle and robot always returns back to it

        # GGLLGG
        """
         --
        |  |
        |  |
         --
        
        if odd number of L or R return true
        # if its G
        GGLGG
           -
            |
            - -
            LGRGLG

        GLGLGGLGL


                -
               | |
               |
                -


                |
                 -
                 L
                 (3,-4)
                 (4, 5)
        """

        l_steps = instructions.count('L')
        r_steps = instructions.count('R')

        if not l_steps and not r_steps:
            return False
        
        x,y = 0, 0
        dx, dy = 0, 1
        for i in range(len(instructions)):
            if instructions[i] == 'G':
                x += dx
                y += dy
            elif instructions[i] == 'L':
                dx, dy = -dy, dx
            elif instructions[i] == 'R':
                dx, dy = dy, -dx
        # print(x,y, curr_dir)
        return [x,y] == [0,0] or [dx,dy]!=[0,1]

        
