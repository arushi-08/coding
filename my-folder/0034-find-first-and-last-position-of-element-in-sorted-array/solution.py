class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        first = self.find_first(nums, target)
        last = self.find_last(nums, target)
        return [first, last]

    def find_first(self, nums, target):

        start = 0
        end = len(nums)-1
        ans = -1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                ans = mid
                end = mid - 1

            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        
        return ans

    def find_last(self, nums, target):

        start = 0
        end = len(nums)-1
        ans = -1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                ans = mid
                start = mid + 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        
        return ans
