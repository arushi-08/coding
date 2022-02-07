class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        if len(nums)==1:
            return nums[0]
        while(left<=right):
            mid = (left + right) // 2
            print(mid)
            if mid+1< len(nums) and nums[mid] > nums[mid+1]:
                return nums[mid + 1]
            else:
                right = mid - 1
                if right < left:
                    left, right = mid + 1, len(nums) - 1
        
        
        return nums[0]
