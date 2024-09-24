class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        
        # return 2d matrix
        # size of matrix is rowSum size * colSum size
        # x1 + x2 + x3 .. = rowSum[i]
        # 
        # [3,0]
        # [1,7]
        # [5,0,0]
        # [3,4,0]
        # [0,2,8]

        # give the min(rowSum[i], colSum[i]) to matrix[i][0]
        # keep doing it 

        N_ROWS = len(rowSum)
        N_COLS = len(colSum)
        matrix = [[0]*N_COLS for _ in range(N_ROWS)]

        for i in range(N_ROWS):
            for j in range(N_COLS):
                matrix[i][j] = min(rowSum[i], colSum[j])
                rowSum[i] -= matrix[i][j]
                colSum[j] -= matrix[i][j]

        return matrix


        
