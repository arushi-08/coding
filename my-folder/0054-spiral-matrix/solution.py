class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        ans = []
        left = 0
        right = len(matrix[0])-1
        up = 0
        down = len(matrix)-1

        while up <= down and left <= right:
            for i in range(left, right+1):
                ans.append(matrix[up][i])
            up += 1
        
            for i in range(up, down+1):
                ans.append(matrix[i][right])
            right -= 1

            if len(ans) == len(matrix) * len(matrix[0]):
                break

            for i in range(right, left-1, -1):
                ans.append(matrix[down][i])
            down -= 1

            for i in range(down, up-1, -1):
                ans.append(matrix[i][left])
            left += 1
        

        return ans
            



