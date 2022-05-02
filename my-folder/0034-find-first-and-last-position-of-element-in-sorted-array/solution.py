class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if not nums or target not in nums:
            return [-1, -1]
        
        l = 0
        r = len(nums) - 1
        lower_bound = len(nums) - 1
        
        while(l < r):
            mid = (l + r) // 2
            if nums[mid] == target:
                r = mid
                lower_bound = min(mid, lower_bound)
            
            elif nums[mid] > target:
                r = mid
            
            else:
                l = mid + 1
        
        l = 0
        r = len(nums) - 1
        upper_bound = 0
        
        while(l < r):
            mid = (l + r) // 2
            print(nums[mid], mid, l, r)
            
            if nums[mid] == target:
                l = mid + 1
                upper_bound = max(mid, upper_bound)
            
            elif nums[mid] > target:
                r = mid
            
            else:
                l = mid + 1
        
        if nums[l] == target:
            upper_bound = l
        return [lower_bound, upper_bound]
        
        
