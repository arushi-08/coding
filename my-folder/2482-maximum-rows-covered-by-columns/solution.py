class Solution:
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        
        # backtracking

        bitmask_mat = [0] * len(matrix)
        for i in range(len(matrix)):
            r = 0
            for j in range(len(matrix[i])):
                r = 2*r + matrix[i][j]
            bitmask_mat[i] = r

        max_rows_covered = 0

        def backtrack(selected_cols, idx, count):
            nonlocal max_rows_covered

            if count == numSelect:

                n_rows_covered = 0
                # for loop
                for r in bitmask_mat:
                    if r & selected_cols == r:
                        n_rows_covered += 1
                    
                max_rows_covered = max(max_rows_covered, n_rows_covered)
                return
            
            for col in range(idx, len(matrix[0])):
                if selected_cols & 1 << col == 0:
                    backtrack(selected_cols | 1 << col, col+1, count+1)
 
        
        selected_cols = [0] * len(matrix[0])
        count = 0
        backtrack(0, 0, count)

        return max_rows_covered
# [
    # [0,0,1],
    # [1,0,0],
    # [0,0,0]
# ]





