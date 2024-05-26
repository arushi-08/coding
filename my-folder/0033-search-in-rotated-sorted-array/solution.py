class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        st = 0
        ed = len(nums)-1
        while st < ed:
            mid = (st + ed)//2
            print("mid", mid, "st", st, "ed", ed)
            if nums[mid] == target:
                return mid
            
            if nums[mid] >= nums[st]:
                # left half is sorted
                if nums[st] <= target and target < nums[mid]:
                    ed = mid - 1
                else:
                    st = mid + 1
            
            if nums[mid] <= nums[ed]:
                if nums[mid] < target and target <= nums[ed]:
                    st = mid + 1
                else:
                    ed = mid - 1
            
        return st if nums[st] == target else -1
