class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        
        zero_arr = [0] * (len(nums)+1)

        for i in range(len(queries)):
            zero_arr[queries[i][0]] += 1
            zero_arr[queries[i][1]+1] -= 1
        
        print(zero_arr)
        for i in range(1, len(zero_arr)):
            zero_arr[i] += zero_arr[i-1]
            if i < len(nums) and zero_arr[i] < nums[i]:
                return False
        
        if zero_arr[0] < nums[0]:
            return False
        return True

