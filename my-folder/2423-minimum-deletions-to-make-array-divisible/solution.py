class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        """ find min(nums) that divides all in numsDivide
            if not there, check second min(nums), check third min ...
            put set of nums in heap or sort set of nums
            if min found, find minimum delete operations
        """
        
        if min(nums) > min(numsDivide): return -1 
        
        arr = list(set(nums))
        arr.sort()
        
        arr2 = list(set(numsDivide))
        # print("arr2", arr2)
        min_arr = 0
        for i in range(len(arr)):
            min_arr_not_found = False
            for j in range(len(arr2)):
                # print(arr2[j], arr[i], arr2[j] % arr[i])
                if arr2[j] % arr[i] != 0:
                    min_arr_not_found = True
                    break
            
            if min_arr_not_found == False:
                min_arr = arr[i]
                break
        
        if min_arr == 0: return -1
#         find all nums smaller than min_arr
        # print("min_arr", min_arr)
        deletions = 0
        for i in range(len(nums)):
            if nums[i] < min_arr:
                deletions += 1
        
        return deletions
        
        
