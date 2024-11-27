class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        
        # given m x n binary matrix
        # flip column every cell
        # max number of rows that have all values equal after some number of flips
        # 0,0,1
        # 0,0,0
        # 1,1,1
        # ans = 2
        # aim get max rows all same values

        # cannot do backtracking, size = 300
        # brute force way would be 
        # 
        # 
        
        # track how many cols have mismatch cells with majority value in rows
        # if these are swapped do we get max rows?
        #   problem with this - what if finding the majority value is not leading us to answer of whether we should swap cells
        #   e.g.
        #       0,1 - no majority
        #       1,1
        #       
        #       0,0,0,1,0 - 0
        #       1,1,0,0,0 - 0
        #       0,0,1,1,1 - 1

        #   1 row's majority value swapping, can change the other rows
        
        # frequency of the most common pattern across all rows in the matrix
        freq_map = {}
        for i in range(len(matrix)):
            pattern = '*'
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == matrix[i][j-1]:
                    pattern += '*'
                else:
                    pattern += '|'
            freq_map[pattern] = freq_map.get(pattern, 0) + 1
            
        
        return max(freq_map.values())



