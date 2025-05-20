class Solution:
    def specialGrid(self, n: int) -> List[List[int]]:
        
        # quadrant defined by offset, size
        # 

        def helper(level, r, c, val):
            
            if level == 0:
                result[r][c] = val
                return
            
            size = 2**level
            half_size = size//2
            max_num_in_quad = half_size*half_size

            helper(level-1, r, c+half_size, val + 0 * max_num_in_quad )
            helper(level-1, r+half_size, c+half_size, val + 1 * max_num_in_quad)
            helper(level-1, r+half_size, c, val + 2 * max_num_in_quad)
            helper(level-1, r, c, val + 3 * max_num_in_quad)

        size = 2**n
        result = [[0] * size for _ in range(size)]
        helper(n, 0, 0, 0 )
        return result
