class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # [3,4,5,1,2]

        # half array is sorted
        # other half array is not sorted

        # 3,4,5                           |    5,1,2
        # left (1) < right (2)            |    left > right
        # left < mid -> sorted           |    
        #   

        # 4,0,1,2,3.  |  2,3,4,0,1
        # if left < right -> not rotated

        # if left > right -> rotated -> check half till mid
        
        # 3,4,5,1,2
        # 2,1
        st = 0
        ed = len(nums)-1
        if nums[st] <= nums[ed]:
            return nums[st]

        while st <= ed:
            mid = (st + ed) // 2

            if nums[mid] > nums[mid+1]:
                return nums[mid+1]

            if nums[mid] <= nums[ed]:
                ed = mid
            
            else:
                st = mid + 1
        
        return nums[st]


        
