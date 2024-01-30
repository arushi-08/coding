class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums)-1
        while left < right:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if nums[left] <= target and target < nums[mid]:
                    right = mid - 1
                elif nums[left] > target or target > nums[mid]:
                    left = mid + 1
                # else:
                    # print(nums[left], nums[mid], nums[right])
            elif nums[mid] < nums[right]:
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                elif nums[mid] > target or target > nums[right]:
                    right = mid - 1

        if nums[left] == target: 
            return left
        return -1

