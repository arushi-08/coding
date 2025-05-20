class Solution:
    def countCells(self, grid: List[List[str]], pattern: str) -> int:
        
        # given m*n matrix grid
        # of characters and a string pattern

        # horizontal substring is a contiguous seq
        # read from left to right

        # if end of a row is reached before substring is complete
        # it wraps to the first column of the next row and continues as needed

        # do not wrap from the bottom row back to the top

        # make 1 long string by wrapping next rows/cols
        # get idx that are having the pattern

        # do idx sets intersection, return size

        # st + row_num * col size
        # 0,1,2,3, 1*4, 1+1*4, 2+1*4

        row_order = []
        rowsize = len(grid)
        colsize = len(grid[0])

        for i in range(rowsize):
            for j in range(colsize):
                row_order.append( [j + i*colsize, grid[i][j]] ) 
        # print('row', new_order)
        row_sets = self.get_sets(row_order, pattern)

        col_order = []
        for i in range(colsize):
            for j in range(rowsize):
                col_order.append( [i + j*colsize, grid[j][i]] ) 
        # print('col', new_order)
        col_sets = self.get_sets(col_order, pattern)

        return len(row_sets.intersection(col_sets))
    
    def get_sets(self, new_order, pattern):
        """
        change n^2 -> n
        """

        pattern_size = len(pattern)
        result = set()
        lps = self.build_lps(pattern)
        j = 0
        diff = [0] * (len(new_order) + 1)

        for i in range(len(new_order)):
            
            while j > 0 and new_order[i][1] != pattern[j]:
                j = lps[j-1]

            if new_order[i][1] == pattern[j]:
                j += 1

            if j == len(pattern):
                start = i - j + 1
                diff[start] += 1
                diff[start+j] -= 1
                # for k in range(start, start+j):
                #     result.add(new_order[k][0])
                j = lps[j-1]
        running = 0
        for i in range(len(diff)):
            running += diff[i]
            if running:
                result.add(new_order[i][0])
                
        # print('set', result)
        return result

    def build_lps(self, pattern):
        patt_len = len(pattern)
        lps = [0] * patt_len
        i = 1
        length = 0 # len of prev lps
        while i < patt_len:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length-1]
                else:
                    lps[i] = 0
                    i += 1

        return lps
