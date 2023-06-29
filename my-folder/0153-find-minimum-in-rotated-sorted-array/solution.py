class Solution:
    def findMin(self, nums: List[int]) -> int:
        

        start = 0
        end = len(nums)-1
        res = float('inf')
        while start <= end:
            mid = (start + end)//2
            res = min(res, nums[mid])
            if nums[mid] >= nums[start]: # left sorted
                if nums[start] > nums[end]: # rotated
                    start = mid + 1
                else: # not rotated
                    end = mid - 1
            
            else:
                if nums[start] > nums[end]: # rotated
                    end = mid - 1
                else:
                    start = mid + 1
        
        return nums[start] if nums[start] < res else res
