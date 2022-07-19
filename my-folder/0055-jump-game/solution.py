class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # goal: check if can reach the end
        # if all above 0 then True
        # else check if you can bypass 0
        # O(N^2) might work
        if not nums: return False
        if nums.count(0) == 0: return True
        
        last_position = len(nums) - 1
        i = len(nums) - 2
        while i >= 0:
            if nums[i] + i >= last_position:
                last_position = i
                i = last_position - 1
                
            else:
                i -= 1
        # print(last_position)
        if last_position == 0:
            return True
        return False
            
        
        
        
