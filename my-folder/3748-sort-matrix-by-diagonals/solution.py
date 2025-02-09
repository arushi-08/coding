class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:

        # sort bottom half diag in decreasing order
        n = len(grid)
        
        for i in range(n-2,-1,-1):
            diag = []
            for j in range(n):
                if i+j >= n: break
                diag.append(grid[i+j][j])
            diag.sort(reverse=True)
            k = 0
            for j in range(n):
                if i+j >= n: break
                grid[i+j][j] = diag[k]
                k += 1
                
        # for i in range(n-2,-1,-1):
        #     diag = []
        #     for j in range(n):
        #         if i+j >= n: break
        #         diag.append(grid[i+j][j])
        #     diag.sort()
        #     k = 0
        #     for j in range(n):
        #         if i+j >= n: break
        #         grid[i+j][j] = diag[k]
        #         k += 1
                
        for i in range(1, n-1):
            diag = []
            k = i
            for j in range(n-1,-1,-1):
                # i = 1, j = n-1
                # i = 0, j = n-2

                # i = 2, j = n-1
                if k < 0: break
                diag.append(grid[k][j])
                k -= 1
            # print(diag)
            diag.sort(reverse=True)
            diag_idx = 0
            k = i
            # print(k)
            for j in range(n-1,-1,-1):
                if k < 0: break
                # print(diag, diag_idx, k)
                grid[k][j] = diag[diag_idx]
                diag_idx += 1
                k -= 1

        return grid
