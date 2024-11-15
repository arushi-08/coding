class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left = 0
        right = len(nums)-1
        while left < right:
            mid = (left + right)//2
            if mid - 1 >= 0 and nums[mid-1] > nums[mid] and mid+1 < len(nums) and nums[mid] < nums[mid+1]:
                return nums[mid]
            if nums[left] > nums[right]:
                if nums[left] > nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[left] < nums[right]:
                if nums[right] > nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

        return nums[left]
