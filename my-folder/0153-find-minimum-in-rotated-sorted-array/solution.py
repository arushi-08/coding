class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # min is left > mid < right

        # 2,1,5,4,3
        # 1,2,3,4,5
        if len(nums) == 1:
            return nums[0]

        if nums[0] < nums[-1]:
            return nums[0]

        st = 0
        ed = len(nums) - 1
        while st <= ed:
            mid = (st + ed) // 2
           
            if nums[mid] > nums[mid+1]:
                return nums[mid + 1]

            if nums[mid-1] > nums[mid]:
                return nums[mid]

            if nums[mid] > nums[0]:
                st = mid + 1

            else:
                ed = mid - 1
            
        return nums[st]
