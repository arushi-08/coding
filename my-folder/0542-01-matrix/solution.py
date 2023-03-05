from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        Step 1: get list of all zeros and all ones
        Step 2: calculate for each ones the closest zero position
        """
        output = [[float('inf')]*len(mat[0]) for i in range(len(mat))]
        queue = deque()
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] == 0:
                    output[row][col] = 0
                    queue.append((row, col))

        rows = [-1, 1, 0, 0]
        cols = [0, 0, 1, -1]

        while len(queue):
            curr_row, curr_col = queue.popleft()
            for i in range(len(rows)):
                new_row = curr_row + rows[i]
                new_col = curr_col + cols[i]
                if (new_row >= 0 and new_row < len(mat) 
                and new_col >= 0 and new_col < len(mat[0])):
                    if output[new_row][new_col] > output[curr_row][curr_col] + 1:
                        output[new_row][new_col] = output[curr_row][curr_col] + 1
                        queue.append((new_row, new_col))


        return output



            
