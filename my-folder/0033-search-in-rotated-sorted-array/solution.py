class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        """
        if st < mid : sorted subarr
            check if val is in between, if it is go to left subarr
            else go to left side
        
        """
        
        st = 0
        ed = len(nums)-1
        while st <= ed:
            mid = (st + ed) // 2

            if nums[mid] == target:
                return mid

            if nums[st] <= nums[mid]:
                if nums[st] <= target <= nums[mid]:
                    ed = mid - 1
                else:
                    st = mid + 1
            
            else:
                if nums[mid] <= target <= nums[ed]:
                    st = mid + 1
                else:
                    ed = mid - 1
        
        return -1

