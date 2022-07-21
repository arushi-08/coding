class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        
        lis = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    lis[i] = max(lis[i], lis[j] + 1)
        
        lds = [1] * n
        for i in range(n-2, -1, -1):
            for j in range(n-1, i, -1):
                if nums[i]>nums[j]:
                    lds[i] = max(lds[i], lds[j] + 1)
        
        size_of_mountain_arr = 0
        for i in range(len(lis)):
            if lis[i] > 1 and lds[i] > 1:
                size_of_mountain_arr = max(size_of_mountain_arr, 
                                           lis[i] + lds[i] - 1 )
        
        return n - size_of_mountain_arr
                
