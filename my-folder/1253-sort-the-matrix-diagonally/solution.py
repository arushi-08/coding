class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        
        r = len(mat)
        c = len(mat[0])
        
        diag = defaultdict(list)
        visited = set()
        for i in range(r):
            for j in range(c):
                for k in range(c+r):
                    if i + k < r and j + k < c and (i+k, j+k) not in visited:
                        if (i-1, j-1) in diag:
                            diag[(i-1,j-1)].append(mat[i+k][j+k])
                        else:
                            diag[(i,j)].append(mat[i+k][j+k])
                        visited.add((i+k, j+k))

        print(diag)

        ans = [[0]*len(mat[0]) for _ in range(len(mat))]
        for k in diag:
            temp = diag[k]
            temp.sort()
            x,y = k
            for i,t in enumerate(temp):
                if i + x < r and y + i < c:
                    ans[x+i][y+i] = t
                    
        return ans


