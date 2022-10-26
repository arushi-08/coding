from collections import Counter
class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        
#         m * n picture of Black B and white W
#         return # Black lonely pixel
        black_rows = []
        black_cols = []
        for i in range(len(picture)):
            for j in range(len(picture[0])):
                if picture[i][j] == 'B':
                    black_rows.append(i)
                    black_cols.append(j)
        
#         [0, 1 ,2]   [2, 2, 0]
        row_map = Counter(black_rows)
        col_map = Counter(black_cols)
        ans = 0
        for i, j in zip(black_rows, black_cols):
            if row_map[i] == 1 and  col_map[j] == 1:
                ans += 1
        return ans
