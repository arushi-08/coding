class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        # given nums and target
        # find sum of 3 nums closest to target
        # 
        #

        nums.sort()
        closest_found = float('inf')
        # -4,-1,1,2 -> -4-1+1 | -4+1+2

        for i in range(len(nums)):
            
            st = i+1
            ed = len(nums)-1
            while st < ed:
                add = nums[i] + nums[st] + nums[ed]
                if add == target:
                    return target
                
                if abs(closest_found - target) > abs(add - target):
                    closest_found = add
                
                if add < target:
                    st += 1
                else:
                    ed -= 1
        
        return closest_found
        


