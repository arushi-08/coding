class Solution:
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        
        # do backtrack on columns selected
        # store max_rows_covered

        max_rows_covered = 0
        selected_cols = set()

        def dfs(idx, selected_cols):
            nonlocal max_rows_covered

            if len(selected_cols) == numSelect:
                n_rows_covered = 0

                for i in range(len(matrix)):
                    row_covered = True
                    for j in range(len(matrix[0])):
                        if matrix[i][j] and j not in selected_cols:
                            row_covered = False
                    if row_covered:
                        n_rows_covered += 1
                
                max_rows_covered = max(
                    max_rows_covered, n_rows_covered
                    )
                return
            
            for i in range(idx, len(matrix[0])):
                if i not in selected_cols:
                    selected_cols.add(i)
                    dfs(idx+1, selected_cols)
                    selected_cols.remove(i)

        dfs(0, selected_cols)
        return max_rows_covered
