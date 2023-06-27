class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ansstart, anssend = -1, -1
        if not nums: return [ansstart, anssend]
        start = 0
        end = len(nums)-1
        while start <= end:
            mid = (start + end) // 2
            
            if nums[mid] == target:
                ansstart = mid
                end = mid - 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        if 0<=start<len(nums) and nums[start] == target:
            ansstart = start

        start = ansstart
        end = len(nums)-1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                anssend = mid
                start = mid + 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        if 0<=end<len(nums) and nums[end] == target:
            anssend = end
        
        return [ansstart, anssend]
        
