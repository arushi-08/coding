class Solution:
    def sortedSquares(self, arr: List[int]) -> List[int]:
        left = 0
        right = len(arr)-1
        output = [0] * len(arr)
        output_idx = len(arr)-1

        while left <= right:
            left_squared = pow(arr[left], 2)
            right_squared = pow(arr[right], 2)
            if left_squared > right_squared:
                output[output_idx] = left_squared
                left += 1
            else:
                output[output_idx] = right_squared
                right -= 1
            output_idx -= 1

        return output

                
        
            
            
