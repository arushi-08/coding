class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        remove_ptr = 0
        non_remove_ptr = len(nums)-1
        while remove_ptr < non_remove_ptr:
            if nums[remove_ptr] == val:
                while non_remove_ptr > remove_ptr and nums[non_remove_ptr] == val:
                    non_remove_ptr -= 1
                if non_remove_ptr > remove_ptr:
                    nums[remove_ptr], nums[non_remove_ptr] = nums[non_remove_ptr], nums[remove_ptr] 
                    non_remove_ptr -= 1
                    remove_ptr += 1
                else:
                    break
            else:
                remove_ptr += 1
        
        return len(nums) - nums.count(val)
                
