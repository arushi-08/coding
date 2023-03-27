class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if not nums: return -1
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid]==target:
                return mid
            # if rotation is in left half
            if nums[left] <= nums[mid]:
                # non rotated part
                if nums[left] <= target and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # if rotation is in second half
            else:
                # non rotated part
                if nums[right] >= target and target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return left if left >=0 and left < len(nums) and nums[left] == target else -1
