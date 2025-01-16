class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        # output elements in spiral order
        top = 0
        bottom = n-1
        left = 0
        right = n-1

        matrix = [[0]*n for _ in range(n)]
        element = 1
        while top <= bottom or left <= right:
            for i in range(left, right+1):
                matrix[top][i] = element
                element += 1
            top += 1
            for i in range(top, bottom+1):
                matrix[i][right] = element
                element += 1
            right -= 1
            for i in range(right,left-1,-1):
                matrix[bottom][i] = element
                element += 1
            bottom -= 1
            for i in range(bottom,top-1,-1):
                matrix[i][left] = element
                element += 1
            left += 1
        
        ans = []
        for i in range(n):
            ans.append(matrix[i])
        
        return ans
