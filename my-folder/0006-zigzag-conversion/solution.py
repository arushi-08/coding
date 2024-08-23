class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # |   |
        # |  /|
        # | / |
        # |   |

        # create matrix: numRows x  numRows
        # populate:
        #   1st column
        #   1st diagonal bottom left to top right
        #   next (could be 3rd or 4th) column
        #   repeat steps


        matrix = [['']* len(s) for _ in range(numRows)]

        r = 0
        c = 0

        diagonal = False
        # P     I    N
        # A   L S  I G
        # Y A   H R
        # P     I

    #    [
    #     ['P', '', 'A', '', 'H', '', 'N', '', '', '', '', '', '', ''], 
    #     ['A', 'P', 'L', 'S', 'I', 'I', 'G', '', '', '', '', '', '', ''], 
    #     ['Y', '', 'I', '', 'R', '', '', '', '', '', '', '', '', '']
    #     ]

        for i in range(len(s)):
            
            if r == len(matrix):
                if r - 2 >= 0:
                    r -= 2
                else:
                    r -= 1
                c += 1
                diagonal = True

            elif r < 0:
                if len(matrix) >= 2:
                    r = 1
                    c -= 1
                else:
                    r = 0

                diagonal = False
            
            matrix[r][c] = s[i]
            
            if diagonal:
                r -= 1
                c += 1
            else:
                r += 1
        
        output = ''

        for i in range(len(matrix)):
            output += ''.join(matrix[i])

        return ''.join(output)
