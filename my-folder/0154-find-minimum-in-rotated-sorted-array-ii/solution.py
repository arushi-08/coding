class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # suppose array is sorted in ascending order
        # between 1 and n times

        # find min in array that is rotated and has duplicates
        if len(nums) == 1: return nums[0]

        if nums[0] < nums[-1]:
            return nums[0]
        
        st = 0
        ed = len(nums)-1
        while st < ed:
            mid = (st + ed) // 2
            print(st, ed, mid)
            if mid + 1 < len(nums) and nums[mid] > nums[mid+1]:
                return nums[mid+1]
            
            if mid - 1 >= 0 and nums[mid-1] > nums[mid]:
                return nums[mid]
            
            if nums[st] == nums[mid] == nums[ed]:
                st += 1
                ed -= 1
                continue

            if nums[mid] <= nums[ed]:
                ed = mid
            elif nums[mid] > nums[ed]:
                st = mid + 1
                

        return nums[st]
