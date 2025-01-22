class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        
        """
        track prefix_bottom & suffix_top
        aim: find the switching point for robot 1
        """
        prefix_bottom = 0
        suffix_top = sum(grid[0])

        robot_1_switching_idx = 0
        n = len(grid[0])

        minimax_sum = float('inf')
        while robot_1_switching_idx < n:
            
            if robot_1_switching_idx > 0:
                prefix_bottom += grid[1][robot_1_switching_idx-1]
            
            suffix_top -= grid[0][robot_1_switching_idx]
            
            minimax_sum = min(minimax_sum, max(prefix_bottom, suffix_top))
            robot_1_switching_idx += 1

        return minimax_sum
