class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if len(nums) < 1:
            return -1
        if len(nums) == 1:
            if target == nums[0]:
                return 0
            else:
                return -1
        if target == nums[int(len(nums)/2)]:
            return int(len(nums)/2)
        
        elif target < nums[int(len(nums)/2)]:
            return self.search(nums[:int(len(nums)/2)], target)
        elif target > nums[int(len(nums)/2)]:
            ans = self.search(nums[int(len(nums)/2)+1:], target)
            if ans>=0:
                return ans + int(len(nums)/2) + 1
            else:
                return -1
